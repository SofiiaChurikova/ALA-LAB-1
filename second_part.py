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


image = cv2.imread("31aca9782309cc934ce0066c2c81ab2f.jpeg")
# ------------------------------------
# Фото без перетворень

# plot_image(image)
# ------------------------------------
# Фото обернене на певний кут

# rotated_image = rotation(image, 45)
# plot_image(rotated_image)
# ------------------------------------
# Фото маштабоване з певним коефіцієнтом

# scaled_image = scale(image, 2)
# plot_image(scaled_image)
# ------------------------------------
# Фото відзеркалене за певної осі

# reflected_image = axis_reflection(image, "x")
# plot_image(reflected_image)
# ------------------------------------
# Нахил певної осі координат

# shear_image = shear_axis(image, 20, "x")
# plot_image(shear_image)
# ------------------------------------
# Трансформація з переданою у функцію кастомною матрицею трансформації

# transformed_image = universal_transformation(image, np.float32([[0, 1, 1], [1, 1, 0]]))
# plot_image(transformed_image)
# ------------------------------------
