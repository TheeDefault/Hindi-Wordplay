import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into DataFrames
dataD = pd.read_csv("poem_analysis_Default.csv")
dataC = pd.read_csv("poem_analysi_Custom.csv")

# Create a figure for side-by-side boxplots
fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

# Boxplot for poem_analysis_Default.csv
axes[0].boxplot(dataD.values, labels=dataD.columns, patch_artist=True, 
                boxprops=dict(facecolor="blue", color="black"),
                medianprops=dict(color="red"),
                whiskerprops=dict(color="green"),
                capprops=dict(color="yellow"))
axes[0].set_title("Box Plot of Features in poem_analysis_Default.csv")
axes[0].set_xlabel("Features")
axes[0].set_ylabel("Values")
axes[0].tick_params(axis='x', rotation=45)

# Boxplot for poem_analysi_Custom.csv
axes[1].boxplot(dataC.values, labels=dataC.columns, patch_artist=True, 
                boxprops=dict(facecolor="orange", color="black"),
                medianprops=dict(color="red"),
                whiskerprops=dict(color="green"),
                capprops=dict(color="blue"))
axes[1].set_title("Box Plot of Features in poem_analysi_Custom.csv")
axes[1].set_xlabel("Features")
axes[1].tick_params(axis='x', rotation=45)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
