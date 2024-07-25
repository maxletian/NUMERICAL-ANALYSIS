from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([1, 2, 3]).reshape(-1, 1)
y = np.array([1, 2, 3])
model = LinearRegression().fit(x, y)
print(model.coef_, model.intercept_)
