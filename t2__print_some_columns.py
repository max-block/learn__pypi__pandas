import pandas as pd

df = pd.read_csv("data/adult.csv")

print(df[["age", "sex"]].head())
#    age     sex
# 0   90  Female
# 1   82  Female
# 2   66  Female
# 3   54  Female
# 4   41  Female
