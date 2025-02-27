import pandas as pd
import numpy as np

# Create a sample DataFrame with mixed data
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, -5, 10, np.nan, 20],
    'C': ['x', 'y', 'x', 'z', ' '],
    'D': [True, False, True, True, False]
})
print("Original DataFrame:\n", df, "\n")

# --- Data Cleaning Methods ---

# Fill NaN with 0
df_filled = df.fillna(0)  # Replaces all NaN with 0
print("Filled NaN with 0:\n", df_filled, "\n")

# Fill NaN with column mean
df_mean = df.fillna(df.mean(numeric_only=True))  # Fills NaN with mean of numeric columns
print("Filled NaN with mean:\n", df_mean, "\n")

# Drop rows with any NaN
df_dropped = df.dropna()  # Removes rows with any NaN
print("Dropped rows with NaN:\n", df_dropped, "\n")

# Check for duplicates in 'C'
duplicates = df.duplicated(subset=['C'])  # Boolean mask for duplicates in 'C'
print("Duplicates in 'C':\n", duplicates, "\n")

# Drop duplicate rows based on 'C'
df_no_duplicates = df.drop_duplicates(subset=['C'])  # Keeps first occurrence of 'C' values
print("Dropped duplicates in 'C':\n", df_no_duplicates, "\n")

# Strip whitespace from 'C'
df['C'] = df['C'].str.strip()  # Removes leading/trailing whitespace in 'C'
print("Whitespace stripped from 'C':\n", df, "\n")

# Replace 'x' with 'X' in 'C'
df['C'] = df['C'].str.replace('x', 'X')  # Replaces 'x' with 'X' in 'C'
print("Replaced 'x' with 'X' in 'C':\n", df, "\n")

# Convert 'A' to integer after filling NaN
df['A'] = df['A'].fillna(0).astype(int)  # Fills NaN in 'A' with 0, then converts to int
print("Converted 'A' to int:\n", df, "\n")

# Clip 'B' between 0 and 15
df['B'] = df['B'].clip(lower=0, upper=15)  # Limits 'B' values to 0-15 range
print("Clipped 'B' between 0 and 15:\n", df, "\n")

# Replace NaN with -1
df_replaced = df.replace(np.nan, -1)  # Replaces all NaN with -1
print("Replaced NaN with -1:\n", df_replaced, "\n")

# Interpolate NaN in 'B'
df_interpolated = df.interpolate()  # Fills NaN in 'B' with linear interpolation
print("Interpolated NaN:\n", df_interpolated, "\n")

# --- Filtering Methods ---

# Filter rows where A > 2
df_query = df.query('A > 2')  # Selects rows where 'A' > 2
print("Rows where A > 2:\n", df_query, "\n")

# Filter rows where 'B' > 5 using loc
df_loc = df.loc[df['B'] > 5]  # Selects rows where 'B' > 5
print("Rows where B > 5 (loc):\n", df_loc, "\n")

# Filter first 3 rows using iloc
df_iloc = df.iloc[:3]  # Selects first 3 rows by position
print("First 3 rows (iloc):\n", df_iloc, "\n")

# Keep values where B > 0, else NaN
df_where = df.where(df['B'] > 0)  # Replaces values with NaN where 'B' <= 0
print("Values where B > 0:\n", df_where, "\n")

# Replace values with -1 where B > 10
df_masked = df.mask(df['B'] > 10, -1)  # Replaces values with -1 where 'B' > 10
print("Values where B > 10 masked with -1:\n", df_masked, "\n")

# Check for NaN values
df_isna = df.isna()  # Boolean mask for NaN values
print("NaN mask:\n", df_isna, "\n")
