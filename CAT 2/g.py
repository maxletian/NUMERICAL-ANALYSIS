import numpy as np
import matplotlib.pyplot as plt

# Define the function to integrate
def f(x):
    return x**2

# Trapezoidal rule implementation
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = h * (np.sum(y) - (y[0] + y[-1]) / 2)
    return integral

# Parameters
a = 0  # Lower limit
b = 1  # Upper limit
n = 5  # Number of trapezoids

# Approximate the integral
approx_integral = trapezoidal_rule(f, a, b, n)
print(f"Approximate integral of f(x) from {a} to {b} is: {approx_integral}")

# Plotting the function and the trapezoids
x = np.linspace(a, b, 1000)
y = f(x)

plt.plot(x, y, label='f(x) = x^2')
plt.fill_between(x, 0, y, alpha=0.1)

# Trapezoids
x_trap = np.linspace(a, b, n+1)
y_trap = f(x_trap)
for i in range(n):
    plt.plot([x_trap[i], x_trap[i]], [0, y_trap[i]], 'r')
    plt.plot([x_trap[i+1], x_trap[i+1]], [0, y_trap[i+1]], 'r')
    plt.plot([x_trap[i], x_trap[i+1]], [y_trap[i], y_trap[i+1]], 'r')

plt.title('Trapezoidal Rule Approximation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
