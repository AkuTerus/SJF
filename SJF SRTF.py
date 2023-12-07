# Python program to implement the Shortest Remaining Time First algorithm

# Function to find the process with the shortest remaining time
def find_shortest_remaining_time(time, n, remaining_time, arrival_time):
    min_time = float('inf')
    min_index = -1
    #Menghitung apakah sisa waktu terkecil dari proses yang telah di intrupsi
    for i in range(n):
        if remaining_time[i] > 0 and arrival_time[i] <= time and remaining_time[i] < min_time:
            min_time = remaining_time[i]
            min_index = i

    return min_index

# Taking the input of the number of processes
n = int(input("Enter the number of processes: "))

# Creating a matrix for storing the Process Id, Burst Time, Arrival Time, Waiting Time, Turn Around Time
mat = [[0 for j in range(5)] for i in range(n)]
avg_wttime, avg_tatime = 0, 0

print("Enter the Arrival Time and Burst Time of the processes:")

# Taking the input of the arrival time and burst time of the processes
for i in range(n):
    mat[i][2] = int(input(f"Arrival Time for P{i + 1}: "))
    mat[i][1] = int(input(f"Burst Time for P{i + 1}: "))
    mat[i][0] = i + 1

remaining_time = [mat[i][1] for i in range(n)]
time = 0

# Sorting the processes based on their arrival time
mat.sort(key=lambda x: x[2])

print("P A_T B_T W_T TA_T")

# Implementing the SRTF algorithm
while True:
    index = find_shortest_remaining_time(time, n, remaining_time, [mat[i][2] for i in range(n)])
    
    if index == -1:
        break
    
    remaining_time[index] -= 1
    #menghitung waktu yang tersisa
    if remaining_time[index] == 0:
        mat[index][4] = time + 1 - mat[index][2]
        mat[index][3] = mat[index][4] - mat[index][1]

    time += 1

# Printing the data in table form
for i in range(n):
    print(f"P{mat[i][0]} {mat[i][2]} {mat[i][1]} {mat[i][3]} {mat[i][4]}")

# Calculating the average waiting time and turn around time
avg_wttime = sum(mat[i][3] for i in range(n)) / n
avg_tatime = sum(mat[i][4] for i in range(n)) / n

print(f"The average Waiting Time of the processes is = {avg_wttime}")
print(f"The average Turn Around Time of the processes is = {avg_tatime}")
