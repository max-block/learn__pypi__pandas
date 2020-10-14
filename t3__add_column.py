import pandas as pd

df = pd.read_csv("data/adult.csv")
# add married column (y/n) which is based on marital.status. If stars with Married, y. Otherwise - n.
df["married"] = df.apply(lambda row: row["marital.status"].startswith("Married"), axis=1)

print(df[["married", "marital.status"]].head(30))
