import points as pts
from quadrilateral import inQuadrilateralArea


def isAtUpperLeft(testPoint):#Point为待测点[x,y]

    in_area = inQuadrilateralArea(pts.left_track_upper_LBPoint,
                                pts.left_track_upper_LTPoint,
                                pts.left_track_upper_RTPoint,
                                pts.left_track_upper_RBPoint,
                                testPoint)
    if in_area: 
        return True
    else: 
        return False


def isAtUpperRight(testPoint):#Point为待测点[x,y]

    in_area = inQuadrilateralArea(pts.right_track_upper_LBPoint,
                                pts.right_track_upper_LTPoint,
                                pts.right_track_upper_RTPoint,
                                pts.right_track_upper_RBPoint,
                                testPoint)
    if in_area: 
        return True
    else: 
        return False



def correct_location(testPoint):
    if isAtUpperLeft(testPoint):
        testPoint[0] = int(testPoint[0] + 0.003*(testPoint[0]-pts.camera_center[0]))
        testPoint[1] = int(testPoint[1] - 0.003*(testPoint[1]-pts.camera_center[1]))
    elif isAtUpperRight(testPoint):
        testPoint[0] = int(testPoint[0] - 0.003*(testPoint[0]-pts.camera_center[0]))
        testPoint[1] = int(testPoint[1] - 0.003*(testPoint[1]-pts.camera_center[1]))
    else:
        testPoint[0] = int(testPoint[0] + 0.012*(testPoint[0]-pts.camera_center[0]))
        testPoint[1] = int(testPoint[1] + 0.009*(testPoint[1]-pts.camera_center[1]))
    return testPoint