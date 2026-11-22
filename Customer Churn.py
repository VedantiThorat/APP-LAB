# Customer Churn - Exploratory Data Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("customer_churn.csv")

# Display Dataset
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Values
print("\nDuplicate Values:", df.duplicated().sum())

# Remove Duplicate Values
df = df.drop_duplicates()

# Handle Missing Values
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# Check Churn Distribution
print("\nChurn Distribution:")
print(df['Churn'].value_counts())

# Churn Visualization
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Distribution")
plt.show()

# Correlation Heatmap
numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Analyze Monthly Charges
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

# Analyze Customer Tenure
sns.histplot(data=df, x='tenure', hue='Churn', kde=True)
plt.title("Customer Tenure vs Churn")
plt.show()

# Final Cleaned Dataset
print("\nCleaned Dataset:")
print(df.head())

# Save Cleaned Dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nData Cleaning Completed Successfully!")