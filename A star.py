import heapq

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=None):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.g = parent.g + 1 if parent else 0
        self.h = sum(1 if puzzle[i][j] != 0 and puzzle[i][j] != 3*i + j + 1 else 0
                     for i in range(3) for j in range(3))
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def is_goal(self):
        return self.h == 0

    def get_children(self):
        children = []
        empty_pos = next((i, j) for i in range(3) for j in range(3) if self.puzzle[i][j] == 0)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_pos = (empty_pos[0] + move[0], empty_pos[1] + move[1])
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
                new_puzzle = [row[:] for row in self.puzzle]
                new_puzzle[empty_pos[0]][empty_pos[1]], new_puzzle[new_pos[0]][new_pos[1]] = \
                    new_puzzle[new_pos[0]][new_pos[1]], new_puzzle[empty_pos[0]][empty_pos[1]]
                children.append(PuzzleState(new_puzzle, self, move))
        return children

def astar(initial_state, final_state):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return path[::-1]

        closed_list.add(tuple(map(tuple, current_state.puzzle)))

        for child in current_state.get_children():
            if tuple(map(tuple, child.puzzle)) not in closed_list:
                child.f = child.g + child.h
                heapq.heappush(open_list, child)

    return None

def get_puzzle_from_user(prompt):
    print(prompt)
    return [list(map(int, input(f"Enter row {i + 1} (separated by space): ").split())) for i in range(3)]

if __name__ == "__main__":
    initial_puzzle = get_puzzle_from_user("Enter the initial state of the puzzle:")
    final_puzzle = get_puzzle_from_user("Enter the final state of the puzzle:")
    
    initial_state = PuzzleState(initial_puzzle)
    final_state = PuzzleState(final_puzzle)

    solution = astar(initial_state, final_state)
    if solution:
        print("Solution found:")
        for step, state in enumerate(solution):
            print(f"Step {step + 1}:")
            for row in state.puzzle:
                print(row)
            print(f"Heuristic value (h): {state.h}")
            print()
    else:
        print("No solution found.")
