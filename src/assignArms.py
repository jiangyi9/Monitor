import points as pts
from converting import convert_array, convert_pix_to_mm
from numpyArrayEncoder import NumpyArrayEncoder
import json
import numpy as np

# define the maximum range of arms
MAX_RANGE_OF_FIXED_ARM = 500
MAX_RANGE_OF_MOVING_ARM = 500

# define two lists to store cubes assigned to the two arms, respectively.
cubes_assigned_to_fixed_arm = []
cubes_assigned_to_moving_arm = []

# assign cubes to the closest arm
def assignArms(point_array):

    for point in point_array:

        # compute the Euclidean Distance between the point and the two arms, respectively.
        distance_to_the_fixed_arm = distEclud(point, pts.fixed_arm)
        distance_to_the_moving_arm = distEclud(point, pts.moving_arm)

        # If the point falls in the fixed-arm (orange) semi-circle, then assign the point to the fixed arm.
        if distance_to_the_fixed_arm < MAX_RANGE_OF_FIXED_ARM and point[1]-pts.fixed_arm[1] > 0:
            cubes_assigned_to_fixed_arm.append([convert_pix_to_mm(point[0],pts.fixed_arm[0]),
                                                convert_pix_to_mm(point[1],pts.fixed_arm[1]),
                                                point[2],
                                                point[3]])
        
        # If the point falls in the moving-arm (purple) semi-circle, then assign the point to the moving arm.
        elif distance_to_the_moving_arm < MAX_RANGE_OF_MOVING_ARM and point[1]-pts.moving_arm[1]>0:
            cubes_assigned_to_moving_arm.append([convert_pix_to_mm(point[0],pts.moving_arm[0]),
                                                convert_pix_to_mm(point[1],pts.moving_arm[1]),
                                                point[2],
                                                point[3]])

    print(cubes_assigned_to_fixed_arm)
    print(cubes_assigned_to_moving_arm)

    # Serialize the assigned points, export them as JSON.
    numpyData = {"cubes_assigned_to_fixed_arm": convert_array(cubes_assigned_to_fixed_arm), "cubes_assigned_to_moving_arm": convert_array(cubes_assigned_to_moving_arm)}
    with open("numpyData.json", "w") as write_file:
        json.dump(numpyData, write_file, cls=NumpyArrayEncoder, indent=2)

# compute the Euclidean Distance between two vectors
def distEclud(point, arm):
    return np.sqrt(np.sum(np.power((point[:2] - arm), 2)))