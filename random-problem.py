import pandas as pd
import random

difficulty = "Easy"  # Options: "Easy", "Medium", "Hard", "All"

data = pd.read_csv("leetcode_top150.csv")
if difficulty != "All":
    data = data[data['difficulty'] == difficulty.upper()]

random_int = random.randint(0, len(data)-1)
print(data.iloc[random_int])