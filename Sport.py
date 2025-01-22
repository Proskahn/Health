import json
import matplotlib.pyplot as plt
from collections import Counter

# File path
file_paths = {
    "Sport": r"Sport.json"
}

# Open and load the JSON file
with open(file_paths["Sport"], 'r') as file:
    data = json.load(file)

# Extract activities
activities = []
for activity in data.values():
    if isinstance(activity, list):  # If the activity is a list, extend the activities list
        activities.extend(activity)
    else:  # If the activity is a string, append it directly
        activities.append(activity)

# Count the occurrences of each activity
activity_counts = Counter(activities)

# Prepare data for the pie chart
labels = list(activity_counts.keys())
sizes = list(activity_counts.values())

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12})
plt.title(f"Sport Distribution in Last {len(data)} Days", fontsize=16, fontweight='bold')
plt.tight_layout()

# Show plot
plt.show()
