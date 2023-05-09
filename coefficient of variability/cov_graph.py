import matplotlib.pyplot as plt

# Coefficient of variation values from the 26 files (replace with your own data)
coef_var = [46.72, 48.85, 54.21, 51.42, 49.22, 53.02, 48.01, 48.13, 49.53, 
            51.85, 49.72, 46.21, 50.86, 52.80, 56.42, 45.78, 49.99, 50.23, 
            48.24, 51.77, 49.30, 42.82, 51.95, 57.72, 52.63, 58.54]

# Round coefficient of variation values to nearest 2 decimal places
coef_var_rounded = [round(cv, 2) for cv in coef_var]

# Create bar plot
plt.bar(range(1, 27), coef_var_rounded, align='center')

# Set axis labels and title
plt.xlabel('File')
plt.ylabel('Coefficient of Variation (%)')
plt.title('Coefficient of Variation for 26 Files')

# Display plot
plt.show()
