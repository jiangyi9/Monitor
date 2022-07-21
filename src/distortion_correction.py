import numpy as np
import cv2


def read_image(fname):
    image = cv2.imread(fname)
    return image


def get_image_height_and_width(image):
    return image.shape[:2]


def get_mapping_relation(source_image, a, b, c, d, mapping_fname):
    height, width = get_image_height_and_width(source_image)

    x, y = np.meshgrid(range(width), range(height))
    x = x.reshape(-1)
    y = y.reshape(-1)
    location_of_source_image = np.stack([x, y], 1)

    center_x = x.mean()
    center_y = y.mean()
    center = np.array([center_x, center_y])
    norm = np.mean(center)
    dist = np.sqrt(((location_of_source_image - center) ** 2).sum(1))

    r = np.sqrt(((x - center_x) / norm) ** 2 + ((y - center_y) / norm) ** 2)
    rdest = (a * r ** 4 + b * r ** 3 + c * r ** 2 + d * r) * norm

    target_x = rdest / dist * (x - center_x) + center_x
    target_y = rdest / dist * (y - center_y) + center_y
    location_of_dest_image = np.stack([target_x, target_y], 1)

    save_array_as_npy(mapping_fname, location_of_dest_image)


def save_array_as_npy(fname, array):
    np.save(fname, array)


if __name__ == "__main__":
    # 1. set some necessary params
    param_a = 0.056  # affects only the outermost pixels of the image
    param_b = -0.37  # most cases only require b optimization
    param_c = 0.43  # most uniform correction
    param_d = 1.0 - param_a - param_b - param_c  # describes the linear scaling of the image
    mapping_where_to_save = "C:\\Users\\19539\\Desktop\\Monitor\\location_of_dest_image.npy"

    # 2. read a image
    color = read_image("C:\\Users\\19539\\Desktop\\Monitor\\pic.png")

    # 3. get mapping and save it as npy
    get_mapping_relation(color, param_a, param_b, param_c, param_d, mapping_where_to_save)



    dest_array = np.load("C:\\Users\\19539\\Desktop\\Monitor\\location_of_dest_image.npy")
    dest_array = dest_array.reshape((-1, 2))

    original_image_name = "C:\\Users\\19539\\Desktop\\Monitor\\pic.png"
    color = cv2.imread(original_image_name)
    width, height, ndim = color.shape[1], color.shape[0], color.shape[2]

    map_x = dest_array[:, 1].reshape((height, width)).astype(np.float32)
    map_y = dest_array[:, 0].reshape((height, width)).astype(np.float32)

    mapped_img = cv2.remap(color, map_y, map_x, cv2.INTER_LINEAR)
    # cropped = mapped_img[15:1065,:]
    cv2.imwrite(
        "C:\\Users\\19539\\Desktop\\Monitor\\pic_undistort.png", mapped_img)
