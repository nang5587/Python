import matplotlib.pyplot as plt
import numpy as np

# def f(x):
#     return x + 1
# def f2(x):
#     return x ** 2 + 2*x + 1

# x = np.arange(10)
# # x = [1,2,3,4,5,6,7,8,9]
# plt.plot(x, f(x))
# # plt.show()

# data = np.array([1,2,3])
# print(data, f(data))

# def f(x):
#     return x**2

# x = np.array([1,2,3,4,5])
# plt.plot(x,f(x))
# plt.show()

# x= np.arange(10)
# y = np.arange(5,15)
# print(len(x), len(y))
# plt.scatter(x,y)
# plt.show()

# x= np.arange(-10, 10, 0.1)


# x = np.linspace(-10, 10, 20)
# y = x**2
# print(x,y)
# plt.scatter(x,y)
# plt.savefig('fig.png')

# import random
# # d = [random.randint(1,6) for _ in range(10000)]
# x = [random.randint(1,9) for _ in range(100)]
# y = [random.randint(1,9) for _ in range(100)]

# plt.plot(x,y)
# plt.show()

from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()