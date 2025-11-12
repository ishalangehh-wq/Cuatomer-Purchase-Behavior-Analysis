import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 📊 Create Dataset
data = {
    "Customer_ID": [f"C{i}" for i in range(1, 21)],
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Female", "Female", "Male", "Male",
               "Female", "Male", "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Female"],
    "Age_Group": ["18-25", "26-35", "36-45", "18-25", "26-35", "36-45", "26-35", "46-55", "36-45", "18-25",
                  "26-35", "46-55", "36-45", "26-35", "18-25", "46-55", "26-35", "36-45", "46-55", "26-35"],
    "Product_Category": ["Electronics", "Clothing", "Groceries", "Electronics", "Groceries", "Clothing",
                         "Electronics", "Groceries", "Clothing", "Groceries", "Electronics", "Clothing",
                         "Groceries", "Electronics", "Clothing", "Groceries", "Electronics", "Clothing",
                         "Groceries", "Electronics"],
    "Purchase_Amount": [15000, 12000, 8000, 20000, 9000, 11000, 18000, 7000, 9500, 8500,
                        16000, 10000, 7500, 19000, 10500, 8800, 17500, 9500, 7200, 21000]
}

df = pd.DataFrame(data)

# 🧮 Display first few rows
print(df.head())

# 🎨 1. Gender vs Purchase Amount
sns.barplot(x="Gender", y="Purchase_Amount", data=df, estimator="mean",hue="Gender" ,palette="coolwarm")
plt.title("Average Purchase Amount by Gender")
plt.savefig("gender_purchase.png")
plt.close()

# 🎨 2. Product Category vs Purchase Amount
sns.barplot(x="Product_Category", y="Purchase_Amount", data=df, estimator="mean",hue="Product_Category", palette="viridis")
plt.title("Average Purchase Amount by Product Category")
plt.savefig("category_purchase.png")
plt.close()

# 🎨 3. Age Group vs Purchase Amount
sns.boxplot(x="Age_Group", y="Purchase_Amount", data=df, palette="Set2")
plt.title("Purchase Amount Distribution by Age Group")
plt.savefig("agegroup_purchase.png")
plt.close()

# 🎨 4. Correlation Heatmap
sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.savefig("Correlation_Matrix.png")
plt.show()
