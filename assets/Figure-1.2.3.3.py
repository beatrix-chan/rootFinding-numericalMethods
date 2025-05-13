import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2 * (x**2) + 7 * x - 4

x0, x1 = 0.25, 1.75

x = np.linspace(-6, 6, 400)
y = f(x)

plt.plot(x, y, c='#cac486', label='$f(x) = 2x^2 + 7x - 4$', zorder=1)
plt.axhline(0, c='#807b81', zorder=0)
plt.axvline(0, c='#807b81', zorder=0)
plt.scatter([x0, x1], [f(x0), f(x1)], marker='*', c='#4b6e74', s=50, label='initial guesses', zorder=3)

m = (f(x1) - f(x0)) / (x1 - x0)
b = f(x0) - m * x0

x_val = -b / m

plt.scatter(x_val, f(x_val), marker='*', c='#ae6168', s=50, label='new approximation', zorder=3)
plt.scatter([x1, x_val], [f(x1), f(x_val)], marker='o', s=130, fc='none', ec='r', label='next approximations', zorder=4)

plt.xlim(0, 2)
plt.ylim(-5, 20)
plt.grid(True, c='grey', alpha=0.5)

plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()

plt.show()