import pandas as pd
import matplotlib.pyplot as plt

file_path = 'sales_data.csv'
sales_data = pd.read_csv(file_path)

print(sales_data)

print(sales_data.isnull().sum())
print(sales_data.describe())
print(sales_data['Product'].unique())
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data['Month'] = sales_data['Date'].dt.month
sales_data['Year'] = sales_data['Date'].dt.year
sales_data['TotalSales'] = sales_data['Quantity'] * sales_data['Revenue']
monthly_sales = sales_data.groupby(['Year', 'Month'])['TotalSales'].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales per Month')
plt.xlabel('Year-Month')
plt.ylabel('Total Sales ($)')
plt.show()
