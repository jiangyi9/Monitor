import numpy as np
import cv2
import points as pts
from cubeCorrection import correct_location
from converting import convert_array, convert_pix_to_mm
from assignArms import assignArms
from drawing import draw_areas, draw_point
from inInvalidAreas import inInvalidAreas
from isOnTrack import isOnTrack


# define the height of the desk (LOW) and the track (HIGH)
LOW = 25
HIGH = 105


def detect(image):

    font = cv2.FONT_HERSHEY_SIMPLEX

    # define hsv bounds
    lower_red = np.array([0, 100, 150])       # define lower bound of "red"
    higher_red = np.array([10, 255, 255])    # define higher bound of "red"
    lower_yellow = np.array([22, 80, 150])   # define lower bound of "yellow"
    higher_yellow = np.array([33, 130, 255])  # define higher bound of "yellow"
    lower_blue = np.array([90,80,150])       # define lower bound of "blue"
    higher_blue = np.array([140,240,255])    # define higher bound of "blue"
    lower_green = np.array([35,80,150])      # define lower bound of "green"
    higher_green = np.array([77,255,255])   # define higher bound of "green"

    # create a point list to store all od the detected points
    point_list = [] 

    # set the window to a fixed size (1920, 1080).
    image = cv2.resize(image, dsize=(1920, 1080)) 

    # transfer the color from BGR to HSV 
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # erode the image
    img_erode = cv2.erode(img_hsv, None, iterations=2)

    # get the red areas, blur them, then find the contours of each area.
    mask_red = cv2.inRange(img_erode, lower_red, higher_red)
    mask_red = cv2.medianBlur(mask_red, 7)
    cnts_red, hierarchy1 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # get the blue areas, blur them, then find the contours of each area.
    mask_blue = cv2.inRange(img_erode, lower_blue, higher_blue)
    mask_blue = cv2.medianBlur(mask_blue, 7)
    cnts_blue, hierarchy2 = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # get the yellow areas, blur them, then find the contours of each area.
    mask_yellow = cv2.inRange(img_erode, lower_yellow, higher_yellow)
    mask_yellow = cv2.medianBlur(mask_yellow, 7)
    cnts_yellow, hierarchy3 = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # get the green areas, blur them, then find the contours of each area.
    mask_green = cv2.inRange(img_erode, lower_green, higher_green)
    mask_green = cv2.medianBlur(mask_green, 7)
    cnts_green, hierarchy4 = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    image = image.copy()

    # for red areas
    for cnt in cnts_red:

        # draw an approximate rectangle around the red area
        (x, y, w, h) = cv2.boundingRect(cnt)  

        # find the minimum bounding rectangle of the red area
        rect = cv2.minAreaRect(cnt) 

        # get the size of the rectangle
        area = cv2.contourArea(cnt) 

        # if the size of the area is too small, we just ignore it.
        if (area < 100): 
            continue

        # get the 4 corners of the minimum bounding rectangle, and round it to (int).
        box = cv2.boxPoints(rect) 
        box = np.int0(box) 

        # get the x and y coordinate of the center point.
        cx = int(rect[0][0]) 
        cy = int(rect[0][1])

        # slightly correct the location of the center point.
        [cx,cy] = correct_location([cx,cy]) 

        # if the point falls in tapes, we exclude it.
        if(inInvalidAreas([cx,cy])): 
            continue

        # add cx and cy to the point_list.
        point_list.append(cx)
        point_list.append(cy)

        # if the center point falls on the track, add the HIGH as its height.
        if(isOnTrack([cx,cy])):
            point_list.append(HIGH)
        else: # otherwise, add the LOW as its height.
            point_list.append(LOW)
        
        # get the rotation angle of the rectangle, and add it to the point_list.
        rotation = int(rect[2])
        point_list.append(rotation)

        # draw the center point of the rectangle, and put the text "red".
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(0, 0, 255),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(0, 0, 255),2)
        cv2.putText(image, 'red', (x, y - 5), font, 0.7, (0, 0, 255), 2)


    # for blue areas
    for cnt in cnts_blue:

        # draw an approximate rectangle around the blue area
        (x, y, w, h) = cv2.boundingRect(cnt)

        # find the minimum bounding rectangle of the blue area
        rect = cv2.minAreaRect(cnt)

        # get the size of the rectangle
        area = cv2.contourArea(cnt)

        # if the size of the area is too small, we just ignore it.
        if (area < 100):
            continue

        # get the 4 corners of the minimum bounding rectangle, and round it to (int).
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # get the x and y coordinate of the center point.
        cx = int(rect[0][0])
        cy = int(rect[0][1])

        # slightly correct the location of the center point.
        [cx,cy] = correct_location([cx,cy])

        # if the point falls in tapes, we exclude it.
        if(inInvalidAreas([cx,cy])):
            continue

        # add cx and cy to the point_list.
        point_list.append(cx)
        point_list.append(cy)

        # if the center point falls on the track, add the HIGH as its height.
        if(isOnTrack([cx,cy])):
            point_list.append(HIGH)
        else: # otherwise, add the LOW as its height.
            point_list.append(LOW)

        # get the rotation angle of the rectangle, and add it to the point_list.
        rotation = int(rect[2])
        point_list.append(rotation)

        # draw the center point of the rectangle, and put the text "red".
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(255, 0, 0),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(255, 0, 0),2)
        cv2.putText(image, 'blue', (x, y - 5), font, 0.7, (255, 0, 0), 2)


    # for yellow areas
    for cnt in cnts_yellow:

        # draw an approximate rectangle around the yellow area
        (x, y, w, h) = cv2.boundingRect(cnt)

        # find the minimum bounding rectangle of the yellow area
        rect = cv2.minAreaRect(cnt)

        # get the size of the rectangle
        area = cv2.contourArea(cnt)

        # if the size of the area is too small, we just ignore it.
        if (area < 100):#小于2000就跳过
            continue

        # get the 4 corners of the minimum bounding rectangle, and round it to (int).
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # get the x and y coordinate of the center point.
        cx = int(rect[0][0])
        cy = int(rect[0][1])

        # slightly correct the location of the center point.
        [cx,cy] = correct_location([cx,cy])

        # if the point falls in tapes, we exclude it.
        if(inInvalidAreas([cx,cy])): 
            continue

        # add cx and cy to the point_list.
        point_list.append(cx)
        point_list.append(cy)

        # if the center point falls on the track, add the HIGH as its height.
        if(isOnTrack([cx,cy])):
            point_list.append(HIGH)
        else: # otherwise, add the LOW as its height.
            point_list.append(LOW)
        
        # get the rotation angle of the rectangle, and add it to the point_list.
        rotation = int(rect[2])
        point_list.append(rotation)

        # draw the center point of the rectangle, and put the text "red".
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(0, 255, 255),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(0, 255, 255),2)
        cv2.putText(image, 'yellow', (x, y - 5), font, 0.5, (0, 255, 255), 2)


    # for green areas
    for cnt in cnts_green:

        # draw an approximate rectangle around the green area
        (x, y, w, h) = cv2.boundingRect(cnt)

        # find the minimum bounding rectangle of the green area
        rect = cv2.minAreaRect(cnt)

        # get the size of the rectangle
        area = cv2.contourArea(cnt)

        # if the size of the area is too small, we just ignore it.
        if (area < 100):
            continue

        # get the 4 corners of the minimum bounding rectangle, and round it to (int).
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # get the x and y coordinate of the center point.
        cx = int(rect[0][0])
        cy = int(rect[0][1])

        # slightly correct the location of the center point.
        [cx,cy] = correct_location([cx,cy])

        # if the point falls in tapes, we exclude it.
        if(inInvalidAreas([cx,cy])): 
            continue

        # add cx and cy to the point_list.
        point_list.append(cx)
        point_list.append(cy)

        # if the center point falls on the track, add the HIGH as its height.
        if(isOnTrack([cx,cy])):
            point_list.append(HIGH)
        else: # otherwise, add the LOW as its height.
            point_list.append(LOW)
        
        # get the rotation angle of the rectangle, and add it to the point_list.
        rotation = int(rect[2])
        point_list.append(rotation)

        # draw the center point of the rectangle, and put the text "red".
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(0, 255, 0),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(0, 255, 0),2)
        cv2.putText(image, 'green', (x, y - 5), font, 0.7, (0, 255, 0), 2)

######################     drawing some points/areas for DEBUG starts  #####################

    draw_point(image, pts.camera_center)
    # draw_point(image, pts.left_track_LBPoint)
    # draw_point(image, pts.left_track_LTPoint)
    # draw_point(image, pts.left_track_RTPoint)
    # draw_point(image, pts.left_track_RBPoint)
    # draw_point(image, pts.right_track_LBPoint)
    # draw_point(image, pts.right_track_LTPoint)
    # draw_point(image, pts.right_track_RTPoint)
    # draw_point(image, pts.right_track_RBPoint)

    image = draw_areas(image)

######################     drawing some lines/points for DEBUG ends   #####################

    # convert the point set from list to array
    point_array = convert_array(point_list)

    # print(point_array)

    # assign the points to the respective arms.
    assignArms(point_array)

    return image


