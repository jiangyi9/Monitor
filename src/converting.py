import numpy as np

# convert the relative location information from pix to mm. (we see the arm as the original point)
def convert_pix_to_mm(number, arm):
    converting_coefficient = 25/39
    return int((number-arm)*converting_coefficient)

# convert a set of points from list to array.
def convert_array(point_list):
    points = np.array(point_list)
    points = points.reshape(-1,4)
    points = points[np.lexsort(points[:,::-2].T)] # sort points according to the column location
    return points