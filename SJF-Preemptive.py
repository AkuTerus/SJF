# Python program to implement the Shortest Job First algorithm without using a matrix

# Taking the input of the number of processes
n = int(input("Enter the number of processes: "))

processes = []

print("Enter the Burst Time of the processes:")

# Taking the input of the burst times of the processes and assigning process Ids
for i in range(n):
    burst_time = int(input(f"P{i + 1}: "))
    processes.append((i + 1, burst_time))

# Sorting the processes according to their burst time
processes.sort(key=lambda x: x[1])
print(processes)


waiting_time = 0
turnaround_time = 0

# Calculating the waiting times and Turn Around Time for each process
print("P B_T W_T TA_T")
for i in range(n):
    waiting_time += processes[i][1]
    turnaround_time += waiting_time
    print(f"P{processes[i][0]} {processes[i][1]} {waiting_time - processes[i][1]} {turnaround_time}")
    # print(processes)

# Calculating the average waiting time and average Turn Around Time
avg_waiting_time = waiting_time / n
avg_turnaround_time = turnaround_time / n

print(f"\nThe average Waiting Time of the whole sequence of processes is = {round(avg_waiting_time)}")
print(f"The average Turn Around Time of the processes is = {round(avg_turnaround_time)}")
