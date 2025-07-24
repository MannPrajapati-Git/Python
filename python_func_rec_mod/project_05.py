# project : todo list 

todo_list = []

def show_menu():
    print("\n===== To-Do Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    todo_list.append(task)
    print("✅ Task added!")

def view_tasks():
    if not todo_list:
        print(" No tasks yet!")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        removed = todo_list.pop(num - 1)
        print(f" Removed: {removed}")
    except:
        print(" Invalid input!")

# Main Loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting To-Do List. Bye!")
        break
    else:
        print("Invalid choice. Try again.")
