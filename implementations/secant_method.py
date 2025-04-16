# STANDARD Secant Method Implementation
def secant(func, x0, x1, tol=1e-5, max_iter=100):
    """
    Perform the Secant Method to find the root of a given function.
    
    Parameters:
        func (function): The function for which the root is to be found
        x0 (float): First initial approximation
        x1 (float): Second initial approximation
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
        
    Returns:
        root (float): Approximated root of func(x)
        approximations (list): List of x approximations
    """
    approximations = [x0, x1]
    
    for _ in range(max_iter):
        if abs(func(x1) - func(x0)) < 1e-10:
            raise ValueError("Denominator too small, method fails.")
            
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        approximations.append(x2)
        
        if abs(x2 - x1) < tol:
            return x2, approximations
            
        x0, x1 = x1, x2
        
    raise ValueError("Secant method did not converge.")

# Tracing Secant Method
def secant_trace(func, x0, x1, tol=1e-5, max_iter=100):
    """
    Trace variables while performing the Secant Method to find the root of a given function.
    
    Parameters:
        func (function): The function for which the root is to be found
        x0 (float): First initial approximation
        x1 (float): Second intiial approximation
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
        
    Returns:
        iteration (int): Number of iterations performed
        approximated (int): Number of approximations made
        current_x (list): List of x1
        previous_x (list): List of x0
        func_x1 (list): List of func(x1)
        func_x0 (list): List of func(x0)
        new_x (list): List of x2
    """
    approximations = [x0, x1]
    iteration = 0
    current_x = []
    previous_x = []
    func_x1 = []
    func_x0 = []
    new_x = []
    
    for _ in range(max_iter):
        if abs(func(x1) - func(x0)) < 1e-10:
            raise ValueError("Denominator too small, method failed.")
            
        current_x.append(x1)
        previous_x.append(x0)
        func_x1.append(func(x1))
        func_x0.append(func(x0))
        
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        
        approximations.append(x2)
        new_x.append(x2)
        iteration += 1
        
        if abs(x2 - x1) < tol:
            return iteration, len(approximations), current_x, previous_x, func_x1, func_x0, new_x
        
        x0, x1 = x1, x2
        
    raise ValueError("Secant Method did not converge.")

# Monitor CPU time
import time
import numpy as np

def secant_time(func, x0, x1):
    """
    Monitor the execution time while performing the Secant Method to find the root of a given function.
    
    Parameters:
        func (function): The function for which the root is to be found
        x0 (float): First initial approximation
        x1 (float): Second initial approximation
        
    Returns:
        times (list): List of CPU times
        mean_time (float): Average CPU time
        min_time (float): Fastest CPU time
        max_time (float): Slowest CPU time
    """
    times = []
    
    for _ in range(100):
        start_time = time.process_time()
        root, approximations = secant(func, x0, x1)
        end_time = time.process_time()
        
        times.append(end_time - start_time)
        
    return times, np.mean(times), np.min(times), np.max(times)

# Monitor error
import numpy as np

def secant_error(func, x0, x1, true_root, tol=1e-5, max_iter=100):
    """
    Trace error while performing the Secant Method.
    
    Parameters:
        func (function): The function for which the root is to be found
        x0 (float): First initial approximation
        x1 (float): Second intiial approximation
        true_root (float): Exact value of the root computing for
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
        
    Returns:
        errors (list): List of errors between approximations and true_root
        abs_error (float): Absolute error between approximated root and true_root
        percent_error (float): Percentage error between approximated root and true_root
    """
    errors = [x0 - true_root, x1 - true_root]
    
    for _ in range(max_iter):
        if abs(func(x1) - func(x0)) < 1e-10:
            raise ValueError("Denominator too small, method failed.")
            
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        
        errors.append(x2 - true_root)
        
        if abs(x2 - x1) < tol:
            return errors, abs(x2 - true_root), abs(x2 - true_root) / true_root * 100
            
        x0, x1 = x1, x2
    
    raise ValueError("Secant Method did not converge.")