tasks = []
while True:
    print("\n1. Add Task  2. View Tasks  3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Added!")
    elif choice == "2":
        print("\n📋 Your Tasks:")
        for t in tasks: print(f"  • {t}")
    elif choice == "3":
        print("👋 Goodbye!")
        break
