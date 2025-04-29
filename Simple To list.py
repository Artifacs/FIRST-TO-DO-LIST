tasks = []

Start = input("Welcome to task organizer\ndo you want to get organize right now?(Y/N): ")

if Start == "Y":
    taking_tasks = input("What is your first task you want to input?")
    tasks.append(taking_tasks)
    print(f"Your task {len(tasks)} {tasks}")

else:
    print("HAVE A NICE DAY!")
