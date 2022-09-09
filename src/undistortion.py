import numpy as np
import cv2

# camera calibration using zhang's method
def undistort(frame):
    fx = 1688.6581
    fy = 1688.8659
    cx = 998.322
    cy = 500
    k1, k2, p1, p2, k3 = -0.3338, 0.1463, 0.0, 0.0, 0.0
 
    # 相机坐标系到像素坐标系的转换矩阵
    k = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ])
    # 畸变系数
    d = np.array([
        k1, k2, p1, p2, k3
    ])
    h, w = frame.shape[:2]
    mapx, mapy = cv2.initUndistortRectifyMap(k, d, None, k, (w, h), 5)
    return cv2.remap(frame, mapx, mapy, cv2.INTER_LINEAR)