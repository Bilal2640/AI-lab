import numpy as np
import pandas as pd

csv_file_path = 'sales_data.csv'  # Replace with your CSV file path
loaded_csv_df = pd.read_csv(csv_file_path)

print("Loaded CSV sales_data.csv:")
print(loaded_csv_df.head())

