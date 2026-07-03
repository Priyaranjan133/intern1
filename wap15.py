import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)

plt.title("Graph of y = x²")
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)
plt.show()