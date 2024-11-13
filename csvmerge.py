import pandas as pd
import glob

# Define the path to the CSV files and load all CSV filenames
csv_files = glob.glob("formantData/*.csv")

# List to hold each DataFrame
dataframes = []

for file in csv_files:
    # Read each CSV file
    df = pd.read_csv(file)
    # Add a new column with the filename (without the path and extension)
    df["filename"] = file.split("/")[-1].replace(".csv", "")
    # Append the DataFrame to the list
    dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Reorder columns to place 'filename' as the first column
merged_df = merged_df[
    ["filename"] + [col for col in merged_df.columns if col != "filename"]
]

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("merged_file.csv", index=False)
