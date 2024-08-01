import pandas as pd
df = pd.read_csv("GoogleApps.csv")
#df.info()
#print(df.head())
#print(df.head(1))
#print(df.describe())
#print(df["Category"].tail(1))
#print(df.tail())
#print(df['Size'].mean())[]
#print(df['Installs'].median())
#print(df["Installs"].mean(0))
#print(df["Installs"].mean(), df["Installs"].median())
print(df[df["Category"]=="ART_AND_DESIGN"]['Installs'].median())
