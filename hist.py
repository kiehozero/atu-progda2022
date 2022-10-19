import matplotlib.pyplot as plt
import numpy as np

# normal takes the parameters and creates a normal/Gaussian distribution
x = np.random.normal(0.0, 1.0, 1000)

# subplot will position the plot that follows it, it firstly chooses the number of rows and columns in the overall plot, while
# the final number is an index number, starting at 1 for the box at co-ordinate 1,1, and finishing at co-ordinate 2,2 (index 4)
plt.subplot(2, 2, 1)
plt.hist(x, bins=1000)

# uniform takes the parameters and creates a roughly similar number for each bin, while not being exactly the same amount
z = np.random.uniform(-4.0,3.0,1000)
# here is the corresponding subplot that places the second chart to the bottom-right
plt.subplot(2, 2, 4)
plt.hist(z)
plt.show()