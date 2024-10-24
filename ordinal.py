import pandas as pd
data = {
    "Games":["Cricket","Football","Kho-Kho","Rugby"],
    "popularity": ["High", "High", "Low", "Medium"]
}
df = pd.DataFrame(data)
mapping = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}
df1=df.copy()
df1["popularity"] = df1["popularity"].replace(mapping)
print(df1)
