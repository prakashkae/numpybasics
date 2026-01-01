import pandas as pd


df = pd.read_csv(r"C:\Users\Prakash\Desktop\Python learn\panda_learn\data.csv",index_col="Name")

# df = df.fillna({"Type2": "None" })
# print(df.to_string())

# df["Type1"] = df["Type1"].replace("Fire", "Flame")
# print(df.to_string())

df["Legendary"] = df["Legendary"].astype(bool)
print(df.to_string())
