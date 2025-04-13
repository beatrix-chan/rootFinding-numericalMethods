import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2 * (x**2) + 7 * x - 4

x = np.linspace(-6, 6, 1000)
y = f(x)

plt.figure(figsize=(8, 6))

plt.plot(x, y, c="#cac486", label="$f(x) = 2x^2 + 7x - 4$", zorder=1)
plt.axvline(0, c="#807b81", zorder=0) # y-axis
plt.axhline(0, c="#807b81", zorder=0) # x-axis
plt.scatter([-4, 0.5], [0, 0], c="#4b6e74", marker="x", s=80, label="Roots", zorder=2)

plt.xlim(-5, 2)
plt.ylim(-15, 8)
plt.grid(True, c="grey", alpha=0.5)

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.legend()

plt.show()