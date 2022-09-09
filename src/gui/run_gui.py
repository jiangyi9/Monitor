import tkinter as tk
import time
import pyscreenshot as ImageGrab
import os

pic_grab_path = "./pic.png"

# 创建Tk对象，Tk代表窗口
root =tk.Tk()
# 让窗口强制置顶
root.wm_attributes('-topmost',1)
# 设置窗口标题
root.title('Monitor')
# 设置窗口大小,位置
root.geometry("180x110+100+800")

# 创建Label对象，第一个参数指定该Label放入root
var=tk.StringVar()

# get the screenshot of the camera
def get_screenshot():
    pic = ImageGrab.grab()
    pic.save(pic_grab_path)

#测试用途
def screenshot_event():
    var.set("Ready to shot...")
    time.sleep(1)
    get_screenshot()
    var.set("Screenshot done!")

def detection_event():
    var.set("Ready to detect...")
    os.system("parallel sh ::: run_docker.sh update_data.sh")
    var.set("Detection done!")

#测试用途
goBtn = tk.Button(text="Screenshot",command=screenshot_event,fg='gray',font=("Romans",16),height=1,width=10)
goBtn.pack()
goBtn = tk.Button(text="Detect",command=detection_event,fg='gray',font=("Romans",16),height=1,width=10)
goBtn.pack()

w =tk.Label(root,textvariable=var,fg='black',font=("Romans",14))
var.set("Monitor is Ready!")
# 调用pack进行布局
w.pack()
 
# 启动主窗口的消息循环
root.mainloop()