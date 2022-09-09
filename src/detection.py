# from pickle import TRUE
# from re import X

from time import time
import numpy as np
import os
import points as pts
import cubeCorrection as cube_correction
import undistortion
import converting
import assigning
import drawing
import tracks

# from PIL import ImageGrab
# import pyscreenshot as ImageGrab
# import sys
import time
import cv2


# define the height of the desk (LOW) and the track (HIGH)
LOW = 25
HIGH = 105


def detect(image):

    font = cv2.FONT_HERSHEY_SIMPLEX

    # hsv
    lower_red = np.array([0, 100, 150])       # define lower bound of "red"
    higher_red = np.array([10, 255, 255])    # define higher bound of "red"
    lower_yellow = np.array([22, 80, 150])   # define lower bound of "yellow"
    higher_yellow = np.array([33, 130, 255])  # define higher bound of "yellow"
    lower_blue = np.array([90,80,150])       # define lower bound of "blue"
    higher_blue = np.array([140,240,255])    # define higher bound of "blue"
    lower_green = np.array([35,43,150])      # define lower bound of "green"
    higher_green = np.array([77,255,255])   # define higher bound of "green"


    point_list = [] # global point list
    yellow_point_list = [] # yellow point list
    red_point_list = [] # red point list
    blue_point_list = [] # blue point list
    green_point_list = [] # green point list

    image = cv2.resize(image, dsize=(1920, 1080)) # set the window in a fixed size (1920, 1080).

    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    img_erode = cv2.erode(img_hsv, None, iterations=2)

    mask_red = cv2.inRange(img_erode, lower_red, higher_red)  # 可以认为是过滤出红色部分，获得红色的掩膜
    mask_red = cv2.medianBlur(mask_red, 7)
    mask_yellow = cv2.inRange(img_erode, lower_yellow, higher_yellow)
    mask_yellow = cv2.medianBlur(mask_yellow, 7)
    mask_blue = cv2.inRange(img_erode, lower_blue, higher_blue)
    mask_blue = cv2.medianBlur(mask_blue, 7)
    mask_green = cv2.inRange(img_erode, lower_green, higher_green)
    mask_green = cv2.medianBlur(mask_green, 7)

    cnts1, hierarchy1 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 轮廓检测 #红色
    cnts2, hierarchy2 = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts3, hierarchy3 = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts4, hierarchy4 = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    image = image.copy()

    for cnt in cnts1:#red                               b g r
        (x, y, w, h) = cv2.boundingRect(cnt)  # 该函数返回矩阵四个点
        rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        area = cv2.contourArea(cnt)#获得blob的面积
        if (area < 100):#小于2000就跳过
            continue
        box = cv2.boxPoints(rect) #  获取最小外接矩形的4个顶点坐标
        box = np.int0(box)#取整
        cx = int(rect[0][0])#获取中心点x坐标
        cy = int(rect[0][1])
        [cx,cy] = cube_correction.correct_location([cx,cy])
        point_list.append(cx)
        point_list.append(cy)
        if(tracks.isOnTrack([cx,cy])):
            point_list.append(HIGH)
        else:
            point_list.append(LOW)
        red_point_list.append(cx)
        red_point_list.append(cy)
        if(tracks.isOnTrack([cx,cy])):
            red_point_list.append(HIGH)
        else:
            red_point_list.append(LOW)
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(0, 0, 255),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(0, 0, 255),2)
        cv2.putText(image, 'red', (x, y - 5), font, 0.7, (0, 0, 255), 2)

    for cnt in cnts2:#blue
        (x, y, w, h) = cv2.boundingRect(cnt)  # 该函数返回矩阵四个点
        rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        area = cv2.contourArea(cnt)#获得blob的面积
        if (area < 100):#小于200就跳过
            continue
        box = cv2.boxPoints(rect) #  获取最小外接矩形的4个顶点坐标
        box = np.int0(box) #取整
        cx = int(rect[0][0]) #获取中心点x坐标
        cy = int(rect[0][1])
        [cx,cy] = cube_correction.correct_location([cx,cy])
        point_list.append(cx)
        point_list.append(cy)
        if(tracks.isOnTrack([cx,cy])):
            point_list.append(HIGH)
        else:
            point_list.append(LOW)
        blue_point_list.append(cx)
        blue_point_list.append(cy)
        if(tracks.isOnTrack([cx,cy])):
            blue_point_list.append(HIGH)
        else:
            blue_point_list.append(LOW)
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(255, 0, 0),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(255, 0, 0),2)
        cv2.putText(image, 'blue', (x, y - 5), font, 0.7, (255, 0, 0), 2)

    for cnt in cnts3:#yellow
        (x, y, w, h) = cv2.boundingRect(cnt)  # 该函数返回矩阵四个点
        rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        area = cv2.contourArea(cnt)#获得blob的面积
        if (area < 100):#小于2000就跳过
            continue
        box = cv2.boxPoints(rect) #  获取最小外接矩形的4个顶点坐标
        box = np.int0(box)#取整
        cx = int(rect[0][0])#获取中心点x坐标
        cy = int(rect[0][1])
        [cx,cy] = cube_correction.correct_location([cx,cy])
        point_list.append(cx)
        point_list.append(cy)
        if(tracks.isOnTrack([cx,cy])):
            point_list.append(HIGH)
        else:
            point_list.append(LOW)
        yellow_point_list.append(cx)
        yellow_point_list.append(cy)
        if(tracks.isOnTrack([cx,cy])):
            yellow_point_list.append(HIGH)
        else:
            yellow_point_list.append(LOW)
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(0, 255, 255),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(0, 255, 255),2)
        cv2.putText(image, 'yellow', (x, y - 5), font, 0.5, (0, 255, 255), 2)

    for cnt in cnts4:#green
        (x, y, w, h) = cv2.boundingRect(cnt)  # 该函数返回矩阵四个点
        rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        area = cv2.contourArea(cnt)#获得blob的面积
        if (area < 100):#小于2000就跳过
            continue
        box = cv2.boxPoints(rect) #  获取最小外接矩形的4个顶点坐标
        box = np.int0(box)#取整
        cx = int(rect[0][0])#获取中心点x坐标
        cy = int(rect[0][1])
        [cx,cy] = cube_correction.correct_location([cx,cy])
        point_list.append(cx)
        point_list.append(cy)
        if(tracks.isOnTrack([cx,cy])):
            point_list.append(HIGH)
        else:
            point_list.append(LOW)
        green_point_list.append(cx)
        green_point_list.append(cy)
        if(tracks.isOnTrack([cx,cy])):
            green_point_list.append(HIGH)
        else:
            green_point_list.append(LOW)
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(0, 255, 0),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(0, 255, 0),2)
        cv2.putText(image, 'green', (x, y - 5), font, 0.7, (0, 255, 0), 2)

######################     draw some lines/points to help debug STARTs    #####################

    drawing.draw_points(image, pts.center_x, pts.center_y)
    # drawing.draw_points(image, pts.left_track_LB_x, pts.left_track_LB_y)
    # drawing.draw_points(image, pts.left_track_LT_x, pts.left_track_LT_y)
    # drawing.draw_points(image, pts.left_track_RT_x, pts.left_track_RT_y)
    # drawing.draw_points(image, pts.left_track_RB_x, pts.left_track_RB_y)
    # drawing.draw_points(image, pts.right_track_LB_x, pts.right_track_LB_y)
    # drawing.draw_points(image, pts.right_track_LT_x, pts.right_track_LT_y)
    # drawing.draw_points(image, pts.right_track_RT_x, pts.right_track_RT_y)
    # drawing.draw_points(image, pts.right_track_RB_x, pts.right_track_RB_y)

    image = drawing.draw_masks(image)

######################     draw some lines/points to help debug ENDs     #####################


    point_array = converting.convert_array(point_list)
    red_point_array = converting.convert_array(red_point_list)
    blue_point_array = converting.convert_array(blue_point_list)
    yellow_point_array = converting.convert_array(yellow_point_list)
    green_point_array = converting.convert_array(green_point_list)

    print(point_array)

    # print(green_point_array)
    # for x in green_point_array:
    #     print(x[1])

    # print(Tracks.isOnTrack([1700,600]))
    # print(point_array)
    assigning.assign_arm(point_array)

    return image


