import numpy as np

# Iterate through files
for i in range(1, 27):
    filename = f"indv{i}_ScSubtypeCALLS.txt"
    
    # Load data from file
    data = np.loadtxt(filename, dtype='str', skiprows=1)

    # Assign values to each subtype
    subtypes = np.unique(data[:, 1])
    values = np.arange(1, len(subtypes) + 1)
    subtype_values = dict(zip(subtypes, values))
    assigned_values = np.array([subtype_values[s] for s in data[:, 1]])

    # Calculate mean and standard deviation of assigned values
    mean_value = np.mean(assigned_values)
    std_value = np.std(assigned_values)

    # Calculate coefficient of variation
    if mean_value != 0:
        cov_value = std_value / mean_value * 100
    else:
        cov_value = 0

    print(f"File {i}:")
    print(f"Mean value: {mean_value}")
    print(f"Standard deviation: {std_value}")
    print(f"Coefficient of variation: {cov_value}%\n")
