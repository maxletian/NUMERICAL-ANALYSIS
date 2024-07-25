from scipy.interpolate import interp1d

x_coords = [2.00, 4.25, 5.25, 7.81, 9.20, 10.60]
y_coords = [7.2, 7.1, 6.0, 5.0, 3.5, 5.0]

linear_spline = interp1d(x_coords, y_coords)
y_value = linear_spline(4.0)
print(y_value)
