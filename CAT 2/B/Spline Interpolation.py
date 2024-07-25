from scipy.interpolate import CubicSpline
import numpy as np

x = np.array([1, 2, 3])
y = np.array([1, 4, 9])
cs = CubicSpline(x, y)
print(cs(2.5))
