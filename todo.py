todo_items = []

while True:
    print("Please, select an operation!\n"
        "---\n"
        "0. Exit Program\n"
        "1. Add task\n"
        "2. List tasks\n"
        "3. Remove task\n")

    select = int(input("Select operation (0-3): "))

    if select == 0:
        print("Exiting program . . .")
        break
    elif select == 1:
        print("You have chosen to add a task!\n"
            "---")
        task = input("Enter the task you want to add: ")
        todo_items.append(task)
        print(f"'{task}' added succesfully!\n")
    elif select == 2:
        print("You have chosen to list your tasks!\n"
            "---")
        if len(todo_items) == 0:
            print("No tasks found. Please, add a task first\n")
        else:
            print("Your current tasks are: ")
            for index, item in enumerate(todo_items, start=1):
                print(f"{index}, {item}"
                "\n")
    else:
        print("Invalid Input.")
