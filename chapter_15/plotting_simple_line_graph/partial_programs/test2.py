import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

# x = np.array([1,2,3,4,5])
# plt.plot(x,f(x), lw=5)
# plt.show()

# fig, ax = plt.subplots(1,2)
# plt.style.use('seaborn-v0_8-pastel')
# ax[0].plot(x, f(x))
# ax[1].plot(x, f(x))
# plt.show()

plt.scatter([1,3], [5,8])
plt.show()