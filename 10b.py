import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/ramu/python/plab/iris (1).csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
df.plot()
plt.show()