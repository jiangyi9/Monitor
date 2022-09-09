import cv2
import numpy as np
import points as pts

def draw_points(image, x, y):
    image = cv2.line(image,(x+3,y),(x-3,y),(255, 255, 255),10)
    image = cv2.line(image,(x,y+3),(x,y-3),(255, 255, 255),10)

def draw_masks(image):
    # draw the mask of the left track
    pts_1 = np.array([[pts.left_track_LB_x, pts.left_track_LB_y],
                        [pts.left_track_LT_x, pts.left_track_LT_y],
                        [pts.left_track_RT_x, pts.left_track_RT_y],
                        [pts.left_track_RB_x, pts.left_track_RB_y]], np.int32)
    pts_1 = pts_1.reshape((-1, 1, 2))
    zeros = np.zeros((image.shape), dtype=np.uint8)
    mask_1 = cv2.fillConvexPoly(zeros, pts_1, (255,0,255))

    # draw the mask of the right track
    pts_2 = np.array([[pts.right_track_LB_x, pts.right_track_LB_y],
                        [pts.right_track_LT_x, pts.right_track_LT_y],
                        [pts.right_track_RT_x, pts.right_track_RT_y],
                        [pts.right_track_RB_x, pts.right_track_RB_y]], np.int32)
    pts_2 = pts_2.reshape((-1, 1, 2))
    mask_2 = cv2.fillConvexPoly(zeros, pts_2, (255,0,255))
    image = 0.3*mask_1 + 0.3*mask_2 + + image

    # draw the mask of the right track
    pts_3 = np.array([[pts.left_track_upper_LB_x, pts.left_track_upper_LB_y],
                        [pts.left_track_upper_LT_x, pts.left_track_upper_LT_y],
                        [pts.left_track_upper_RT_x, pts.left_track_upper_RT_y],
                        [pts.left_track_upper_RB_x, pts.left_track_upper_RB_y]], np.int32)
    pts_3 = pts_3.reshape((-1, 1, 2))
    mask_3 = cv2.fillConvexPoly(zeros, pts_3, (255,255,255))

    # draw the mask of the right track
    pts_4 = np.array([[pts.right_track_upper_LB_x, pts.right_track_upper_LB_y],
                        [pts.right_track_upper_LT_x, pts.right_track_upper_LT_y],
                        [pts.right_track_upper_RT_x, pts.right_track_upper_RT_y],
                        [pts.right_track_upper_RB_x, pts.right_track_upper_RB_y]], np.int32)
    pts_4 = pts_4.reshape((-1, 1, 2))
    mask_4 = cv2.fillConvexPoly(zeros, pts_4, (255,255,255))

    image = 0.3*mask_1 + 0.3*mask_2 + 0.05*mask_3 + 0.05*mask_4 + image

    # # draw the mask of tape A
    # pts_3 = np.array([[pts.tape_A_4_x, pts.tape_A_4_y],[pts.tape_A_1_x, pts.tape_A_1_y],[pts.tape_A_2_x, pts.tape_A_2_y],[pts.tape_A_3_x, pts.tape_A_3_y]], np.int32)
    # pts_3 = pts_3.reshape((-1, 1, 2))
    # mask_3 = cv2.fillConvexPoly(zeros, pts_3, (255,255,255))

    return image