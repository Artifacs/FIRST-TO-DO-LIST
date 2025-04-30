tasks = []

def task_adder():
    taking_tasks = input("What is your first task you want to input?: ")
    tasks.append(taking_tasks)
    
    more = input("Do you want to add another task? (Y/N): ")
    if more.lower() == 'y':
        task_adder()
    else:
        print("Your tasks are:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

task_adder()

