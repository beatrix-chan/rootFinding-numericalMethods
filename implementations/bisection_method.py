# STANDARD Bisection Method Implementation
def bisection(func, a, b, tol=1e-5, max_iter=100):
    """
    Perform the Bisection Method to find the root of a given function.
    
    Parameters:
        func (function): The function for which the root is to be found
        a (float): Left endpoint of the interval
        b (float): Right endpoint of the interval
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
        
    Returns:
        root (float): Approximated root of func(x)
        midpoints (list): List of midpoint approximations
    """
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

# Tracing Bisection Method    
def bisection_trace(func, a, b, tol=1e-5, max_iter=100):
    """
    Trace variables while performing the Bisection Method to find the root of a given function.
    
    Parameters:
        func (function): The function for which the root is to be found
        a (float): Left endpoint of the interval
        b (float): Right endpoint of the interval
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
        
    Returns:
        iteration (int): Number of iterations performed
        approximated (int): Number of approximation made
        a_list (list): List of a
        b_list (list): List of b
        func_a (list): List of func(a)
        func_b (list): List of func(b)
        c_list (list): List of c
        func_c (list): List of func(c)
    """
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have opposite signs at the endpoints.")
        
    iteration = 0
    a_list = []
    b_list = []
    func_a = []
    func_b = []
    c_list = []
    func_c = []
    
    for _ in range(max_iter):
        a_list.append(a)
        b_list.append(b)
        func_a.append(func(a))
        func_b.append(func(b))
        
        c = (a + b) / 2
        
        c_list.append(c)
        func_c.append(func(c))
        iteration += 1
        
        if func(c) == 0 or abs(b - a) / 2 < tol:
            return iteration, len(c_list), a_list, b_list, func_a, func_b, c_list, func_c
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
            
    raise ValueError("Bisection method did not converge.")

# Monitor CPU time    
import time
import numpy as np

def bisection_time(func, a, b):
    """
    Trace CPU time while performing the Bisection Method to find the root of a given function.
    
    Parameters:
        func (function): The function for which the root is to be found
        a (float): Left endpoint of the interval
        b (float): Right endpoint of the interval
        
    Returns:
        times (list): List of CPU times
        mean_time (float): Average CPU time
        min_time (float): Fastest CPU time
        max_time (float): Slowest CPU time
    """
    times = []
    
    for _ in range(100):
        start_time = time.process_time()
        root, midpoints = bisection(func, a, b)
        end_time = time.process_time()
        
        times.append(end_time - start_time)
    
    return times, np.mean(times), np.min(times), np.max(times)

# Monitor error    
import numpy as np

def bisection_error(func, a, b, true_root, tol=1e-5, max_iter=100):
    """
    Trace errors while performing the Bisection Method.
    
    Parameters:
        func (function): The function for which the root is to be found
        a (float): Left endpoint of the interval
        b (float): Right endpoint of the interval
        true_root (float): Exact value of the root computing for
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
        
    Returns:
        errors (list): List of errors between each midpoints and true_root
        abs_error (float): Absolute error between approximated root and true_root
        percent_error (float): Percentage error between approximated root and true_root
    """
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have opposite signs at the endpoints.")
        
    errors = []
    
    for _ in range(max_iter):
        c = (a + b) / 2
        
        errors.append(c - true_root)
        
        if func(c) == 0 or abs(b - a) / 2 <  tol:
            return errors, abs(c - true_root), abs(c - true_root) / true_root * 100
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
            
    raise ValueError("Bisection Method did not converge.")
