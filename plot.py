# based roughly on the tutorial found at https://matplotlib.org/stable/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x
noise = np.random.normal(0.0,2.0,len(x))

# the 'b'in the 'bo' parameter will remove the default assumption that there is a linear relationship between the points along the x-axis
plt.plot(x, y + noise, 'g-')
plt.plot(x,y, 'b.')
plt.xlabel("rubbish")
plt.ylabel('some numbers')
plt.show()
