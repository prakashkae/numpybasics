import pandas as pd

data = {
    "Name": ["John", "Anna", "James", "Linda"],
    "Age": [28, 22, 35, 32],
    "City": ["New York", "Paris", "London", "Berlin"]
    
}

df = pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3","Employee 4"])

# add a new column
df["job"] = ["Cook","N/A","Doctor","Engineer"]

#add a new row

New_rows = pd.DataFrame([{"Name":"Prakash","Age":22,"City":"Mumbai","job":"Engineer"},
{"Name":"Shrestha","Age":25,"City":"Mumbai","developer":"Engineer"}],index=["Employee 5","Employee 6"])
df = pd.concat([df,New_rows])
print(df)