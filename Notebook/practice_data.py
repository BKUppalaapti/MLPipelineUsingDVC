import pandas as pd

# Sample data
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Scores': [10, 20, 30, 40, 50, 60, 65, 75, 85, 95]
}

df = pd.DataFrame(data)

print(df)