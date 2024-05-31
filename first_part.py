import numpy as np
import matplotlib.pyplot as plt

def plot_object(object, title):
    plt.figure()
    plt.plot(object[:, 0], object[:, 1])
    plt.title(title)
    plt.axis('equal')
    plt.grid(True)
    plt.show()


def rotation(object, angle):
    rad_angle = np.radians(angle)
    rotation_matrix = np.array([[np.cos(rad_angle), -np.sin(rad_angle)], [np.sin(rad_angle), np.cos(rad_angle)]])
    rotated_object = np.dot(object, rotation_matrix)
    return rotated_object


def scale(object, coeff):
    scaled_object = object * coeff
    return scaled_object


def axis_reflection(object, axis):
    if axis == "x":
        reflection_matrix = np.array([[1, 0], [0, -1]])
    elif axis == "y":
        reflection_matrix = np.array([[-1, 0], [0, 1]])
    reflected_object = np.dot(object, reflection_matrix)
    return reflected_object


def shear_axis(object, angle, axis):
    rad_angle = np.radians(angle)
    if axis == "x":
        shear_matrix = np.array([[1, 0], [rad_angle, 1]])
        shear_object = np.dot(object, shear_matrix)
    if axis == "y":
        shear_matrix = np.array([[1, rad_angle], [0, 1]])
        shear_object = np.dot(object, shear_matrix)
    return shear_object


def universal_transformation(object, matrix):
    transformed_matrix = np.dot(object, matrix)
    return transformed_matrix


def plot_object_3d(object, title):
    figure = plt.figure()
    ax = figure.add_subplot(projection='3d')
    ax.plot(object[:, 0], object[:, 1], object[:, 2], 'o-')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.show()


def axis_reflection_3d(object, axis):
    if axis == "x":
        reflection_matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
    elif axis == "y":
        reflection_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])
    elif axis == "z":
        reflection_matrix = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    reflected_object = np.dot(object, reflection_matrix)
    return reflected_object


def shear_axis_3d(object, angle, axis):
    rad_angle = np.radians(angle)
    if axis == "x":
        shear_matrix = np.array([[1, 0, 0], [np.tan(rad_angle), 1, 0], [np.tan(rad_angle), 0, 1]])
        shear_object = np.dot(object, shear_matrix)
    elif axis == "y":
        shear_matrix = np.array([[1, np.tan(rad_angle), 0], [0, 1, 0], [0, np.tan(rad_angle), 1]])
        shear_object = np.dot(object, shear_matrix)
    elif axis == "z":
        shear_matrix = np.array([[1, 0, np.tan(rad_angle)],[0, 1, np.tan(rad_angle)], [0, 0, 1]])
        shear_object = np.dot(object, shear_matrix)
    return shear_object


batman_figure = np.array([
    [0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4],
    [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
flower_figure = np.array([
    [0, 0], [0.2, 0.5], [0.5, 0.2], [0.7, 0.7], [1, 0.4],
    [0.5, 1], [0, 0.8], [-0.5, 1], [-1, 0.4], [-0.7, 0.7],
    [-0.5, 0.2], [-0.2, 0.5], [0, 0]
])

# Об'єкти без перетворень

# plot_object(batman_figure, "Batman")
# plot_object(flower_figure, "Flower")
# ------------------------------------
# Об'єкти обернені на певний кут

# rotated_batman = rotation(batman_figure, 45)
# plot_object(rotated_batman, "Rotated batman")

# rotated_flower = rotation(flower_figure, 90)
# plot_object(rotated_flower, "Rotated flower")
# ------------------------------------
# Об'єкти маштабовані з певним коефіцієнтом

# scaled_batman = scale(batman_figure, 2.5)
# scaled_flower = scale(flower_figure, 3)

# plot_object(scaled_batman, "Scaled Batman")
# plot_object(scaled_flower, "Scaled Flower")
# ------------------------------------
# Об'єкти відзеркаленні за певної осі

# reflected_batman_x = axis_reflection(batman_figure, "x")
# reflected_batman_y = axis_reflection(batman_figure, "y")

# reflected_flower_x = axis_reflection(flower_figure, "x")
# reflected_flower_y = axis_reflection(flower_figure, "y")

# plot_object(reflected_batman_x, "Reflected batman x-axis")
# plot_object(reflected_batman_y, "Reflected batman y-axis")

# plot_object(reflected_flower_x, "Reflected flower x-axis")
# plot_object(reflected_flower_y, "Reflected flower y-axis")
# ------------------------------------
# Нахил певної осі координат

# shear_batman_x = shear_axis(batman_figure, 45, "x")
# shear_batman_y = shear_axis(batman_figure, 45, "y")
#
# shear_flower_x = shear_axis(flower_figure, 45, "x")
# shear_flower_y = shear_axis(flower_figure, 45, "y")
#
# plot_object(shear_batman_x, "Shear Batman x-asis")
# plot_object(shear_batman_y, "Shear Batman y-asis")
#
# plot_object(shear_flower_x, "Shear Flower x-asis")
# plot_object(shear_flower_y, "Shear Flower y-asis")
# ------------------------------------
# Трансформація з переданою у функцію кастомною матрицею трансформації

# custom_matrix = np.array([[4, 2], [1, 1]])
# transformed_batman = universal_transformation(batman_figure, custom_matrix)
# plot_object(transformed_batman, "Transformed batman with custom matrix")
# ------------------------------------
# three_dimensional

pyramid_3d = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0],
    [0.5, 0.5, 1], [1, 1, 0], [0.5, 0.5, 1], [1, 0, 0],
    [0.5, 0.5, 1], [0, 1, 0]
])
# Об'єкт без перетворень

# plot_object_3d(pyramid_3d, "3D Pyramid")
# ------------------------------------
# Об'єкти відзеркалений за певної осі

# reflected_3d_pyramid = axis_reflection_3d(pyramid_3d, "x")
# plot_object_3d(reflected_3d_pyramid, "Reflected 3D Pyramid")
# ------------------------------------
# Нахил певної осі координат

# shear_pyramid_3d = shear_axis_3d(pyramid_3d, 45, "x")
# plot_object_3d(shear_pyramid_3d, "Shear Pyramid x-axis")