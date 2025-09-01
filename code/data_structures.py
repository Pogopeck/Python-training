# -------------------------------
# 2. Data Structures
# -------------------------------

# List - Ordered, mutable
tasks = ["Email team", "Review report", "Schedule meeting"]
tasks.append("Update dashboard")
print("Tasks:", tasks)

# Access by index
print("First task:", tasks[0])

# Dictionary - Key-value pairs
employee = {
    "name": "Abdul",
    "role": "developer",
    "department": "Operations",
    "active": True
}
print("Employee role:", employee["role"])

# List of dictionaries
team = [
    {"name": "Piyush", "task": "Complete audit"},
    {"name": "Surabhi", "task": "Submit timesheet"}
]

for member in team:
    print(f"{member['name']} needs to: {member['task']}")

print("-" * 30)
