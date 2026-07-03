import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)
y = x^2 - 4*x + 4
plt.plot(x, y, label='y = x^2 - 4*x + 4', color='red')
plt.title('graph plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
