# Code Explanation

<details>

<summary>Table of Contents</summary>

1. [Implementations](#1-implementations)
2. [Trace Tables](#2-trace-tables)
3. [Comparison Table](#3-comparison-table)
4. [Plots of Convergence](#4-plots-of-convergence)

</details>

> ![NOTE]
> Here is a quick recap of what was mentioned in [theories.md](theories.md)
> 
> | Methods | Approximation Algorithm | Iteration formula |
> | :-----: | :---------------------- | :---------------: |
> | Bisection Method | Halves an interval over and over again | $$c = \frac{a + b}{2}$$ |
> | Newton-Raphson Method | Uses the tangent line to refine approximation | $$x_{n + 1} = x_{n} - \frac{f(x_{n})}{f'(x_{n})}$$ |
> | Secant Method | Uses secant line to refine approximation | $$x_{n + 1} = x_{n} - f(x_{n}) \times \frac{x_{n} - x_{n - 1}}{f(x_{n}) - f(x_{n - 1})}$$

> [!IMPORTANT]
> **ALWAYS** remember to add necessary libraries before starting to run your codes. Jupyter is very smart for storing variables but it will become a pain if bugs are in between.
> ```python
> import time # CPU times
> import numpy as np # Errors and Analysis
> import pandas as pd
> import matplotlib.pyplot as plt
> ```

---

## 1. Implementations

In this section, we will look at how to implement these three numerical methods. These are under the comment `# STANDARD --- Method Implementation` (replaced `---` with the methods' names).

> [!TIP]
> You can add those python sheets and implement in your experiment environment the same way you do with python functions (e.g. `time`, `numpy`, `pandas`, etc.), but you need to identify the source, then the function (just like importing the `Decimal` library.)
> ```python
> from bisection_method import bisection
> from newton_raphson_method import newton_raphson
> from secant_method import secant

### 1.1 Parameters
> [!TIP]
> At the beginning of every functions, there are a multi-line strings within a pair of triple quotes. They are called "docstrings" under [PEP 257](https://peps.python.org/pep-0257/#multi-line-docstrings). If you use Visual Studio Code (no matter the classic or developer version), you can hover your cursor above a function's name and see a small container underneath your cursor. The content of that container is the docstring! It's equivalent to using `<function>?` in Jupyter Notebook and `print(<function>.__doc__)` in python.

All methods also requires the input of `func`, which is the function you want to find the root for. An actual function in python must have the `return` keyword within it because that's an exit "command" and send a value back to the caller. Therefore, you cannot just put $f(x)$'s equation as an argument of a function. The line below shoulds the incorrect method:

```python
root, approximation = bisection(2 * x**2 + 7 * x - 4, -1, 1)
```

Instead, you should have a seperately define what your function is. Like this:

```python
def f(x):
    return 2 * x**2 + 7 * x - 4

root, approximation = bisection(f, -1, 1)
```
> [!CAUTION]
> Remember `return`!
>
> [!WARNING]
> And it's `f` not `f(x)`

Other than `func`, the three of them also have common parameters `tol` and `max_iter`. The docstring sort of explain it already but just to expand on that slightly, their purpose is similar to machine epsilon ($\epsilon$) from Formative Assessment 1. `max_iter` is used in the for loop outside the methods' iteration formula, which means the maximum number of times this formula can be used is 100 times not caring if convergent ever happened.

#### 1.1.1 Bisection Method

The two remaining parameters required you to input are `a` and `b`. As explained in the docstrings, they are the left and right endpoints of the initial interval respectively.

---

## 2. Trace Tables


---

## 3. Comparison Table


---

## 4. Plots of Convergence