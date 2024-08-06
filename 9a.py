import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/ramu/python/plab/iris (1).csv")
df.plot()
plt.show()
df.plot.scatter(x="sepal.length",y="sepal.width",c='red')
plt.show()
df.plot.scatter(x="sepal.length",y="sepal.width",c="petal.length",colormap='viridis')
plt.show()
df["sepal.length"].hist()
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

