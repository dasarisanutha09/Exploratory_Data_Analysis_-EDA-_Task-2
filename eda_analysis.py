# ================================
# CODEALPHA TASK 2
# EXPLORATORY DATA ANALYSIS (EDA)
# ================================


# Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# -------------------------------
# 1. Load Dataset
# -------------------------------


df = pd.read_excel("sales_data.xlsx")


print("\nDataset Loaded Successfully")



# -------------------------------
# 2. Display First Rows
# -------------------------------


print("\nFirst 5 Rows")

print(df.head())



# -------------------------------
# 3. Dataset Information
# -------------------------------


print("\nDataset Information")

print(df.info())



# -------------------------------
# 4. Dataset Size
# -------------------------------


print("\nNumber of Rows and Columns")

print(df.shape)



# -------------------------------
# 5. Check Missing Values
# -------------------------------


print("\nMissing Values")

print(df.isnull().sum())



# -------------------------------
# 6. Statistical Analysis
# -------------------------------


print("\nStatistical Summary")

print(df.describe())



# -------------------------------
# 7. Category Analysis
# -------------------------------


print("\nCategory Count")

print(df["Category"].value_counts())



# -------------------------------
# 8. Sales Distribution Graph
# -------------------------------


plt.figure(figsize=(8,5))

sns.histplot(df["Sales"])

plt.title("Sales Distribution")

plt.xlabel("Sales")

plt.ylabel("Count")

plt.show()



# -------------------------------
# 9. Category Visualization
# -------------------------------


plt.figure(figsize=(8,5))

sns.countplot(
    x="Category",
    data=df
)

plt.title("Category Analysis")

plt.show()



# -------------------------------
# 10. Profit Analysis
# -------------------------------


plt.figure(figsize=(8,5))

sns.boxplot(
    y=df["Profit"]
)

plt.title("Profit Analysis")

plt.show()



# -------------------------------
# 11. Correlation Heatmap
# -------------------------------


plt.figure(figsize=(8,5))


sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)


plt.title("Correlation Analysis")

plt.show()



# -------------------------------
# 12. Save Clean Dataset
# -------------------------------


df.to_excel(
    "clean_sales_data.xlsx",
    index=False
)


print("\nClean Dataset Created Successfully")
