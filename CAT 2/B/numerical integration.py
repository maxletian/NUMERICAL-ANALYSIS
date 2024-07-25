from scipy.integrate import quad

f = lambda x: x**2 - x - 2
result, error = quad(f, 1, 3)
print(result)
