import pandas as pd

calories = {"day 1": 1750, "day 2": 2000, "day 3": 2250, "day 4": 2500, "day 5": 2750}
series = pd.Series(calories)
series.loc["day 2"] += 2000
print(series[series <= 2000])
