# STANDARD Newton-Raphson Method Implementation
def newton_raphson(func, dfunc, x0, tol=1e-5, max_iter=100):
    """
    Perform the Newton-Raphson Method to find the root of a given function.
    
    Parameters:
        func (function): The function for which the root is to be found
        dfunc (function): The derivative of func
        x0 (float): Initial approximation
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
        
    Returns:
        root (float): Approximated root of func(x)
        approximations (list): List of x approximations
    """
    approximations = [x0]
    
    for _ in range(max_iter):
        if abs(dfunc(x0)) < 1e-10:
            raise ValueError("Derivative too small, method failed.")
            
        x1 = x0 - func(x0) / dfunc(x0)
        approximations.append(x1)
        
        if abs(x1 - x0) < tol:
            return x1, approximations
            
        x0 = x1
        
    raise ValueError("Newton-Raphson method did not converge.")
    
# Tracing Newton-Raphson Method
def newton_trace(func, dfunc, x0, tol=1e-5, max_iter=100):
    """
    Trace variables while performing the Newton-Raphson Method.
    
    Parameters:
        func (function): The function for which the root is to be found
        dfunc (function): The derivative of dfunc
        x0 (float): Initial approximation
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
        
    Returns:
        iteration (int): Number of iterations performed
        approximated (int): Number of approximations made
        current_x (list): List of current approximations
        func_x (list): List of func(x0)
        dfunc_x (list): List of dfunc(x0)
        new_x (list): List of new approximations
    """
    approximations = [x0]
    iteration = 0
    current_x = []
    func_x = []
    dfunc_x = []
    new_x = []
    
    for _ in range(max_iter):
        if abs(dfunc(x0)) < 1e-10:
            raise ValueError("Derivative too small, method fails.")
            
        current_x.append(x0)
        func_x.append(func(x0))
        dfunc_x.append(dfunc(x0))
        
        x1 = x0 - func(x0) / dfunc(x0)
        
        approximations.append(x1)
        new_x.append(x1)
        iteration += 1
        
        if abs(x1 - x0) < tol:
            return iteration, len(approximations), current_x, func_x, dfunc_x, new_x
            
        x0 = x1
        
    raise ValueError("Newton-Raphson method did not converge.")
    
# CPU time for Newton-Raphson Method
import time
import numpy as np

def newton_time(func, dfunc, x0):
    """
    Monitor execution time for the Newton-Raphson Method while finding the root of a given function.
    
    Parameters:
        func (function): The function for which the root is to be found
        dfunc (function): The derivative of func
        x0 (float): Initial approximation
        
    Returns:
        times (list): List of CPU times
        mean_time (float): Average CPU time
        min_time (float): Fastest CPU time
        max_time (float): Slowest CPU time
    """
    times = []
    
    for _ in range(100):
        start_time = time.process_time()
        root, approximations = newton_raphson(func, dfunc, x0)
        end_time = time.process_time()
        
        times.append(end_time - start_time)
    
    return times, np.mean(times), np.min(times), np.max(times)
    
# Monitor error
import numpy as np

def newton_error(func, dfunc, x0, true_root, tol=1e-5, max_iter=100):
    """
    Trace errors while performing the Newton-Raphson method.
    
    Parameters:
        func (function): The functino for which the root is to be found
        dfunc (function): The derivative of func
        x0 (float): Initial approximation
        true_root (float): Exact value of the root computing for
        tol (float): Tolerance level for convergence
        max_iter (int): Maximum number of iterations allowed
        
    Returns:
        errors (list): List of errors between each approximations and true_root
        abs_error (float): Absolute error between approximated root and true_root
        percent_error (float): Percentage error between approximated root and true_root
    """
    errors = [x0 - true_root]
    
    for _ in range(max_iter):
        if abs(dfunc(x0)) < 1e-10:
            raise ValueError("Derivative too small, method fails.")
            
        x1 = x0 - func(x0) / dfunc(x0)
        errors.append(x1 - true_root)
        
        if abs(x1 - x0) < tol:
            return errors, abs(x1 - true_root), abs(x1 - true_root) / true_root * 100
            
        x0 = x1
        
    raise ValueError("Newton-Raphson method did not converge.")