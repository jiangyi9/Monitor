import points as pts
import converting
import numpyArrayEncoder
import json

# define the maximum range of arms
MAX_RANGE_OF_FIXED_ARM = 512
MAX_RANGE_OF_MOVING_ARM = 512

# define two lists to store cubes assigned to two arms, respectively.
cubes_assigned_to_fixed_arm = []
cubes_assigned_to_moving_arm = []

# assign cubes to the closest arm
def assign_arm(point_array):
    for point in point_array:
        distance_to_the_fixed_arm = (point[0]-pts.fixed_arm_x)*(point[0]-pts.fixed_arm_x) + (point[1]-pts.fixed_arm_y)*(point[1]-pts.fixed_arm_y)
        distance_to_the_moving_arm = (point[0]-pts.moving_arm_x)*(point[0]-pts.moving_arm_x) + (point[1]-pts.moving_arm_y)*(point[1]-pts.moving_arm_y)
        if distance_to_the_fixed_arm > MAX_RANGE_OF_FIXED_ARM*MAX_RANGE_OF_FIXED_ARM and distance_to_the_moving_arm > MAX_RANGE_OF_MOVING_ARM*MAX_RANGE_OF_MOVING_ARM:
            continue
        elif distance_to_the_fixed_arm < distance_to_the_moving_arm:
            cubes_assigned_to_fixed_arm.append([converting.convert_pix_to_mm(point[0],pts.fixed_arm_x),converting.convert_pix_to_mm(point[1],pts.fixed_arm_y),point[2]])
        else:
            cubes_assigned_to_moving_arm.append([converting.convert_pix_to_mm(point[0],pts.moving_arm_x),converting.convert_pix_to_mm(point[1],pts.moving_arm_y),point[2]])

    print(cubes_assigned_to_fixed_arm)
    print(cubes_assigned_to_moving_arm)

    # Serialization
    numpyData = {"cubes_assigned_to_fixed_arm": converting.convert_array(cubes_assigned_to_fixed_arm), "cubes_assigned_to_moving_arm": converting.convert_array(cubes_assigned_to_moving_arm)}
    with open("numpyData.json", "w") as write_file:
        json.dump(numpyData, write_file, cls=numpyArrayEncoder.NumpyArrayEncoder, indent=2)