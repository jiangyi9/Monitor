import cv2
import numpy as np
import points as pts
import assignArms

# get the maximum range of arms
MAX_RANGE_OF_FIXED_ARM = assignArms.MAX_RANGE_OF_FIXED_ARM
MAX_RANGE_OF_MOVING_ARM = assignArms.MAX_RANGE_OF_MOVING_ARM

def draw_point(image, testPoint):
    image = cv2.line(image,(testPoint[0]+3,testPoint[1]),(testPoint[0]-3,testPoint[1]),(255, 255, 255),10)
    image = cv2.line(image,(testPoint[0],testPoint[1]+3),(testPoint[0],testPoint[1]-3),(255, 255, 255),10)

def draw_areas(image):

    zeros = np.zeros((image.shape), dtype=np.uint8)
    
    # draw the mask of the left track
    pts_1 = np.array([[pts.left_track_LBPoint[0], pts.left_track_LBPoint[1]],
                        [pts.left_track_LTPoint[0], pts.left_track_LTPoint[1]],
                        [pts.left_track_RTPoint[0], pts.left_track_RTPoint[1]],
                        [pts.left_track_RBPoint[0], pts.left_track_RBPoint[1]]], np.int32)
    pts_1 = pts_1.reshape((-1, 1, 2))
    mask_1 = cv2.fillConvexPoly(zeros, pts_1, (255,0,255))

    # draw the mask of the right track
    pts_2 = np.array([[pts.right_track_LBPoint[0], pts.right_track_LBPoint[1]],
                        [pts.right_track_LTPoint[0], pts.right_track_LTPoint[1]],
                        [pts.right_track_RTPoint[0], pts.right_track_RTPoint[1]],
                        [pts.right_track_RBPoint[0], pts.right_track_RBPoint[1]]], np.int32)
    pts_2 = pts_2.reshape((-1, 1, 2))
    mask_2 = cv2.fillConvexPoly(zeros, pts_2, (255,0,255))

    # draw the mask of the left track upper area
    pts_3 = np.array([[pts.left_track_upper_LBPoint[0], pts.left_track_upper_LBPoint[1]],
                        [pts.left_track_upper_LTPoint[0], pts.left_track_upper_LTPoint[1]],
                        [pts.left_track_upper_RTPoint[0], pts.left_track_upper_RTPoint[1]],
                        [pts.left_track_upper_RBPoint[0], pts.left_track_upper_RBPoint[1]]], np.int32)
    pts_3 = pts_3.reshape((-1, 1, 2))
    mask_3 = cv2.fillConvexPoly(zeros, pts_3, (255,255,0))

    # draw the mask of the right track upper area
    pts_4 = np.array([[pts.right_track_upper_LBPoint[0], pts.right_track_upper_LBPoint[1]],
                        [pts.right_track_upper_LTPoint[0], pts.right_track_upper_LTPoint[1]],
                        [pts.right_track_upper_RTPoint[0], pts.right_track_upper_RTPoint[1]],
                        [pts.right_track_upper_RBPoint[0], pts.right_track_upper_RBPoint[1]]], np.int32)
    pts_4 = pts_4.reshape((-1, 1, 2))
    mask_4 = cv2.fillConvexPoly(zeros, pts_4, (255,255,0))

    # draw the mask of tape A
    pts_5 = np.array([[pts.tape_A_LBPoint[0], pts.tape_A_LBPoint[1]],
                        [pts.tape_A_LTPoint[0], pts.tape_A_LTPoint[1]],
                        [pts.tape_A_RTPoint[0], pts.tape_A_RTPoint[1]],
                        [pts.tape_A_RBPoint[0], pts.tape_A_RBPoint[1]]], np.int32)
    pts_5 = pts_5.reshape((-1, 1, 2))
    mask_5 = cv2.fillConvexPoly(zeros, pts_5, (255,255,255))

    # draw the mask of tape B
    pts_6 = np.array([[pts.tape_B_LBPoint[0], pts.tape_B_LBPoint[1]],
                        [pts.tape_B_LTPoint[0], pts.tape_B_LTPoint[1]],
                        [pts.tape_B_RTPoint[0], pts.tape_B_RTPoint[1]],
                        [pts.tape_B_RBPoint[0], pts.tape_B_RBPoint[1]]], np.int32)
    pts_6 = pts_6.reshape((-1, 1, 2))
    mask_6 = cv2.fillConvexPoly(zeros, pts_6, (255,255,255))

    # draw the mask of tape C
    pts_7 = np.array([[pts.tape_C_LBPoint[0], pts.tape_C_LBPoint[1]],
                        [pts.tape_C_LTPoint[0], pts.tape_C_LTPoint[1]],
                        [pts.tape_C_RTPoint[0], pts.tape_C_RTPoint[1]],
                        [pts.tape_C_RBPoint[0], pts.tape_C_RBPoint[1]]], np.int32)
    pts_7 = pts_7.reshape((-1, 1, 2))
    mask_7 = cv2.fillConvexPoly(zeros, pts_7, (255,255,255))

    # draw the mask of tape D
    pts_8 = np.array([[pts.tape_D_LBPoint[0], pts.tape_D_LBPoint[1]],
                        [pts.tape_D_LTPoint[0], pts.tape_D_LTPoint[1]],
                        [pts.tape_D_RTPoint[0], pts.tape_D_RTPoint[1]],
                        [pts.tape_D_RBPoint[0], pts.tape_D_RBPoint[1]]], np.int32)
    pts_8 = pts_8.reshape((-1, 1, 2))
    mask_8 = cv2.fillConvexPoly(zeros, pts_8, (255,255,255))

    # draw the mask of tape E
    pts_9 = np.array([[pts.tape_E_LBPoint[0], pts.tape_E_LBPoint[1]],
                        [pts.tape_E_LTPoint[0], pts.tape_E_LTPoint[1]],
                        [pts.tape_E_RTPoint[0], pts.tape_E_RTPoint[1]],
                        [pts.tape_E_RBPoint[0], pts.tape_E_RBPoint[1]]], np.int32)
    pts_9 = pts_9.reshape((-1, 1, 2))
    mask_9 = cv2.fillConvexPoly(zeros, pts_9, (255,255,255))

    # draw the mask of tape F
    pts_10 = np.array([[pts.tape_F_LBPoint[0], pts.tape_F_LBPoint[1]],
                        [pts.tape_F_LTPoint[0], pts.tape_F_LTPoint[1]],
                        [pts.tape_F_RTPoint[0], pts.tape_F_RTPoint[1]],
                        [pts.tape_F_RBPoint[0], pts.tape_F_RBPoint[1]]], np.int32)
    pts_10 = pts_10.reshape((-1, 1, 2))
    mask_10 = cv2.fillConvexPoly(zeros, pts_10, (255,255,255))

    # draw the working range of the moving arm
    cv2.ellipse(image,(pts.moving_arm[0],pts.moving_arm[1]),
                (MAX_RANGE_OF_MOVING_ARM,MAX_RANGE_OF_MOVING_ARM),0,0,180,(255,111,131),4)
    cv2.line(image, (pts.moving_arm[0]-MAX_RANGE_OF_MOVING_ARM,pts.moving_arm[1]), 
                    (pts.moving_arm[0]+MAX_RANGE_OF_MOVING_ARM,pts.moving_arm[1]), 
                    (255,111,131), 4, 4)
    
    # draw the original point of the moving arm (it is out of the scope of the image)
    draw_point(image, [pts.moving_arm[0],pts.moving_arm[1]])

    # draw the working range of the fixed arm
    cv2.ellipse(image,(pts.fixed_arm[0],pts.fixed_arm[1]),
                (MAX_RANGE_OF_FIXED_ARM,MAX_RANGE_OF_FIXED_ARM),0,0,180,(0,127,255),4)
    cv2.line(image, (pts.fixed_arm[0]-MAX_RANGE_OF_FIXED_ARM,pts.fixed_arm[1]), 
                    (pts.fixed_arm[0]+MAX_RANGE_OF_FIXED_ARM,pts.fixed_arm[1]), 
                    (0,127,255), 4, 4)

    # draw the original point of the fixed arm
    draw_point(image, [pts.fixed_arm[0],pts.fixed_arm[1]])

    image = 0.6*mask_10 + image

    return image