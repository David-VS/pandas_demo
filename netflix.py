import pandas as pd
import matplotlib.pyplot as plt



netflix_data = pd.read_csv("data/netflix_titles.csv")

print(netflix_data.dtypes)
print(netflix_data.head(10))
print(netflix_data.groupby("type").count())
print(netflix_data.groupby(["director", "type"]).count())
print(netflix_data.groupby(["release_year", "type"]).count())

netflix_data["release_year"].plot()
plt.show()