import pandas as pd

df = pd.read_csv("../csv/employees.csv")

names1 = [row[1]["first_name"] + " " + row[1]["last_name"] for row in df.iterrows()]
print(names1)
names2 = [name for name in names1 if "e" in name]
print(names2)