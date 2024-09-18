#Estimated due date / maximum lateness scheduling

def max_lateness_scheduling(tasks):
    # Sort tasks by their due dates (Earliest Due Date first)
    tasks.sort(key=lambda task: task[2])  # Sort by due date, task[2] is due date

    current_time = 0
    max_lateness = 0
    schedule = []  # To store the scheduled tasks

    # Schedule tasks
    for task in tasks:
        task_name, processing_time, due_date = task
        
        # Schedule the task and update the current time
        current_time += processing_time

        # Calculate lateness for this task
        lateness = max(0, current_time - due_date)
        max_lateness = max(max_lateness, lateness)

        # Add task to the schedule
        schedule.append((task_name, current_time, lateness))

    return schedule, max_lateness



#  tasks as (task_name, processing_time, due_date)
tasks = [
    ("Task 1", 4, 6),
    ("Task 2", 2, 8),
    ("Task 3", 1, 9),
    ("Task 4", 3, 5),
    ("Task 5", 5, 7)
]

# Schedule the tasks using EDD algorithm
schedule, max_lateness = max_lateness_scheduling(tasks)

# Output the schedule and maximum lateness
print("Scheduled Tasks:")
for task in schedule:
    print(f"{task[0]}: Completion Time = {task[1]}, Lateness = {task[2]}")

print(f"\nMaximum Lateness: {max_lateness}")
