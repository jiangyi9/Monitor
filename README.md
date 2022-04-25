# Introduction

This is my Interdisciplinary project: to implement a monitoring system using camera footage and Lidars. I use Python as the main developing language.

The goal of the monitoring system is to detect the position of goods (represented as cubes) in the context of a mock, Web of Things compliant industrial system, and propagate gained information to the system controller to allow for self-correcting behavior.

The concrete tasks are: 

- Research techniques and algorithms for detecting objects using image processing techniques and Lidars.
- Getting familiar with the used machinery and devices.
- Development and deployment of the monitoring system.
- Stress testing the developed monitoring system.
- Documentation of the system.



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





## Detect rectangles, identify their colors and locations

We have read the video. Each frame of the video can be seen as a image.

```
cap = cv2.VideoCapture(0) # load the PC webcam
ret, image = cap.read() # ret is a flag
```





