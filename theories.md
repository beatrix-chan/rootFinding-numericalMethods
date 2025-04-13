# Theories

> [!NOTE]
>
> Rongsen put these thories together as one of the support materials for our lab session on Week 5's Friday. The summary is awesome but here's just a shorter and more focused version.

<details>

<summary>Table of Contents</summary>

1. [Basics of Root-Finding](#1-basics-of-root-finding)
3. [Analytical Methods VS Numerical Methods](#2-analytical-methods-vs-numerical-methods)
4. [Numerical Methods](#3-numerical-methods)

</details>

## 1. Basics of Root-Finding

### 1.1 Definition of Roots
The $x$-intercepts, where the graph intersect with the $x$-axis. In a mathematically way, it's written as $f\left (x\right ) = 0$.

### 1.2 Solving Algebratically
Let's take $f\left (x\right ) = 2x^{2} + 7x - 4$ as an example:

> $f\left (x\right ) = 2x^{2} + 7x - 4$
>
> $\because f\left (x\right ) = 0$<br />
> $\therefore 2x^{2} + 7x - 4 = 0$
>
> $0 = 2x^{2} + 8x - x - 4$<br />
> $0 = \left (2x^{2} + 8x\right ) - \left (x + 4\right )$<br />
> $0 = 2x\left (x + 4\right ) - \left (x + 4\right )$<br />
> $0 = \left (2x - 1\right )\left (x + 4\right )$
>
> Solve for $x$:
> | $0 = 2x - 1$ | $0 = x + 4$ |
> | :----------- | :---------- |
> | $x = \frac{1}{2}$ | $x = -4$ |
>
> $\therefore$ The roots for $f\left (x\right ) = 2x^{2} + 7x - 4$ are $x = -4$ and $x = \frac{1}{2}$.

### 1.3 Solving Graphically
<details>

<summary>Code Snippet</summary>

```python
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2 * (x**2) + 7 * x - 4

x = np.linspace(-6, 6, 1000)
y = f(x)

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
```

</details>
<img src="assets/Figure-1.3.1.svg" alt="Figure 1.3.1: Example of Solving Graphically" />
<p align="center"><i><b>Figure 1.3.1</b>: Example of Solving Graphically</i></p>

***

## 2. Analytical Methods VS Numerical Methods

### 2.1 Analytical Methods
Analytical Methods aims for exact solutions. It's commonly solved using mathematical formulas and theorems.

| :white_check_mark: Advantages | :x: Disadvantages |
| :---------------------------- | :---------------- |
| **Exact Solution**<br />Provide precise solutions without approximation errors. | **Complexity Constraints**<br />For higher-degree or nonlinear equations, finding closed-form solutions may be impossible |
| **General Insights**<br />Offer expressions that can be analysed to understand the overall behaviours of functions | **Limited Applicability**<br /> Suitable only for certain types of equations; complex equations may resist analytical solutions. |

- **Example of formulas/theorems**
  - The quardratic formula<br />$x = \frac{-b \pm \sqrt{b^{2} - 4ac}}{2a}$
- **Application**
  - Math exam :upside_down_face:

### 2.2 Numerical Methods
Numerical Methods use iterative algorithms to approximate solutions. Usually used computationally and are applicable to complex equations.

| :white_check_mark: Advantages | :x: Disadvantages |
| :---------------------------- | :---------------- |
| **Broad Applicability**<br />Effective for solving a wide range of complex or high-degree equations | **Precision**<br />Results are approximated, accuracy depends on the algorithm's properties and computational resources |
| **Flexibility**<br />Suitable for nonlinear equations and systems | **Convergence Issues**<br />Some methods may converge slowly or fail to converge, influenced by initial guesses and function characteristics |

- **Application**
  - Live-tracking of parsels and airplanes

### 2.3 Comparing Approaches
When choosing between analytical and numerical methods, consider the following factors:

| Factor | Analytical Method | Numerical Method |
| :----: | :---------------- | :--------------- |
| **Equation Complexity** | Simple Equations (Degree less than 5) | Complex Equations (High-degree equations) |
| **Desired Precision** | Exact solutions | Approximations |

- **Computational Resources**: Numerical methods may demand significant computation, especially for high-precision and requirements or intricate equations.
- **Function Characteristics**: Continuity, differentiability, and initial estimates influence the convergence and efficiency of numerical methods.

***

## 3. Numerical Methods
> [!IMPORTANT]
> We will discuss the theories of these Numerical Methods here, but I will explain step-by-step how these Methods operate in [code-explanation.md](code-explanation.md)

1. **Bisection Method**<br />Iteratively halves an interval to converge on a root. Simple and guaranteed to converge, but relatively slow.
2. **Newton's Method**<br />Utilises function derivatives to rapidly converge to a root. Offers quadratic convergence near the root but requires derivative computation and may diverge if the initial guess is not close enough.
3. **Secant Method**<br />Similar to Newton's method but approximates the derivative using two initial points. Avoids direct derivative computation but may have slower convergence.

## 3.1 Bisection Method
The Bisection Method is a straightforward and reliable technique that narrows down the interval containing a root by repeatedly halving it. It requires the function changes sign over the interval, indicating the presence of a root due to the Intermediate Value Theorem.

## Bisection Method Algorithm

> [!WARNING]
> Only the midpoints are your approximations! $a$ and $b$ aren't!!!

**To start**
- *Initial Interval* (variable): $\left [a,b\right ]$, such that $f(a)$ and $f(b)$ have opposite signs.
  - $a$ is the left endpoint of the interval
  - $b$ is the right endpoint of the interval

**Iteration**
- Compute for the midpoint ($c$)<br />$c = \frac{a + b}{2}$
- Evaluate $f(c)$
- Update interval:
  - $\because f\left (a\right ) \times f\left (c\right ) < 0$<br />$\therefore$ New interval: $\left [a,c\right ]$
  - $\because f\left (a\right ) \times f\left (c\right ) > 0$<br />$\therefore$ New interval: $\left [c,b\right ]$
- Repeat until $\left |\frac{b - a}{2}\right |$ is less than tolerance level.

### Evaluating the Bisection Method

| :white_check_mark: Advantages | :x: Disadvantage |
| :---------------------------- | :--------------- |
| Guranteed convergence if the initial interval is valid | Linear convergence rate, which can be slow |
| Simple implementation | Requires the function to change sign over the interval |

## 3.2 Newton-Raphson Method
The Newton-Raphson Method uses tangents to approximate the root of a function. Starting from an initial guess, it iteratively refines the estimate using the function's derivative.

### Newton-Raphson Method Algorithm

**To start**
- *Initial Guess* (variable): Your first approximation $x_{0}$
- *Derivative of function* (function): The derivative of your function. Substituting $x$ here will get the slope of the tangent line for $x$.

**Iteration**
- Substitute $x_{0}$ to $x_{n}$ (current x) in the formula below. $x_{n + 1}$ is your next approximation.<br />$x_{n + 1} = x_{n} - \frac{f(x_{n})}{f'(x_{n})}$
- Update approximation:<br />$x_{n + 1} \to x_{n}$
- Repeat until $\left | x_{n + 1} - x_{n} \right |$ is less than tolerance level.

### Evaluating the Newton-Raphson Method

| :white_check_mark: Advantages | :x: Disadvantage |
| :---------------------------- | :--------------- |
| Quadratic convergence near the root, leading to rapid results | Requires computation of the derivative $f'$ |
|  | Convergence is not guranteed. Depends on initial guess and the function's behaviour |

## 3.3 Secant Method
The Secant Method approximates the root by using a sequence of secant lines through pairs of points on the function. It does not require the computation of derivatives.

### Secant Method Algorithm

**To start**
- *Initial Guesses* (variables): Two initial approximations
  - $x_{1}$ (in the formula, it will become $x_{n}$) is your current approximation
  - $x_{0}$ (in the formula, it will become $x_{n - 1}$) is your previous approximation
 
**Iteration**
- Substitute your variables into the formula below to compute for the next approximation:<br />$x_{n + 1} = x_{n} - f(x_{n}) \times \frac{x_{n} - x_{n - 1}}{f(x_{n}) - f(x_{n - 1})}$
- Update approximations:<br />$x_{n} \to x_{n - 1}$<br />$x_{n + 1} \to x_{n}$
- Repeat until $\left | x_{n + 1} - x_{n} \right |$ is less than tolerance level
