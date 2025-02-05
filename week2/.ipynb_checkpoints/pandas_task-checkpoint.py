import pandas as pd

print("....................................................................................")
# 1. Read the dataset into a pandas DataFrame and display the first 5 rows
print("Answer1:")

df = pd.read_csv('python-lab/week2/CarPrice_project.csv')
print("First 5 rows of the DataFrame:")
print(df.head())


print("....................................................................................")
# 2. Slice the DataFrame to create a new DataFrame containing only the columns CarName, fueltype,
#carbody, and price. Display the first 10 rows of the new DataFrame.
print("Answer2:")

selected_columns = ['CarName', 'fueltype', 'carbody', 'price']
df_selected = df[selected_columns]
print("\nFirst 10 rows of the selected DataFrame:")
print(df_selected.head(10))


print("....................................................................................")# 3. Filter the DataFrame to include only cars with fueltype as 'gas'. Display the first 20 rows of the
# filtered DataFrame.
print("Answer3:")

df_gas = df[df['fueltype'] == 'gas']
print("\nFirst 20 rows of cars with fueltype as gas:")
print(df_gas.head(20))


print("....................................................................................")
# 4. Slice the DataFrame to include only cars with carlength greater than 180 and fueltype as 'diesel'.
# Display the first 5 rows of the sliced DataFrame.
print("Answer4:")

df_diesel_large = df[(df['carlength'] > 180) & (df['fueltype'] == 'diesel')]
print("\nFirst 5 rows of cars with carlength > 180 and fueltype as diesel:")
print(df_diesel_large.head())

print("....................................................................................")
# 5.Count the number of cars for each fueltype. Display the result.
print("Answer5:")

fueltype_counts = df['fueltype'].value_counts()
print("\nNumber of cars for each fueltype:")
print(fueltype_counts)


print("....................................................................................")
# 6. Create a new column car_type which represents the size of the car based on the carlength.
# Hint: Use the .apply() method.
# ○​ If carlength is below 150, consider it as short_length_cars.
# ○​ If it is between 150 to 170, consider it as mid_length_cars.
# ○​ If it is greater than 170, consider it as long_length_cars.
# Apply this function to the DataFrame to create the column car_type. Display the count of
# each car_type.
print("Answer6:")
def classify_car_length(length):
    if length < 150:
        return 'short_length_cars'
    elif 150 <= length <= 170:
        return 'mid_length_cars'
    else:
        return 'long_length_cars'

df['car_type'] = df['carlength'].apply(classify_car_length)
print(df['car_type'].value_counts())
print("....................................................................................")

# 7. Remove the column symboling from the DataFrame as an inplace operation. Display the first 5
# rows of the DataFrame after removal.
print("Answer7:")
df.drop(columns=['symboling'], inplace=True)
print(df.head())



print("....................................................................................")
# 8. Group by carbody and calculate the mean price for each group.

print("Answer8:")
mean_price_by_carbody = df.groupby('carbody')['price'].mean()
print(mean_price_by_carbody)


print("....................................................................................")
# 9. Create a series of 4 capital cities where the index is the name of corresponding country.

print("Answer9:")
capitals = pd.Series({"India": "New Delhi", "USA": "Washington D.C.", "France": "Paris", "Japan": "Tokyo"})
print(capitals)


print("....................................................................................")
# 10. Create a dataframe of (at least 4) countries, with 2 variables: population and capital. Country
# name should be the index.

print("Answer10:")
data = {"Country": ["India", "USA", "France", "Japan"],
        "Population": [1393409038, 331002651, 65273511, 126476461],
        "Capital": ["New Delhi", "Washington D.C.", "Paris", "Tokyo"]}
countries_df = pd.DataFrame(data).set_index("Country")
print(countries_df)
print("....................................................................................")