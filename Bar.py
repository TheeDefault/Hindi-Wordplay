import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV data into DataFrames
dataD = pd.read_csv("poem_analysis_Default.csv")
dataC = pd.read_csv("poem_analysi_Custom.csv")

# Calculate the mean of the 4 features for both datasets
mean_dataD = dataD.mean()
mean_dataC = dataC.mean()

# Create a DataFrame to hold the means for easy plotting
means_df = pd.DataFrame({
    'Features': mean_dataD.index,  # Feature names
    'poem_analysis_Default.csv': mean_dataD.values,  # Means from dataD
    'poem_analysi_Custom.csv': mean_dataC.values  # Means from dataC
})

# Set the index as Features for plotting
means_df.set_index('Features', inplace=True)

# Plot a grouped bar graph
ax = means_df.plot(kind='bar', figsize=(10, 6), width=0.8)
ax.set_title('Grouped Bar Graph of Feature Means')
ax.set_xlabel('Features')
ax.set_ylabel('Mean Value')
ax.set_xticklabels(means_df.index, rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
