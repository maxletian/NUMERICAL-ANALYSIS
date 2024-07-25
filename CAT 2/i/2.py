def newton_divided_difference(x, y):
    n = len(x)
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = y

    for j in range(1, n):
        for i in range(n-j):
            divided_diff[i,j] = (divided_diff[i+1,j-1] - divided_diff[i,j-1]) / (x[i+j] - x[i])

    def newton_polynomial(x_val):
        result = divided_diff[0,0]
        product_term = 1.0
        for j in range(1, n):
            product_term *= (x_val - x[j-1])
            result += divided_diff[0,j] * product_term
        return result

    coefficients = divided_diff[0]
    return coefficients, newton_polynomial

# Example usage
coefficients, newton_poly = newton_divided_difference(x, y)
print(coefficients)
