import pandas as pd
import os

# Take file name from user
file_name = input("Enter CSV/TSV file path: ")

# Detect file type and read accordingly
if file_name.endswith(".tsv"):
    df = pd.read_csv(file_name, sep="\t")
else:
    df = pd.read_csv(file_name)

print("\n===== CSV/TSV FILE INSPECTOR =====")

# 1. Display dimensions
print("\nDataset Dimensions:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Display column names
print("\nColumn Names:")
print(list(df.columns))

# 3. Display data types
print("\nData Types:")
print(df.dtypes)

# 4. Display first few rows
print("\nFirst 5 Rows:")
print(df.head())

# 5. Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# 6. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 7. Filter numerical rows
print("\nAvailable Numerical Columns:")
numeric_columns = df.select_dtypes(include="number").columns
print(list(numeric_columns))

if len(numeric_columns) > 0:
    column = input("\nEnter column to filter: ")

    if column in numeric_columns:
        value = float(input("Enter minimum value: "))

        filtered_df = df[df[column] >= value]

        print("\nFiltered Data:")
        print(filtered_df)

        # 8. Export filtered data
        output_file = "cleaned_data.csv"
        filtered_df.to_csv(output_file, index=False)

        print("\nFiltered data saved successfully!")
        print("Output file:", output_file)

    else:
        print("Invalid numerical column.")

else:
    print("No numerical columns found.")