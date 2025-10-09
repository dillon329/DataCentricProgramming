import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 32, 18, 47],
    "city": ["NYC", "LA", "NYC", "Chicago"]
}

df = pd.DataFrame(data)
print(df)

condition = df["age"]>30

print(condition)

print(len(df[condition]))
    