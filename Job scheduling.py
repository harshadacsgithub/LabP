def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    result = [-1] * (max_deadline + 1)
    total_profit = 0
    for job in jobs:
        for j in range(job[1], 0, -1):
            if result[j] == -1:
                result[j] = job[0]
                total_profit += job[2]
                break
    return result[1:], total_profit

def take_input():
    jobs = []
    n = int(input("Enter the number of jobs: "))
    for i in range(n):
        name = input("Enter job name: ")
        deadline = int(input("Enter deadline for job {}: ".format(name)))
        profit = int(input("Enter profit for job {}: ".format(name)))
        jobs.append((name, deadline, profit))
    return jobs

print("Enter details for each job:")
jobs = take_input()
schedule, total_profit = job_scheduling(jobs)
print("Scheduled Jobs:", schedule)
print("Total profit:", total_profit)

