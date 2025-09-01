# -------------------------------
# 4. Functions & Reusability
# -------------------------------

def send_reminder(name, task):
    """Sends a personalized reminder"""
    return f"Hi {name}, don't forget to: {task}!"

def calculate_bonus(salary, rating):
    """Calculate bonus based on performance rating"""
    if rating == "A":
        return salary * 0.15
    elif rating == "B":
        return salary * 0.10
    else:
        return salary * 0.05

# Use the functions
print(send_reminder("Priya", "Submit timesheet"))

base_salary = 60000
bonus = calculate_bonus(base_salary, "B")
print(f"Bonus: ₹{bonus:.2f}")
print("-" * 30)
