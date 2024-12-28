from matplotlib import pyplot as plt
import numpy as np

fix, ax = plt.subplots(1, 1)
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 1, 20, 51, 5, 79, 31, 27])
ax.hist(a, bins=[0, 25, 50, 75, 100])
ax.set_title("Histogram of result")
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xlabel("Marks")
ax.set_ylabel("no. of students")
plt.show()


