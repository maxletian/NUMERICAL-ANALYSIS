import numpy as np

def lagrange_interpolation(x, y):
    def basis_polynomial(i):
        p = [(x[i] - x[j]) if j != i else 1 for j in range(len(x))]
        b = np.poly(p)
        return b / np.prod([x[i] - x[j] for j in range(len(x)) if j != i])
    
    L = sum(y[i] * basis_polynomial(i) for i in range(len(x)))
    return L

# Example usage
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
coefficients = lagrange_interpolation(x, y)
print(coefficients)
