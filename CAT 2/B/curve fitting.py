import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * x**2 + b * x + c

x_data = np.array([1, 2, 3])
y_data = np.array([0, 2, 6])
params, params_covariance = curve_fit(func, x_data, y_data)
print(params)
