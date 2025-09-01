# -------------------------------
# 5. File Handling: Save & Read
# -------------------------------

# Write tasks to a file
tasks = ["Task 1: Update records", "Task 2: Send invoice", "Task 3: Call client"]

with open("my_tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

print("✅ Tasks saved to 'my_tasks.txt'")

# Read tasks back
print("\n📋 Tasks from file:")
with open("my_tasks.txt", "r") as file:
    content = file.read()
    print(content)
print("-" * 30)
