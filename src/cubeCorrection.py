import Points as pts


def isAtUpperLeft(testPoint):#testPoint为待测点[x,y]

    # define area 1 as the left track (pink)
    LBPoint_1 = [pts.upper_left_4_x, pts.upper_left_4_y]
    LTPoint_1 = [pts.upper_left_1_x, pts.upper_left_1_y]
    RTPoint_1 = [pts.upper_left_2_x, pts.upper_left_2_y]
    RBPoint_1 = [pts.upper_left_3_x, pts.upper_left_3_y]
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

    # define area 1 as the left track (pink)
    LBPoint_1 = [pts.upper_right_4_x, pts.upper_right_4_y]
    LTPoint_1 = [pts.upper_right_1_x, pts.upper_right_1_y]
    RTPoint_1 = [pts.upper_right_2_x, pts.upper_right_2_y]
    RBPoint_1 = [pts.upper_right_3_x, pts.upper_right_3_y]
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