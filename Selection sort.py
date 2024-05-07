def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        small = i  
        for j in range(i + 1, n):
            if arr[j] < arr[small]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]

def print_arr(arr):
    for elem in arr:
        print(elem, end=" ")
    print()

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements of the array:")
    for _ in range(n):
        elem = int(input())
        arr.append(elem)

    print("Before sorting array elements are - ")
    print_arr(arr)
    selection_sort(arr)
    print("After sorting array elements are - ")
    print_arr(arr)

