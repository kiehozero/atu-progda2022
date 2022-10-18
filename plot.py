# based roughly on the tutorial found at https://matplotlib.org/stable/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10, 0, 0.01)
y = 3.0 * x

# the 'b'in the 'bo' parameter will remove the default assumption that there is a linear relationship between the points along the x-axis
plt.plot([1,2,3,4],[1,7,5,4], 'bo')
plt.xlabel("rubbish")
plt.ylabel('some numbers')
plt.show()
print(x)