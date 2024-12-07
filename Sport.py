import json
import matplotlib.pyplot as plt
from collections import Counter
# File path
file_paths = {
    "Sport": r"C:\Users\DEZHKAN\Desktop\Health\Sport.json"
}

# Open and load the JSON file
with open(file_paths["Sport"], 'r') as file:
    data = json.load(file)

# Extract days and activities
days = list(data.keys())
activities = list(data.values())

# Assign a numeric value to each activity
activity_mapping = {activity: idx for idx, activity in enumerate(set(activities))}
activity_values = [activity_mapping[activity] for activity in activities]

# Create a timeline plot
plt.figure(figsize=(10, 5))
plt.scatter(days, activity_values, color='purple', s=100, label="Activity")
plt.yticks(list(activity_mapping.values()), list(activity_mapping.keys()), fontsize=10)
plt.title("Activity Timeline", fontsize=16, fontweight='bold')
plt.xlabel("Days", fontsize=12)
plt.ylabel("Activity", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show plot
plt.show()
