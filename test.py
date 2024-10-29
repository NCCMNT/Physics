import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [[50, 30], [40, 25], [30, 10]]
df = pd.DataFrame(data)
print(df.iloc[::-1].reset_index(drop=True))

xs, ys = df.shape
print(xs,ys)

x = np.arange(xs)
y = np.arange(ys)
X, Y = np.meshgrid(x,y)

plt.figure(figsize = (20,10))