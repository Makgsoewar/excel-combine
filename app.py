import os
import pandas as pd

# Specify the directory path
directory = "input"

# Get the list of files in the directory
file_list = os.listdir(directory)

# Sort the file_list array in ascending order
file_list = sorted(file_list)

# Create an empty list to store the DataFrames
dfs = []

# Iterate over the file list
for file_name in file_list:
    # Check if the file is in Excel format
    if file_name.endswith(".xlsx"):
        # Construct the full file path
        file_path = os.path.join(directory, file_name)

        # Read the Excel file into a DataFrame
        data = pd.read_excel(file_path)

        # Append the DataFrame to the list
        dfs.append(data)

# Concatenate the DataFrames into a single DataFrame
combined_data = pd.concat(dfs, ignore_index=True)

# Write the combined_data DataFrame to a new Excel file
combined_data.to_excel("output/combined_data.xlsx", index=False)
