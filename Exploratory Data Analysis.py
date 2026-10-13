
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("customer_churn.csv")

# Step 2: Display the first five rows
print("First five rows:")
print(df.head())

# Step 3: Display dataset information
print("\nDataset Information:")
df.info()

# Step 4: Check dataset shape
print("\nDataset Shape:")
print(df.shape)

# Step 5: Check column names
print("\nColumn Names:")
print(df.columns)

# Step 6: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 7: Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Step 8: Display statistical summary
print("\nStatistical Summary:")
print(df.describe(include="all"))

# Step 9: Clean the data
# Remove duplicate rows
df = df.drop_duplicates()

# Replace blank strings with NaN
df = df.replace(r"^\s*$", np.nan, regex=True)

# Convert TotalCharges to numeric if this column exists
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"], errors="coerce"
    )

# Fill missing numeric values with the median
numeric_cols = df.select_dtypes(include=np.number).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with the mode
categorical_cols = df.select_dtypes(include=["object", "category"]).columns
for col in categorical_cols:
    if df[col].isnull().any() and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Step 10: Analyze customer churn
if "Churn" in df.columns:
    print("\nChurn Distribution:")
    print(df["Churn"].value_counts())

    # Plot churn distribution
    sns.countplot(data=df, x="Churn")
    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.show()

    # Calculate churn percentages
    print("\nChurn Percentage:")
    print(df["Churn"].value_counts(normalize=True) * 100)

# Step 11: Analyze numerical features
numeric_cols = df.select_dtypes(include=np.number).columns

if len(numeric_cols) > 0:
    df[numeric_cols].hist(figsize=(12, 8), bins=20)
    plt.suptitle("Distribution of Numerical Features")
    plt.tight_layout()
    plt.show()

# Step 12: Correlation analysis
if len(numeric_cols) > 1:
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

# Step 13: Analyze churn by contract type
if "Churn" in df.columns and "Contract" in df.columns:
    sns.countplot(data=df, x="Contract", hue="Churn")
    plt.title("Churn by Contract Type")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

# Step 14: Save the cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("\nFinal Dataset Shape:", df.shape)
print("\nEDA and Data Cleaning Completed.")

