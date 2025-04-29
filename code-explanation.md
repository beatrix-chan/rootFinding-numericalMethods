# Code Explanation

<details>

<summary>Table of Contents</summary>

1. [Implementations](#1-implementations)
2. [Trace Tables](#2-trace-tables)
3. [Comparison Table](#3-comparison-table)
4. [Plots of Convergence](#4-plots-of-convergence)

</details>

> [!NOTE]
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
> ```

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

> [!WARNING]
> And it's `f` not `f(x)`

Other than `func`, the three of them also have common parameters `tol` and `max_iter`. The docstring sort of explain it already but just to expand on that slightly, their purpose is similar to machine epsilon ($\epsilon$) from Formative Assessment 1. `max_iter` is used in the for loop outside the methods' iteration formula, which means the maximum number of times this formula can be used is 100 times not caring if convergent ever happened.

#### 1.1.1 Bisection Method

```python
def bisection(func, a, b, tol=1e-5, max_iter=100):
    """
    Perform the Bisection Method to find the root of a given function.

    Parameters:
        func (function): The function for which the root is to be found
        a (float): Left endpoint of the interval
        b (float): Right endpoint of the interval
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iteraions allowed
    """
```

The two remaining parameters required you to input are `a` and `b`. As explained in the docstrings, they are the left and right endpoints of the initial interval respectively.

> [!TIP]
> You have two choices to input `a` and `b` (both ways works):
>
> 1. Initialise variables
> ```python
> # Initialise variables
> a = 1
> b = 2
> 
> #Implement the Bisection Method
> root, midpoints = bisection(f, a, b)
> ```
> 2. Substitute as given input
> ```python
> # Implement the Bisection Method
> root, midpoints = bisection(f, 1, 2)
> ```
>
> I personally recommend *Method 2*, just so you can use `a` and `b` to collect `a_list` and `b_list` later for Trace Table if you decided to implement them in the same notebook. But it's really up to you how you want to do it. You can use literally anything to name your variables as long as it matches the sequence from the `return` line (e.g.: `return c, midpoints` then you must have 2 variables to recieve `c` and `midpoints`.)

#### 1.1.2 Newton-Raphson Method

```python
def newton_raphson(func, dfunc, x0, tol=1e-5, max_iter=100):
    """
    Perform the Newton-Raphson Method to find the root of a given function.

    Parameters:
        func (function): The function for which the root is to be found
        dfunc (function): The derivative of func
        x0 (float): Initial approximation
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
    """
```

`dfunc`:

After you defined `f`, it will be convenient to immediately define `df` as well. Same rule applies, add the keyword `return` before the function.

`x0`:

> [!IMPORTANT]
> In order to make your comparison fair, you should be aiming to approximate the **same** root for all methods. After you choose `a` and `b` (it will be better to not choose an interval that immediately results the exact root because no convergence can be observed, do something like $\pm 0.1$ or $\pm 0.2$), make your initial guess (`x0`) for Newton-Raphson Method the first midpoint (`c`) approximation from the Bisection Method. *Read the Important admonition at Secant Method for its correspondance variables.*

Unlike the Bisection Method where `a` and `b` do not count into the approximation list, `x0` do because in another words, it's your "initial guess". Therefore, the number of iterations and number of approximations are **not equal**.

> [!TIP]
> Same as the Bisection Method, you can initialise the variables in those two ways as well. But adding on to that, I suggest adding a prefix to variables that repeats for different methods because they can be overwritten if called again. Like if you put `root` for all three methods, Newton-Raphson's root will overwrite Bisection's, and Secant's will overwrite Newton-Raphson's. Do something like: `bisection_root`, `newton_root`, `secant_root`, etc.
> But they won't influence each other or crash into each other in their own `.py` files, because they are in seperated files.

#### 1.1.3 Secant Method

```python
def secant(func, x0, x1, tol=1e-5, max_iter=100):
    """Perform the Secant Method to find the root of a given function.

    Parameters:
        func (function): The function for which the root is to be found
        x0 (float): First initial approximation
        x1 (float): Second initial approximation
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
    """
```

The secant method's parameters look difficult (it is complicated if calculated by hand), but in terms of application, it's cheaper than the Newton-Raphson method and converges quicker than the Bisection Method.

`x0`, `x1`:

Although in the docstring `x0` is called the "first initial approximation", accurately speaking, it's actually the "previous approximation". If we look into Secant Method's iteration formula, there are three variables: $x_{n + 1}$, $x_{n}$, and $x_{n - 1}$, and it's corresponding to our variables `x2`, `x1`, `x0`. Therefore, you current approximation should be `x1`.

> [!IMPORTANT]
> We know how that `x1` is our current approximation, but in reality, it's actually impossible to get our "previous approximation". Making `x0`our first midpoint approximation from the Bisection Method neither is correct. So to make life easier. Just make `a` your `x0`, and `b` your `x1`.

### 1.2 Process

In this section, I will explain how each method works line by line.

#### 1.2.1 Bisection Method

```python
def bisection(func, a, b, tol=1e-5, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have opposite signs at the endpoints.")

    midpoints = []

    for _ in range(max_iter):
        c = (a + b) / 2
        midpoints.append(c)

        if func(c) == 0 or abs(b - a) / 2 < tol:
            return c, midpoints
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
    
    raise ValueError("Bisection method did not converge.")
```

The `raise ValueError`s might be new to you but they are not too complicated to understand. The first `raise ValueError` is in the `if` statement that checks if $f(a)$ and $f(b)$ has opposite signs by multiplying them together (because when a negative number multiplies a positive number, their product should be a negative number. If their product is equals to zero, first either $a$ and/or $b$ is/are the root(s) for the function, but at the same time it doesn't meet the requirement that they must be in opposite root in the function.) The code can be interpretated in another way like this:

```python
if func(a) * func(b) >= 0:
    raise ValueError("Function must have opposite signs at the endpoints.")
else:
    midpoints = []

    for _ in range(max_iter):
        # remaining implementation
```

For the second `raise ValueError` statement, it's dedicated for the `for` loop. This `raise ValueError` can be interpretated as in `else:` statement too (because `for` is recursive loop, it can be modified into iterative loop with `if`, but I'm not here to confuse you). This error will be raised if after `max_iter` iterations, `f(c)` still does not result in zero, and $|\frac{b - a}{2}|$ is still larger than tolerance level allowed. The purpose of this statement prevents infinite loops and a representation to indicate the method failed within the set tolerance.

```python
midpoints = []
```

This line initialise the variable `midpoints` as an empty list. This line shouldn't be added inside the `for` loop, otherwise the list resets every iteration.

```python
for _ in range(max_iter):
    c = (a + b) / 2
    midpoints.append(c)
```

Here, the `for` loop begins. 

```python
    if func(c) == 0 or abs(b - a) / 2 < tol:
        return c, midpoints
    elif func(a) * func(c) < 0:
        b = c
    else:
        a = c
```

#### 1.2.2 Newton-Raphson Method

#### 1.2.3 Secant Method

### 1.3 Returns

---

## 2. Trace Tables


---

## 3. Comparison Table


---

## 4. Plots of Convergence
