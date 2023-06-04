import numpy as np
import matplotlib.pyplot as plt

#27000; 91033
#28000; 101312
#29000; 112085

# Define some data points with uncertainties
x = np.array([91033, 101312, 112085])
y = np.array([27000, 28000, 29000])
sigma = np.repeat(1.0, 3)

# Use the inverse of the uncertainties as weights
w = 1 / sigma

# Fit a quadratic equation using numpy.polyfit with weights
a, b = np.polyfit(x, y, 1) # w=w

# Print the coefficients
print(f"a = {a:.6f}, b = {b:.3f}") #, c = {c:.3f}, d = {d:.3f}")

# Plot the data points with error bars and the fitted curve
plt.errorbar(x, y, yerr=sigma, fmt="o", label="Data")
plt.plot(x, a*x + b, label="Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
