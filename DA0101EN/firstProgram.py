"""
Internet dataset: https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data
"""
import numpy as np
import pandas as pd

csv_path = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(csv_path, header = None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style",
           "drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type",
           "num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ration",
           "horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns=headers
print(df.head(10))
