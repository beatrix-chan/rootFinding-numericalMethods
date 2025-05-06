import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2 * (x**2) + 7 * x - 4

def df(x):
    return 4 * x + 7

x0 = 1

m = df(x0)
b = f(x0) - m * x0

x = np.linspace(-6, 6, 400)
y = f(x)
tangent = m * x + b

plt.plot(x, y, c='#cac486', label='$f(x) = 2x^2 + 7x - 4$', zorder=1)
plt.axvline(0, c='#807b81', zorder=0)
plt.axhline(0, c='#807b81', zorder=0)
plt.plot(x, tangent, c='#72969d', label=f'Tangent line at $x = {x0}$', zorder=2)
# plt.scatter(x0, f(x0), marker='*', c='#4b6e74', s=50, label='initial guess', zorder=3)

x_val = - b / m
plt.scatter(x_val, 0, marker='*', c='#db8a90', s=80, label='Tangent = 0', zorder=3)
plt.scatter(x_val, f(x_val), marker='*', c='#ae6168', s=80, label='Next approximation', zorder=4)
plt.plot([x_val, x_val], [0, f(x_val)], c='#ecb8bb', ls='--', label='approximating', zorder=3)

plt.xlim(0.48, 0.62)
plt.ylim(-0.2, 0.8)
plt.grid(True, c='grey', alpha=0.5)

plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()

plt.show()