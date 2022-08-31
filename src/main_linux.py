from pickle import TRUE
import cv2
import numpy as np

# from PIL import ImageGrab
import pyscreenshot as ImageGrab
import sys
import keyboard
pic_grab_path = "/home/jelly/Desktop/Monitor/pic.png"
pic_undistorted_path = "/home/jelly/Desktop/Monitor/img_undistorted.png"
pic_detected_path = "/home/jelly/Desktop/Monitor/image_detection.png"
keyboard_flag = 0

def get_screenshot():
    pic = ImageGrab.grab()
    pic.save(pic_grab_path)


def abc(x):
    a = keyboard.KeyboardEvent('down', 28, 'enter')
    #按键事件a为按下enter键，第二个参数如果不知道每个按键的值就随便写，
    #如果想知道按键的值可以用hook绑定所有事件后，输出x.scan_code即可
    b = keyboard.KeyboardEvent('down', 25, 'p')
    c = keyboard.KeyboardEvent('down', 16, 'q')
    
    if x.event_type == 'down' and x.name == b.name:
        print("你按下了p键")

        # get_screenshot()

        frame = cv2.imread(pic_grab_path)
        cv2.imwrite(pic_undistorted_path, undistort(frame))

        detect()



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




def detect():
    font = cv2.FONT_HERSHEY_SIMPLEX

    # hsv
    lower_red = np.array([0, 100, 150])       # define lower bound of "red"
    higher_red = np.array([10, 255, 255])    # define higher bound of "red"
    lower_yellow = np.array([22, 80, 100])   # define lower bound of "yellow"
    higher_yellow = np.array([33, 130, 255])  # define higher bound of "yellow"
    lower_blue = np.array([90,80,150])       # define lower bound of "blue"
    higher_blue = np.array([140,240,255])    # define higher bound of "blue"
    lower_green = np.array([35,43,46])      # define lower bound of "green"
    higher_green = np.array([77,255,255])   # define higher bound of "green"

    cap = cv2.VideoCapture(0)

    point_list = [] # global point list
    yellow_point_list = [] # yellow point list
    red_point_list = [] # red point list
    blue_point_list = [] # blue point list
    green_point_list = [] # green point list

# while True:
    # ret, image = cap.read()

    image = cv2.imread(pic_undistorted_path)
    # image = ImageGrab.grab(bbox=(100, 100, 580, 400))
    # image = np.array(image)
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # transfer color space from BGR to RGB
    # image = cv2.resize(image, dsize=(1000, 600)) # set the window in a fixed size (648, 486).


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
        if (area < 2):#小于2000就跳过
            continue
        box = cv2.boxPoints(rect) #  获取最小外接矩形的4个顶点坐标
        box = np.int0(box)#取整
        cx = int(rect[0][0])#获取中心点x坐标
        cy = int(rect[0][1])
        point_list.append(cx)
        point_list.append(cy)
        red_point_list.append(cx)
        red_point_list.append(cy)
        # print(rect[2])#打印旋转角度
        # image = cv2.drawContours(image, [box], 0, (0, 0, 255), 3)#画旋转方框

        #image = cv2.circle(image,(cx,cy),4,(0, 0, 255),3)
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(0, 0, 255),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(0, 0, 255),2)
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 将检测到的颜色框起来
        cv2.putText(image, 'red', (x, y - 5), font, 0.7, (0, 0, 255), 2)

    for cnt in cnts2:#blue
        (x, y, w, h) = cv2.boundingRect(cnt)  # 该函数返回矩阵四个点
        rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        area = cv2.contourArea(cnt)#获得blob的面积
        if (area < 2):#小于200就跳过
            continue
        box = cv2.boxPoints(rect) #  获取最小外接矩形的4个顶点坐标
        box = np.int0(box) #取整
        cx = int(rect[0][0]) #获取中心点x坐标
        cy = int(rect[0][1])
        point_list.append(cx)
        point_list.append(cy)
        blue_point_list.append(cx)
        blue_point_list.append(cy)
        # print(rect[2]) #打印旋转角度
        # image = cv2.drawContours(image, [box], 0, (255, 0, 0), 3) #画旋转方框

        #image = cv2.circle(image,(cx,cy),4,(0, 0, 255),3)
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(255, 0, 0),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(255, 0, 0),2)
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 将检测到的颜色框起来
        cv2.putText(image, 'blue', (x, y - 5), font, 0.7, (255, 0, 0), 2)

    for cnt in cnts3:#yellow
        (x, y, w, h) = cv2.boundingRect(cnt)  # 该函数返回矩阵四个点
        rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        area = cv2.contourArea(cnt)#获得blob的面积
        if (area < 0):#小于2000就跳过
            continue
        box = cv2.boxPoints(rect) #  获取最小外接矩形的4个顶点坐标
        box = np.int0(box)#取整
        cx = int(rect[0][0])#获取中心点x坐标
        cy = int(rect[0][1])
        point_list.append(cx)
        point_list.append(cy)
        yellow_point_list.append(cx)
        yellow_point_list.append(cy)
        # print(rect[2])#打印旋转角度

        cnt_len = cv2.arcLength(cnt[0], True)
        cnt = cv2.approxPolyDP(cnt[0], 0.02*cnt_len, True)
        if len(cnt) >= 4:
            image = cv2.drawContours(image, [cnt], -1, (255, 255, 0), 3 )
        
        # image = cv2.drawContours(image, [box], 0, (0, 255, 255), 3)#画旋转方框

        #image = cv2.circle(image,(cx,cy),4,(0, 0, 255),3)
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(0, 255, 255),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(0, 255, 255),2)
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)  # 将检测到的颜色框起来
        cv2.putText(image, 'yellow', (x, y - 5), font, 0.5, (0, 255, 255), 2)

    for cnt in cnts4:#green
        (x, y, w, h) = cv2.boundingRect(cnt)  # 该函数返回矩阵四个点
        rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        area = cv2.contourArea(cnt)#获得blob的面积
        if (area < 0):#小于2000就跳过
            continue
        box = cv2.boxPoints(rect) #  获取最小外接矩形的4个顶点坐标
        box = np.int0(box)#取整
        cx = int(rect[0][0])#获取中心点x坐标
        cy = int(rect[0][1])
        point_list.append(cx)
        point_list.append(cy)
        green_point_list.append(cx)
        green_point_list.append(cy)
        # print(cx, cy)
        # print(rect[2])#打印旋转角度
        # image = cv2.drawContours(image, [box], 0, (0, 255, 0), 3)#画旋转方框

        # image = cv2.circle(image,(cx,cy),4,(0, 0, 255),3)
        image = cv2.line(image,(cx+2,cy),(cx-2,cy),(0, 255, 0),2)
        image = cv2.line(image,(cx,cy+2),(cx,cy-2),(0, 255, 0),2)
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 将检测到的颜色框起来
        cv2.putText(image, 'green', (x, y - 5), font, 0.7, (0, 255, 0), 2)

    # cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    # cv2.imshow("image", image)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     # cap.release()
    #     cv2.destroyAllWindows()
    #     break
    cv2.imwrite(pic_detected_path, image)
    point_array = np.array(point_list)
    point_array = point_array.reshape(-1,2)
    red_point_array = np.array(red_point_list)
    red_point_array = red_point_array.reshape(-1,2)
    blue_point_array = np.array(blue_point_list)
    blue_point_array = blue_point_array.reshape(-1,2)
    yellow_point_array = np.array(yellow_point_list)
    yellow_point_array = yellow_point_array.reshape(-1,2)
    green_point_array = np.array(green_point_list)
    green_point_array = green_point_array.reshape(-1,2)
    print(green_point_array[np.lexsort(green_point_array.T)])


if __name__=="__main__":  

    keyboard.hook(abc)
    while True:
        input = keyboard.read_key()
        if input=='q':
            break