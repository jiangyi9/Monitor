import cv2
import time
import undistortion
import detection

pic_grab_path = "./pic.png"
pic_undistorted_path = "./img_undistorted.png"
pic_detected_path = "./image_detection.png"

# # get the scrrenshot of the camera
# def get_screenshot():
#     pic = ImageGrab.grab()
#     pic.save(pic_grab_path)

if __name__=="__main__":  

    # get_screenshot()

    time.sleep(1)

    image = cv2.imread(pic_grab_path)
    image = undistortion.undistort(image)
    cv2.imwrite(pic_undistorted_path, image)

    image = detection.detect(image)

    cv2.imwrite(pic_detected_path, image)

    print("demo runs successfully")

    time.sleep(1)