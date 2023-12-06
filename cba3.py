class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.end_time = None
        self.waiting_time = 0

def sjf_preemptive(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    n = len(processes)
    time_chart = []

    current_time = 0
    total_execution_time = sum(process.burst_time for process in processes)

    while total_execution_time > 0:
        runnable_processes = [process for process in processes if process.arrival_time <= current_time and process.remaining_time > 0]

        if not runnable_processes:
            current_time += 1
            continue

        selected_process = min(runnable_processes, key=lambda x: x.remaining_time)
        
        if selected_process.start_time is None:
            selected_process.start_time = current_time

        time_chart.append(selected_process.process_id)
        selected_process.remaining_time -= 1
        current_time += 1
        total_execution_time -= 1

        if selected_process.remaining_time == 0:
            selected_process.end_time = current_time
            selected_process.waiting_time = selected_process.start_time - selected_process.arrival_time

    return time_chart

# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, 0, 7),
        Process(2, 2, 4),
        Process(3, 4, 1),
        Process(4, 5, 4)
    ]

    result = sjf_preemptive(processes)

    # Display the timeline of process execution
    print("Timeline of process execution:", result)

    # Display the details of each process including corrected waiting time
    for process in processes:
        print(process.waiting_time)
        print(f"Process {process.process_id}: Arrival Time={process.arrival_time}, Burst Time={process.burst_time}, Waiting Time={process.waiting_time}")

    # Calculate and display average waiting time and average turn around time
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_turnaround_time = sum(process.end_time - process.arrival_time for process in processes)
    

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(process.waiting_time)