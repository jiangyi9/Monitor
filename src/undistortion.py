import numpy as np
import cv2

# camera calibration using zhang's method
def undistort(image):

    # define parameters (get from MATLAB using chessboard)
    fx = 1688.6581
    fy = 1688.8659
    cx = 998.322
    cy = 500
    k1, k2, p1, p2, k3 = -0.3338, 0.1463, 0.0, 0.0, 0.0
 
    # conversion matrix of camera coordinate system to pixel coordinate system
    k = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ])

    # distortion factor
    d = np.array([
        k1, k2, p1, p2, k3
    ])
    
    h, w = image.shape[:2]
    mapx, mapy = cv2.initUndistortRectifyMap(k, d, None, k, (w, h), 5)
    return cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)