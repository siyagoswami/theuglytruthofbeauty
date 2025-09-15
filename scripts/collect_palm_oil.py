import os 
import requests
import pandas as pd 

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

file_path = "data/FAOSTAT_data_en_8-20-2025.csv"
df = pd.read_csv(file_path)

print("verified palm oil production data")
print(df.head())
print(df.columns)