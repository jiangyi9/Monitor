import points as pts
from quadrilateral import inQuadrilateralArea

# judge whether a point is in or out of the track
def isOnTrack(testPoint):#Point为待测点[x,y]

    in_left_track = inQuadrilateralArea(pts.left_track_LBPoint,
                                    pts.left_track_LTPoint,
                                    pts.left_track_RTPoint,
                                    pts.left_track_RBPoint,
                                    testPoint)

    in_right_track = inQuadrilateralArea(pts.right_track_LBPoint,
                                    pts.right_track_LTPoint,
                                    pts.right_track_RTPoint,
                                    pts.right_track_RBPoint,
                                    testPoint)

    if in_left_track or in_right_track: # if the point falls in either the left track or the right track, return True.
        return True
    else: # else, return False.
        return False