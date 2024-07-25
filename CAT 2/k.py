import numpy as np

def gradient_descent(f, grad_f, initial_guess, learning_rate, num_iterations):
    x, y = initial_guess
    for _ in range(num_iterations):
        grad_x, grad_y = grad_f(x, y)
        x -= learning_rate * grad_x
        y -= learning_rate * grad_y
    return x, y

# Function to compute the value of f(x, y)
def f(x, y):
    return x**2 + y**2 - xy + x - y + 1

# Function to compute the gradient of f(x, y)
def grad_f(x, y):
    grad_x = 2*x - y + 1
    grad_y = 2*y - x - 1
    return grad_x, grad_y

# Parameters
initial_guess = (0, 0)
learning_rate = 0.1
num_iterations = 1000

# Running gradient descent
min_x, min_y = gradient_descent(f, grad_f, initial_guess, learning_rate, num_iterations)
print(f"Minimum found at x = {min_x}, y = {min_y}")
