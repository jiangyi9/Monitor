import tkinter as tk
import time
import pyscreenshot as ImageGrab
import os

pic_grab_path = "./pic.png"

# create TK object
root =tk.Tk()

# always show the interface
root.wm_attributes('-topmost',1)

# set the title of the interface
root.title('Monitor')
# set the size and location of the interface
root.geometry("180x110+100+800")

var=tk.StringVar()

# get the screenshot of the camera
def get_screenshot():
    pic = ImageGrab.grab()
    pic.save(pic_grab_path)

# screenshot event
def screenshot_event():
    time.sleep(1)
    get_screenshot()
    var.set("Screenshot done!")

# detection event
def detection_event():
    var.set("Ready to detect...")
    os.system("parallel sh ::: run_docker.sh update_data.sh")
    var.set("Detection done!")

# set two buttons
goBtn = tk.Button(text="Screenshot",command=screenshot_event,fg='gray',font=("Romans",16),height=1,width=10)
goBtn.pack()
goBtn = tk.Button(text="Detect",command=detection_event,fg='gray',font=("Romans",16),height=1,width=10)
goBtn.pack()

w =tk.Label(root,textvariable=var,fg='black',font=("Romans",14))
var.set("Monitor is Ready!")
w.pack()
 
# start the loop
root.mainloop()