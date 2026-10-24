
import pandas as pd

# Load the sales dataset
file_path = "data/Online Retail.xlsx"
df = pd.read_excel(file_path)

# Display the first five records
print("FIRST FIVE RECORDS")
print(df.head())

# Display the number of rows and columns
print("\nDATASET SHAPE")
print(df.shape)

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check duplicate records
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())
