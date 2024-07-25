import sympy as sp

x = sp.symbols('x')
function = x**2 - x - 2
derivative = sp.diff(function, x)
print(derivative)
