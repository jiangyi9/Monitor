import cv2
import time
import undistortion
import detection

pic_grab_path = "./pic.png"
pic_undistorted_path = "./img_undistorted.png"
pic_detected_path = "./image_detection.png"


if __name__=="__main__":  

    time.sleep(1)

    image = cv2.imread(pic_grab_path)
    image = undistortion.undistort(image)
    cv2.imwrite(pic_undistorted_path, image)

    image = detection.detect(image)

    cv2.imwrite(pic_detected_path, image)

    print("demo runs successfully")

    time.sleep(1)