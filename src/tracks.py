import points as pts

# judge whether a point is in or out of the track
def isOnTrack(testPoint):#testPoint为待测点[x,y]

    # define area 1 as the left track (pink)
    LBPoint_1 = [pts.corner_left_4_x, pts.corner_left_4_y]
    LTPoint_1 = [pts.corner_left_1_x, pts.corner_left_1_y]
    RTPoint_1 = [pts.corner_left_2_x, pts.corner_left_2_y]
    RBPoint_1 = [pts.corner_left_3_x, pts.corner_left_3_y]
    a = (LTPoint_1[0]-LBPoint_1[0])*(testPoint[1]-LBPoint_1[1])-(LTPoint_1[1]-LBPoint_1[1])*(testPoint[0]-LBPoint_1[0])
    b = (RTPoint_1[0]-LTPoint_1[0])*(testPoint[1]-LTPoint_1[1])-(RTPoint_1[1]-LTPoint_1[1])*(testPoint[0]-LTPoint_1[0])
    c = (RBPoint_1[0]-RTPoint_1[0])*(testPoint[1]-RTPoint_1[1])-(RBPoint_1[1]-RTPoint_1[1])*(testPoint[0]-RTPoint_1[0])
    d = (LBPoint_1[0]-RBPoint_1[0])*(testPoint[1]-RBPoint_1[1])-(LBPoint_1[1]-RBPoint_1[1])*(testPoint[0]-RBPoint_1[0])
    in_area_1 = (a>0 and b>0 and c>0 and d>0) or (a<0 and b<0 and c<0 and d<0)

    # define area 2 as the right track (pink)
    LBPoint_2 = [pts.corner_right_4_x, pts.corner_right_4_y]
    LTPoint_2 = [pts.corner_right_1_x, pts.corner_right_1_y]
    RTPoint_2 = [pts.corner_right_2_x, pts.corner_right_2_y]
    RBPoint_2 = [pts.corner_right_3_x, pts.corner_right_3_y]
    a = (LTPoint_2[0]-LBPoint_2[0])*(testPoint[1]-LBPoint_2[1])-(LTPoint_2[1]-LBPoint_2[1])*(testPoint[0]-LBPoint_2[0])
    b = (RTPoint_2[0]-LTPoint_2[0])*(testPoint[1]-LTPoint_2[1])-(RTPoint_2[1]-LTPoint_2[1])*(testPoint[0]-LTPoint_2[0])
    c = (RBPoint_2[0]-RTPoint_2[0])*(testPoint[1]-RTPoint_2[1])-(RBPoint_2[1]-RTPoint_2[1])*(testPoint[0]-RTPoint_2[0])
    d = (LBPoint_2[0]-RBPoint_2[0])*(testPoint[1]-RBPoint_2[1])-(LBPoint_2[1]-RBPoint_2[1])*(testPoint[0]-RBPoint_2[0])
    in_area_2 = (a>0 and b>0 and c>0 and d>0) or (a<0 and b<0 and c<0 and d<0)

    if in_area_1 or in_area_2: # if the point falls in either the left track or the right track, return True.
        return True
    else: # else, return False.
        return False