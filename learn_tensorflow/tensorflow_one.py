import numpy as np
import tensorflow  as tf
import matplotlib.pyplot as plt


x = np.linspace(1,10)
y = np.cos(x)

plt.figure(1,(10,8),120)
plt.plot(x,y)
plt.show()