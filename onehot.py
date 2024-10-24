import pandas as pd
data = {
    "names":["Ravisha","Aadya","Shambhavi","Archita"],
    "Favourite color": ["Red", "Red", "Yellow", "Blue"]
}
df = pd.DataFrame(data)
print(pd.get_dummies(df,columns=["Favourite color"]))
