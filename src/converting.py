import numpy as np

def convert_pix_to_mm(number, arm):
    converting_coefficient = 25/39
    return int((number-arm)*converting_coefficient)

def convert_array(point_list):
    points = np.array(point_list)
    points = points.reshape(-1,3)
    points = points[np.lexsort(points[:,:-1:].T)] # sort according to the column location
    return points