import matplotlib.pyplot as plt
import numpy as np
import cv2


def plot_image(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()


def rotation(image, angle):
    rows, cols = image.shape[:2]
    center = (cols // 2, rows // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    return rotated_image


def scale(image, coeff):
    scaled_image = cv2.resize(image, None, fx=coeff, fy=coeff, interpolation=cv2.INTER_LINEAR)
    return scaled_image


def axis_reflection(image, axis):
    if axis == "x":
        reflected_image = cv2.flip(image, 0)
    elif axis == "y":
        reflected_image = cv2.flip(image, 1)
    return reflected_image


def shear_axis(image, angle, axis):
    rad_angle = np.radians(angle)
    if axis == "x":
        shear_matrix = np.float32([[1, rad_angle, 0], [0, 1, 0]])
    elif axis == "y":
        shear_matrix = np.float32([[1, 0, 0], [rad_angle, 1, 0]])
    rows, cols = image.shape[:2]
    sheared_image = cv2.warpAffine(image, shear_matrix, (cols, rows))
    return sheared_image


def universal_transformation(image, matrix):
    rows, cols = image.shape[:2]
    transformed_image = cv2.warpAffine(image, matrix, (cols, rows))
    return transformed_image


def create_image_from_figure(figure, size=(900, 900), color='r'):
    fig, ax = plt.subplots()
    ax.plot(figure[:, 0], figure[:, 1], color)
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.axis('off')
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    image = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)
    return image


image = cv2.imread("31aca9782309cc934ce0066c2c81ab2f.jpeg")

batman_figure = np.array([
    [0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4],
    [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
flower_figure = np.array([
    [0, 0], [0.2, 0.5], [0.5, 0.2], [0.7, 0.7], [1, 0.4],
    [0.5, 1], [0, 0.8], [-0.5, 1], [-1, 0.4], [-0.7, 0.7],
    [-0.5, 0.2], [-0.2, 0.5], [0, 0]
])

batman_image = create_image_from_figure(batman_figure)
flower_image = create_image_from_figure(flower_figure)

# ------------------------------------
# Фото без перетворень

# plot_image(image)
# plot_image(batman_image)
# plot_image(flower_image)
# ------------------------------------
# Фото обернене на певний кут

# rotated_image = rotation(image, 45)
# plot_image(rotated_image)
#
# rotated_batman = rotation(batman_image, 45)
# plot_image(rotated_batman)
#
# rotated_flower = rotation(flower_image, 60)
# plot_image(rotated_flower)
# ------------------------------------
# Фото маштабоване з певним коефіцієнтом

# scaled_image = scale(image, 2)
# plot_image(scaled_image)

# scaled_batman = scale(batman_image, 2)
# plot_image(scaled_batman)
#
# scaled_flower = scale(flower_image, 4)
# plot_image(scaled_flower)
# ------------------------------------
# Фото відзеркалене за певної осі

# reflected_image = axis_reflection(image, "x")
# plot_image(reflected_image)

reflected_batman = axis_reflection(batman_image, "x")
plot_image(reflected_batman)
#
# reflected_flower = axis_reflection(flower_image, "y")
# plot_image(reflected_flower)
# ------------------------------------
# Нахил певної осі координат

# shear_image = shear_axis(image, 20, "x")
# plot_image(shear_image)

# shear_batman = shear_axis(batman_image, 35, "x")
# plot_image(shear_batman)
#
# shear_flower = shear_axis(flower_image, 20, "y")
# plot_image(shear_flower)
# ------------------------------------
# Трансформація з переданою у функцію кастомною матрицею трансформації

# transformed_image = universal_transformation(image, np.float32([[0, 1, 1], [1, 1, 0]]))
# plot_image(transformed_image)

# transformed_batman = universal_transformation(batman_image, np.float32([[1, 0, 1], [1, 0.5, 0]]))
# plot_image(transformed_batman)
#
# transformed_flower = universal_transformation(flower_image, np.float32([[0.5, 0, 0], [1, 0.5, 0]]))
# plot_image(transformed_flower)
# ------------------------------------
