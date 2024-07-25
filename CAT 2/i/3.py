import matplotlib.pyplot as plt
import numpy as np


# Generate more points for a smooth curve
x_vals = np.linspace(1, 4, 100)
lagrange_poly = np.poly1d(lagrange_interpolation(x, y))
newton_poly_vals = [newton_poly(xi) for xi in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro', label='Data points')
plt.plot(x_vals, lagrange_poly(x_vals), label='Lagrange Polynomial')
plt.plot(x_vals, newton_poly_vals, label='Newton Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Comparison of Lagrange and Newton Polynomials')
plt.show()
