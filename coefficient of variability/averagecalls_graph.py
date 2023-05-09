import os
import matplotlib.pyplot as plt

# Initialize a dictionary to hold the combined subtype counts for all files
combined_counts = {}

# Loop through all files with names indv*_ScSubtypeCALLS.txt
for filename in os.listdir():
    if filename.startswith('indv') and filename.endswith('ScSubtypeCALLS.txt'):
        # Read the file and count the number of cells for each subtype
        subtype_counts = {}
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    values = line.split('\t')
                    if len(values) == 2:
                        cell_id, subtype = values
                        subtype_counts[subtype] = subtype_counts.get(subtype, 0) + 1
        
        # Combine the subtype counts for this file with the combined counts
        for subtype, count in subtype_counts.items():
            prefix = f"{filename}: "
            combined_counts[prefix + subtype] = combined_counts.get(prefix + subtype, 0) + count

# Define the colors for each subtype
colors = {
    "Basal_SC": "tab:blue",
    "LumA_SC": "tab:orange",
    "LumB_SC": "tab:green",
    "Her2E_SC": "tab:red"
}

# Create a bar graph of the combined subtype counts
plt.bar(combined_counts.keys(), combined_counts.values(), color=[colors[subtype.split(": ")[1].replace('"', '')] for subtype in combined_counts.keys()])

# Add a legend in the top right corner
plt.legend(handles=[plt.Rectangle((0,0),1,1, color=color) for subtype, color in colors.items()], labels=colors.keys(), loc='upper right', bbox_to_anchor=(1.15, 1))

plt.xlabel('Subtype')
plt.ylabel('Number of Cells')
plt.xticks(rotation=90)
plt.show()
