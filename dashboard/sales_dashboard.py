import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sales_data.csv")

print("Total Sales:", df["Sales"].sum())

region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)

region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Revenue")
plt.show()

product_sales = df.groupby("Product")["Sales"].sum()

product_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Product Contribution")
plt.show()