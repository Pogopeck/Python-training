# -------------------------------
# 3. Control Flow: if, for, while
# -------------------------------

# If-elif-else: Bonus calculation
performance_score = 82

if performance_score >= 90:
    bonus = 10000
elif performance_score >= 75:
    bonus = 5000
else:
    bonus = 0

print(f"Performance Score: {performance_score} → Bonus: ₹{bonus}")

# For loop: Send reminders
pending_tasks = ["Submit report", "Approve leave", "Review budget"]

print("\nDaily Reminders:")
for task in pending_tasks:
    print(f"🔔 {task}")

# While loop: Countdown to meeting
countdown = 3
while countdown > 0:
    print(f"Meeting in {countdown} mins...")
    countdown -= 1
print("Meeting started!")
print("-" * 30)
