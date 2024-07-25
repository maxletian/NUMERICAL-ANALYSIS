def f(x):
    return 423 * 10**6 - 99331650 * x - x**4

def f_prime(x):
    return -99331650 - 4 * x**3

x0 = 0.5  # Initial guess
for i in range(3):
    x1 = x0 - f(x0) / f_prime(x0)
    error = abs((x1 - x0) / x1) * 100
    x0 = x1
    print(f"Iteration {i+1}, x = {x0}, Error = {error}%")
