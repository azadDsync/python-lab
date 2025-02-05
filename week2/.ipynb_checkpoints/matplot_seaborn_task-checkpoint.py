import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("python-lab/week2/CarPrice_project.csv")

# # 1. Plot y=sin⁡(x) and y=cos⁡(x) on the same graph for x in [0,2π].
# x = np.linspace(0, 2 * np.pi, 100)
# plt.plot(x, np.sin(x), label='sin(x)')
# plt.plot(x, np.cos(x), label='cos(x)')
# plt.legend()
# plt.title("Sine and Cosine Functions")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

# # 2. Create a heatmap to show the correlation matrix of numerical columns in the CarPrice_project.csv dataset.
# numerical_df = df.select_dtypes(include=[np.number])  # Select only numerical columns
# plt.figure(figsize=(10, 6))
# sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title("Correlation Heatmap")
# plt.show()


# # 3. Create a combination plot:
# # ● Use a bar plot to show the average price for each carbody.
# # ● Overlay a line plot to show the count of cars for each carbody.
# avg_price = df.groupby('carbody')['price'].mean()
# car_counts = df['carbody'].value_counts()

# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# ax1.bar(avg_price.index, avg_price, color='b', alpha=0.6, label='Avg Price')
# ax2.plot(car_counts.index, car_counts, color='r', marker='o', label='Car Count')
# ax1.set_xlabel("Car Body")
# ax1.set_ylabel("Average Price", color='b')
# ax2.set_ylabel("Car Count", color='r')
# plt.title("Average Price & Car Count by Car Body")
# plt.show()

# # 4. Visualize the relationship between horsepower, enginesize, and price.
# sns.scatterplot(data=df, x='horsepower', y='price', hue='enginesize', palette='viridis')
# plt.title("Horsepower vs Price (Hue: Engine Size)")
# plt.show()

# 5. Which column has the highest variance? Why might this be?
numeric_columns = df.select_dtypes(include=[np.number])
variance = numeric_columns.var().idxmax()
print(f"Column with highest variance: {variance}")

# 6. What insights can you draw by comparing the max and min values of the columns?
summary = df.describe().loc[['min', 'max']]
print(summary)

# 7. How does the variance of price compare to that of enginesize and horsepower?
variance_comparison = df[['price', 'enginesize', 'horsepower']].var()
print(variance_comparison)

# 8. Create a bar plot showing the maximum and minimum values for each numerical column in the dataset.
summary.T[['min', 'max']].plot(kind='bar', figsize=(12,6))
plt.title("Max & Min Values for Each Numerical Column")
plt.show()

# 9. Create a pie chart showing the proportion of each carbody and drivewheel type.
# ● Which carbody type dominates the dataset?
# ● Which drivewheel type is the least common?
fig, ax = plt.subplots(1, 2, figsize=(12,6))
df['carbody'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax[0], title='Car Body Distribution')
df['drivewheel'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax[1], title='Drive Wheel Distribution')
plt.show()

# Insights
print("Car body type that dominates the dataset:", df['carbody'].value_counts().idxmax())
print("Least common drivewheel type:", df['drivewheel'].value_counts().idxmin())
