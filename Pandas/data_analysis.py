import pandas as pd

df = pd.read_csv("C:\\Mervin\\Analytics\\IBMDE\\exercise03_car_sales_data.csv")

print(df.head())

print("\n\n")

# Get the maximum of price

print(df['price'].max())