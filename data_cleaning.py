# -----------------------------------------------
# Netflix Movies and TV Shows - Data Cleaning Project
# by Prajwal Sandip Shelar
# -----------------------------------------------

import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("netflix_titles.csv")
print("✅ Dataset loaded successfully!")
print("Initial shape:", df.shape)
print("-" * 50)

# Step 2: Check for missing values
print("Missing values before cleaning:")
print(df.isnull().sum())
print("-" * 50)

# Step 3: Handle missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Not Available', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)

# Step 4: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 5: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 6: Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Step 7: Verify data types
print("Data types after cleaning:")
print(df.dtypes)
print("-" * 50)

# Step 8: Check for duplicates and nulls again
print("Duplicates remaining:", df.duplicated().sum())
print("Missing values after cleaning:")
print(df.isnull().sum())
print("-" * 50)

# Step 9: Save the cleaned dataset
df.to_csv("netflix_titles_cleaned.csv", index=False)
print("✅ Cleaned dataset saved successfully as 'netflix_titles_cleaned.csv'")
print("Final shape:", df.shape)
