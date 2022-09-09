import points as pts

# judge whether a point is in or out of the track
def isOnTrack(testPoint):#testPoint为待测点[x,y]

    # define area 1 as the left track (pink)
    left_track_LBPoint = [pts.left_track_LB_x, pts.left_track_LB_y]
    left_track_LTPoint = [pts.left_track_LT_x, pts.left_track_LT_y]
    left_track_RTPoint = [pts.left_track_RT_x, pts.left_track_RT_y]
    left_track_RBPoint = [pts.left_track_RB_x, pts.left_track_RB_y]
    a = (left_track_LTPoint[0]-left_track_LBPoint[0])*(testPoint[1]-left_track_LBPoint[1])-(left_track_LTPoint[1]-left_track_LBPoint[1])*(testPoint[0]-left_track_LBPoint[0])
    b = (left_track_RTPoint[0]-left_track_LTPoint[0])*(testPoint[1]-left_track_LTPoint[1])-(left_track_RTPoint[1]-left_track_LTPoint[1])*(testPoint[0]-left_track_LTPoint[0])
    c = (left_track_RBPoint[0]-left_track_RTPoint[0])*(testPoint[1]-left_track_RTPoint[1])-(left_track_RBPoint[1]-left_track_RTPoint[1])*(testPoint[0]-left_track_RTPoint[0])
    d = (left_track_LBPoint[0]-left_track_RBPoint[0])*(testPoint[1]-left_track_RBPoint[1])-(left_track_LBPoint[1]-left_track_RBPoint[1])*(testPoint[0]-left_track_RBPoint[0])
    in_area_1 = (a>0 and b>0 and c>0 and d>0) or (a<0 and b<0 and c<0 and d<0)

    # define area 2 as the right track (pink)
    right_track_LBPoint = [pts.right_track_LB_x, pts.right_track_LB_y]
    right_track_LTPoint = [pts.right_track_LT_x, pts.right_track_LT_y]
    right_track_RTPoint = [pts.right_track_RT_x, pts.right_track_RT_y]
    right_track_RBPoint = [pts.right_track_RB_x, pts.right_track_RB_y]
    a = (right_track_LTPoint[0]-right_track_LBPoint[0])*(testPoint[1]-right_track_LBPoint[1])-(right_track_LTPoint[1]-right_track_LBPoint[1])*(testPoint[0]-right_track_LBPoint[0])
    b = (right_track_RTPoint[0]-right_track_LTPoint[0])*(testPoint[1]-right_track_LTPoint[1])-(right_track_RTPoint[1]-right_track_LTPoint[1])*(testPoint[0]-right_track_LTPoint[0])
    c = (right_track_RBPoint[0]-right_track_RTPoint[0])*(testPoint[1]-right_track_RTPoint[1])-(right_track_RBPoint[1]-right_track_RTPoint[1])*(testPoint[0]-right_track_RTPoint[0])
    d = (right_track_LBPoint[0]-right_track_RBPoint[0])*(testPoint[1]-right_track_RBPoint[1])-(right_track_LBPoint[1]-right_track_RBPoint[1])*(testPoint[0]-right_track_RBPoint[0])
    in_area_2 = (a>0 and b>0 and c>0 and d>0) or (a<0 and b<0 and c<0 and d<0)

    if in_area_1 or in_area_2: # if the point falls in either the left track or the right track, return True.
        return True
    else: # else, return False.
        return False