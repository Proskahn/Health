import json

# File paths
file_paths = {
    "Beer": r"C:\Users\DEZHKAN\Desktop\Health\Beer.json",
    "Smoking": r"C:\Users\DEZHKAN\Desktop\Health\Smoking.json",
    "Weight": r"C:\Users\DEZHKAN\Desktop\Health\Weight.json",
    "Step": r"C:\Users\DEZHKAN\Desktop\Health\Step.json",
    "Stock": r"C:\Users\DEZHKAN\Desktop\Health\Stock.json",
    "FoodExpense": r"C:\Users\DEZHKAN\Desktop\Health\FoodExpense.json"
}

averages = {}

# Compute averages
for title, path in file_paths.items():
    try:
        with open(path, 'r') as file:
            data = json.load(file)
        
        # Extract values and calculate the average
        values = list(data.values())
        averages[title] = sum(values) / len(values) if values else 0
    except Exception as e:
        averages[title] = None  # Could not compute average

# Display averages
for title, avg in averages.items():
    if avg is not None:
        print(f"The average for {title} is: {avg:.2f}")
    else:
        print(f"Could not compute the average for {title}.")
