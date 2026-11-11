todo_items = []

while True:
    print("Please, select an operation!\n"
        "---\n"
        "0. Exit Program\n"
        "1. Add task\n"
        "2. List tasks\n"
        "3. Remove task\n")

    # Ensures a number is input.
    while True:
        try:
            select = int(input("Select operation (0-3): "))
            break
        except ValueError:
            print("Invalid input! Please, enter a number.")

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
        if len(todo_items) == 0:
            print("No tasks found. Please, add a task first\n")
        else:
            print("Your current tasks are: \n"
                "---")
            for index, item in enumerate(todo_items, start=1):
                print(f"{index}. {item}")

    elif select == 3:
        if len(todo_items) == 0:
            print("No tasks found. Please, add a task first\n")
        else:
            print("Your current tasks are: \n"
                "---")
            for index, item in enumerate(todo_items, start=1):
                print(f"{index}. {item}")

            try:
                index = int(input("Enter the task number you want to remove: ")) -1 # Changing from user index to code index
                if 0 <= index < len(todo_items):
                    final_index = todo_items.pop(index)
                    print (f"Task '{final_index}' removed succesfully!")

            except ValueError:
                print("Invalid input. Please, enter a valid task number")

    else:
        print("Invalid Input.")
