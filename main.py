import numpy as np
import matplotlib.pyplot as plt


def plot_object(object, title):
    plt.figure()
    plt.plot(object[:, 0], object[:, 1])
    plt.title(title)
    plt.axis('equal')
    plt.grid(True)
    plt.show()


batman_figure = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
flower_figure = np.array([
    [0, 0], [0.2, 0.5], [0.5, 0.2], [0.7, 0.7], [1, 0.4],
    [0.5, 1], [0, 0.8], [-0.5, 1], [-1, 0.4], [-0.7, 0.7],
    [-0.5, 0.2], [-0.2, 0.5], [0, 0]
])

print(plot_object(batman_figure, "Batman"))
print(plot_object(flower_figure, "Flower"))



