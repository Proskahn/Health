import json
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# File paths
file_paths = {
    "Beer": r"data/Beer.json",
    "Smoking": r"data/Smoking.json",
    "Weight": r"data/Weight.json",
    "Step": r"data/Step.json",
    "Stock": r"data/Stock.json",
    "FoodExpense": r"data/FoodExpense.json"
}

# Generate color palette
colors = cm.tab10.colors  # Use a colormap for consistent yet colorful plots

# Create a figure for the subplots
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 12))
axes = axes.flatten()  # Flatten to iterate easily
fig.suptitle("Over Days", fontsize=20, fontweight='bold', color="darkblue")

# Plot each JSON file
for idx, (title, path) in enumerate(file_paths.items()):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
        
        # Extract days and values
        days = list(data.keys())
        values = list(data.values())
        
        # Plot data
        axes[idx].plot(days, values, marker='o', linestyle='-', linewidth=2, 
                       color=colors[idx % len(colors)], label=title)
        axes[idx].set_title(title, fontsize=14, fontweight='bold')
        axes[idx].set_ylabel("Values", fontsize=12)
        axes[idx].tick_params(axis='x', rotation=45, labelsize=10)
        axes[idx].tick_params(axis='y', labelsize=10)
        axes[idx].grid(True, linestyle='--', alpha=0.6)
        axes[idx].legend(fontsize=10)
    except Exception as e:
        axes[idx].text(0.5, 0.5, f"Error loading {title}", 
                       fontsize=12, ha='center', va='center')
        axes[idx].set_title(title, fontsize=14, fontweight='bold')
        axes[idx].axis("off")

# Remove any unused subplots
for idx in range(len(file_paths), len(axes)):
    axes[idx].axis("off")

# Adjust layout to leave even more space for the title
plt.tight_layout(rect=[0, 0, 1, 0.88])  # Reserve more space for the title
plt.subplots_adjust(top=0.85)  # Push subplots down even further
plt.show()
