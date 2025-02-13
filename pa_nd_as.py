import pandas as pd  

# Sample data  
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 40, 45],
    "income": [50000, 60000, 75000, 80000, 65000],
    "gender": ["Female", "Male", "Male", "Male", "Female"]
}  

df = pd.DataFrame(data)  

# Basic operations  
avg_income = df["income"].mean()  
median_income = df["income"].median()  
income_std = df["income"].std()  
total_income = df["income"].sum()  
max_age = df["age"].max()  
min_age = df["age"].min()  

# Counting unique values  
unique_genders = df["gender"].nunique()  
gender_count = df["gender"].value_counts()  

# Filtering and sorting  
high_income = df[df["income"] > 60000]  
sorted_df = df.sort_values(by="age", ascending=False)  

# Selecting specific columns  
selected_columns = df[["name", "income"]]  

# Data transformation  
df["tax"] = df["income"] * 0.1  
df["age_group"] = df["age"].apply(lambda x: "Young" if x < 35 else "Old")  

# Grouping and aggregation  
avg_income_by_gender = df.groupby("gender")["income"].mean()  
age_group_count = df["age_group"].value_counts()  

# Handling missing values  
df["income"].fillna(df["income"].mean(), inplace=True)  
df.dropna(inplace=True)  

# Print results  
print("Average Income:", avg_income)  
print("Median Income:", median_income)  
print("Income Standard Deviation:", income_std)  
print("Total Income:", total_income)  
print("Max Age:", max_age, "| Min Age:", min_age)  
print("\nGender Count:\n", gender_count)  
print("\nSorted DataFrame:\n", sorted_df)  
print("\nAverage Income by Gender:\n", avg_income_by_gender)  
print("\nAge Group Count:\n", age_group_count)  
