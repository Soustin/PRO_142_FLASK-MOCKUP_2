import pandas as pd
import numpy

df = pd.read_csv('articles.csv')

output = df['totalEvents'].head(20).values.tolist()