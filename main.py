import pandas as pd

data = {
    "year": [2021, 2022, 2023],
    "GDP rate": [2.8, 3.1, 3.0],
    "GDP": ["1.637M", "1.73M", "1.83M"],
}

df = pd.DataFrame(data)
print(df)
