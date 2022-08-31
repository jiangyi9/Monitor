# Introduction

This is my Interdisciplinary project: to implement a monitoring system using camera footage and Lidars. I use Python as the main developing language.

The goal of the monitoring system is to detect the position of goods (represented as cubes) in the context of a mock, Web of Things compliant industrial system, and propagate gained information to the system controller to allow for self-correcting behavior.

The concrete tasks are: 

- Research techniques and algorithms for detecting objects using image processing techniques and Lidars.
- Getting familiar with the used machinery and devices.
- Development and deployment of the monitoring system.
- Stress testing the developed monitoring system.
- Documentation of the system.



## Questions to be solved (will update periodically)

1. The RpLidar uses (angle, distance) pair to present the location of a point, which is different from the webcam's (x, y) format. Can I directly export the (angle, distance) pair of each cubes? Or do I need to transform them to (x, y) format (this would be very hard, because I should first know the exact location of the RpLidar)? （Yes, we should transform it to (x, y) format)

1. Where should I put the RpLidar? Is it a fixed place? I want to know this because the design of monitoring system depends largely on the location of RpLidar. (depend on myself)

1. RpLidar can only detect the edges (or say: the closest shelter), so if 2 cubes locate at the same angle (one closer, one farther), then RpLidar cannot detect the farther one. So I don't need to detect the farther one, right? (Yes)

1. It could be very challenging to deal with the case that 2 cubes are together. (partly because RpLidar cannot detect the color of the cube). (simply dismiss this case, because it's very edge case)

1. If I put the RpLidar on the desk, I'm not sure whether the RpLidar can detect cubes on the belt (because these cubes are higher than the desk and the RpLidar). (事实上这个location数据是三维的。所以只要把在履带上的cube加一个height就行了)

1. A global question: how does the webcam and the RpLidar work together in the monitor system? Are they two invidual parts? （最终目标：发现桌面上的所有cube。webcam起主要作用，RpLidar起次要作用。）

   

   

















## Access the video stream (not be tested yet)

OpenCV provides a class to help us access video files, video streams, and cameras. We assume the RTSP is used to transmit the video, the example address is: rtsp://192.168.1.64/1. HTTP can also be used if required.

```
capture = cv2.VideoCapture('rtsp://192.168.1.64/1') 
```

For camera with IP address, we should add its username and password as parameters.

```
capture = cv2.VideoCapture('rtsp://[username]:
[password]@192.168.1.64/1')
```

A full example to access the video stream is below. (see [here](https://cloud.tencent.com/developer/article/1697128))

```
import cv2

#print("Before URL")
cap = cv2.VideoCapture('rtsp://admin:123456@192.168.1.216/H264?ch=1&subtype=0')
#print("After URL")

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv2.imshow("Capturing",frame)
    #print('Running..')

    # press 'q' to break the 'while' loop. 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and destory the captured stream. This is important because it may cause significant system delay if someone doesn't destroy the window.
cap.release()
cv2.destroyAllWindows()
```





## Detect rectangles, identify their colors and locations (completed)

We have read the video. Each frame of the video can be seen as an image.

```
cap = cv2.VideoCapture(0) # load the PC webcam
ret, image = cap.read() # ret is a flag
```

Now, we want to detect all <font color='red'>red cubes</font> in the image.

Note that OpenCV-Python uses BGR color space, so we should transfer it to HSV color space.

```
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # img_hsv is an image that stores HSV color information.
img_erode = cv2.erode(img_hsv, None, iterations=2) # erode the image to help detect edges better.
```

Next, we get the <font color='red'>red</font> areas (i.e. get the red masks) in the image. We define <font color='red'>red</font> by limiting its higher_bound and lower_bound (in HSV color space). Then we use cv2.inRange() to filter the <font color='red'>red</font> color. For cv2.inRange(), the area in img_hsv that is between higher_bound and lower_bound is marked as white (0), and others marked as black (255). (see more about cv2.inRange() [here](https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html))

Afterwards, we use cv2.medianBlur() to blur the masked image. The goal of this step is to smooth the image, so some noisy points can be eliminated. Note that there are multiple blur methods to be select. (see [here](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html))

Then, we detect edges of <font color='red'>red</font> masks using cv2.findContours(). Each contour is stored as a vector of points, and cnts1 stores all edge information. (see more about cv2.findContours [here](https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html))

```
lower_red = np.array([156, 43, 46])       # lower bound of "red"
higher_red = np.array([180, 255, 255])    # higher bound of "red"

mask_red = cv2.inRange(img_erode, lower_red, higher_red)  # get red masks
mask_red = cv2.medianBlur(mask_red, 7)

cnts1, hierarchy1 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # detect, then store the edge of each red area in cnts1.
```

Now we get the edges of red masks. Next draw the edges of each red area as a rectangle.

```
for cnt in cnts1: #red (BGR color space here)
        (x, y, w, h) = cv2.boundingRect(cnt)  # get 4 points of cnt as x,y,w,h.
        rect = cv2.minAreaRect(cnt) # get the information of the Smallest External Rectangle in rect. rect is a 1*3 vector: (center point, width and height, rotation angle).
        area = cv2.contourArea(cnt) # get the area of the rectangle
        if (area < 2000): # if the area is too small, we jujst ignore it.
            continue
        box = cv2.boxPoints(rect) #  get 4 vertex coordinates of the Smallest External Rectangle in box.
        box = np.int0(box) # Rounding up
        
        # get the center point coordinate of the rectangle
        cx = int(rect[0][0])
        cy = int(rect[0][1])
        # print(rect[2]) # show the rotation angle
        image = cv2.drawContours(image, [box], 0, (0, 0, 255), 3) # draw the edge.

        # draw the center point of the rectangle
        image = cv2.line(image,(cx+10,cy),(cx-10,cy),(0, 0, 255),2)
        image = cv2.line(image,(cx,cy+10),(cx,cy-10),(0, 0, 255),2)
        
        # show the color word.
        cv2.putText(image, 'red', (x, y - 5), font, 0.7, (0, 0, 255), 2)
```





1. Do I need to <font color='red'>track</font> objects by ID (i.e. when a new cubes appears in the webcam, we should give it a unique ID. The system should track each cube by ID. In this case, we see each cube as an OBJECT, with attributes like ID, color, location, etc.. The cube ID will not change only if the cube leaves the screen and then re-enter the screen) ? 

   Or simply <font color='red'>detect</font> objects by color and location (in each time point, the system only needs to know e.g. there are 2 blue cubes at points (120, 400) and (300, 50), and a red cube at point(200, 200). The system doesn't care about the exact IDENTITY of cube) ?

   A: the second one (simply detect)

2. Will the webcam always places right above the cubes (i.e. the webcam can only see the upper side of cubes, so this is a <font color='red'>2D dection task</font>)?

   Or this is a <font color='red'>3D dection task</font>? (approx. 2d)

3. <font color='red'>How frequent</font> the cube location information should be updated and transmitted? Frame by frame? Or per second? (the time that I enter the button, it's only one frame)

4. Do you have the RTSP / HTTP / WSS address of the camera? (maybe yes)

5. About the upper-left cubes, do I need to detect them? Or can I remove them from the webcam? (we don't consider these cubes)

6. About Web of Things: Is there any tutorials that can tell me how to export location data into the Web of Things system?
