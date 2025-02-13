import pandas as pd

a = pd.read_csv("cars.csv", header=None)  # No header row
a = pd.read_csv("cars.csv")  
a = pd.read_csv("cars.csv",nrows=10)  # Read only the first 10 rows
a = pd.read_csv("cars.csv", usecols=["CarName"])  # Read only selected columns ["column name"]
a = pd.read_csv("cars.csv", na_values=["?", "NA", "NULL"])  # Treat ?, NA, NULL as NaN
a = pd.read_csv("output.csv")
cars_dict = a.to_dict()
df = pd.read_csv("data.csv", skiprows=5)  # Skip first 5 rows
a = pd.read_csv("cars.csv")
a.info() # Display information about the DataFrame  
print(a)  # This will print the DataFrame

# Read csv from url
url = "https://example.com/data.csv"
a = pd.read_csv(url)

chunk_size = 5  # Define the number of rows in each chunk
for chunk in pd.read_csv("cars.csv", chunksize=chunk_size):
    print(chunk.head())  # Process each chunk separately

total_rows = 0
for chunk in pd.read_csv("cars.csv", chunksize=5):
    total_rows += len(chunk)  # Count rows in each chunk
print("Total rows:", total_rows)



