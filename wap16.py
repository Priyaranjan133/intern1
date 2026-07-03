import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y1 = x**2
y2 = x**3

plt.plot(x, y1, label="y = x²")
plt.plot(x, y2, label="y = x³")

plt.title("Quadratic and Cubic Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.show()