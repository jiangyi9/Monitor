import points as pts


def isAtUpperLeft(testPoint):#testPoint为待测点[x,y]

    # define area 1 as the left track (white)
    LBPoint_1 = [pts.left_track_upper_LB_x, pts.left_track_upper_LB_y]
    LTPoint_1 = [pts.left_track_upper_LT_x, pts.left_track_upper_LT_y]
    RTPoint_1 = [pts.left_track_upper_RT_x, pts.left_track_upper_RT_y]
    RBPoint_1 = [pts.left_track_upper_RB_x, pts.left_track_upper_RB_y]
    a = (LTPoint_1[0]-LBPoint_1[0])*(testPoint[1]-LBPoint_1[1])-(LTPoint_1[1]-LBPoint_1[1])*(testPoint[0]-LBPoint_1[0])
    b = (RTPoint_1[0]-LTPoint_1[0])*(testPoint[1]-LTPoint_1[1])-(RTPoint_1[1]-LTPoint_1[1])*(testPoint[0]-LTPoint_1[0])
    c = (RBPoint_1[0]-RTPoint_1[0])*(testPoint[1]-RTPoint_1[1])-(RBPoint_1[1]-RTPoint_1[1])*(testPoint[0]-RTPoint_1[0])
    d = (LBPoint_1[0]-RBPoint_1[0])*(testPoint[1]-RBPoint_1[1])-(LBPoint_1[1]-RBPoint_1[1])*(testPoint[0]-RBPoint_1[0])
    in_area = (a>0 and b>0 and c>0 and d>0) or (a<0 and b<0 and c<0 and d<0)

    if in_area: 
        return True
    else: 
        return False


def isAtUpperRight(testPoint):#testPoint为待测点[x,y]

    # define area 2 as the left track (white)
    LBPoint_1 = [pts.right_track_upper_LB_x, pts.right_track_upper_LB_y]
    LTPoint_1 = [pts.right_track_upper_LT_x, pts.right_track_upper_LT_y]
    RTPoint_1 = [pts.right_track_upper_RT_x, pts.right_track_upper_RT_y]
    RBPoint_1 = [pts.right_track_upper_RB_x, pts.right_track_upper_RB_y]
    a = (LTPoint_1[0]-LBPoint_1[0])*(testPoint[1]-LBPoint_1[1])-(LTPoint_1[1]-LBPoint_1[1])*(testPoint[0]-LBPoint_1[0])
    b = (RTPoint_1[0]-LTPoint_1[0])*(testPoint[1]-LTPoint_1[1])-(RTPoint_1[1]-LTPoint_1[1])*(testPoint[0]-LTPoint_1[0])
    c = (RBPoint_1[0]-RTPoint_1[0])*(testPoint[1]-RTPoint_1[1])-(RBPoint_1[1]-RTPoint_1[1])*(testPoint[0]-RTPoint_1[0])
    d = (LBPoint_1[0]-RBPoint_1[0])*(testPoint[1]-RBPoint_1[1])-(LBPoint_1[1]-RBPoint_1[1])*(testPoint[0]-RBPoint_1[0])
    in_area = (a>0 and b>0 and c>0 and d>0) or (a<0 and b<0 and c<0 and d<0)

    if in_area: 
        return True
    else: 
        return False



def correct_location(point):
    if isAtUpperLeft(point):
        point[0] = int(point[0] + 0.003*(point[0]-pts.center_x))
        point[1] = int(point[1] - 0.003*(point[1]-pts.center_y))
    elif isAtUpperRight(point):
        point[0] = int(point[0] - 0.003*(point[0]-pts.center_x))
        point[1] = int(point[1] - 0.003*(point[1]-pts.center_y))
    else:
        point[0] = int(point[0] + 0.012*(point[0]-pts.center_x))
        point[1] = int(point[1] + 0.009*(point[1]-pts.center_y))
    return point