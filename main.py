import pandas as pd
nba = pd.read_csv("classes.csv")
type(nba)
print(len(nba))
print(nba.shape)
print(nba.head())
pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)
print(nba.tail())
print(nba.info())
print(nba.describe())
print(nba["Class"].value_counts())