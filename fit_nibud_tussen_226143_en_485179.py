import numpy as np
import matplotlib.pyplot as plt

#55000; 226143
#56000; 230255
#57000; 239054
#58000; 243248
#59000; 252293
#60000; 256570
#61000; 265862
#62000; 270220
#63000; 274579
#64000; 278937
#65000; 283295
#66000; 293081
#67000; 297522
#68000; 301963
#69000; 312007
#70000; 316000
#71000; 321123
#72000; 331567
#73000; 336172
#74000; 340777
#75000; 345382
#81000; 379674
#100000; 485179

# Define some data points with uncertainties
x = np.array([226143.0, 230255.0, 239054.0, 243248.0, 252293.0, 256570.0, 265862.0, 270220.0, 274579.0, 278937.0, 283295.0, 293081.0, 297522.0, 301963.0, 312007.0, 316000.0, 321123.0, 331567.0, 336172.0, 340777.0, 345382.0, 379674.0, 485179.0])
y = np.array([55000.0, 56000.0, 57000.0, 58000.0, 59000.0, 60000.0, 61000.0, 62000.0, 63000.0, 64000.0, 65000.0, 66000.0, 67000.0, 68000.0, 69000.0, 70000.0, 71000.0, 72000.0, 73000.0, 74000.0, 75000.0, 81000.0, 100000.0])
sigma = np.repeat(1.0, 23)

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
