import cv2
import time
from undistortion import undistort
from detection import detect

pic_grab_path = "./img.png"
pic_undistorted_path = "./img_undistorted.png"
pic_detected_path = "./img_detection.png"


if __name__=="__main__":  

    time.sleep(1)

    image = cv2.imread(pic_grab_path)
    image = undistort(image)
    cv2.imwrite(pic_undistorted_path, image)

    image = detect(image)

    cv2.imwrite(pic_detected_path, image)

    print("demo runs successfully")

    time.sleep(1)