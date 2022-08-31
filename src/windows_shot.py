# import sys
# import threading
# import time
# import win32clipboard 
# import win32api, win32con  
# from PIL import ImageGrab, Image

# CAPTURE_PNG_URL = 'C:\\Users\\19539\\Desktop\\capture.png'
  
# def on_cap_pic_clicked():#点击截获图片
#     win32clipboard.OpenClipboard()
#     win32clipboard.EmptyClipboard() #清空剪贴板
#     win32clipboard.CloseClipboard()

#     try:
#         win32api.keybd_event(0x5B, 0, 0, 0)    # 0x5B --> left win key 
#         win32api.keybd_event(0x10, 0, 0, 0)    # 0x10 --> SHIFT
#         win32api.keybd_event(0x53, 0, 0, 0)    # 0x53 --> S
#         win32api.keybd_event(0x5B, 0, win32con.KEYEVENTF_KEYUP, 0)    
#         win32api.keybd_event(0x10, 0, win32con.KEYEVENTF_KEYUP, 0)
#         win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)
#     except:
#         print('keyboard event does not successful.')
#         sys.exit(1)
    
#     image = ImageGrab.grabclipboard() # 获取剪贴板文件
#     image.show()   #debug
#     image.save(CAPTURE_PNG_URL)

# def capture_screen():#监听点击，右键重新截取
#     # 考虑先清空剪贴板然后查看剪贴板判断是否结束。1月13日
#     while(True):
#         image = ImageGrab.grabclipboard() # 获取剪贴板文件
#         if image:
#             break
#         else:
#             time.sleep(1)

# on_cap_pic_clicked()
# capture_screen()








# import win32api, win32con, win32gui
# def get_window_pos(name): 
#     name = name
#     handle = win32gui.FindWindow(0, name)
#     #获取窗口句柄
#     if handle == 0: return None
#     else:
#        #返回坐标值和handle
#        return win32gui.GetWindowRect(handle), handle
# (x1, y1, x2, y2), handle = get_window_pos('Remote Lab')
# win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
# # 发送还原最小化窗口的信息
# win32gui.SetForegroundWindow(handle)
# # 设为高亮
# from PIL import Image, ImageGrab
# img_ready = ImageGrab.grab((x1, y1, x2, y2))
# # 截图
# img_ready.show()
# # 展示








import time
import os
from PIL import ImageGrab
import keyboard

def abc(x):
    a = keyboard.KeyboardEvent('down', 28, 'enter')
    #按键事件a为按下enter键，第二个参数如果不知道每个按键的值就随便写，
    #如果想知道按键的值可以用hook绑定所有事件后，输出x.scan_code即可
    
    if x.event_type == 'down' and x.name == a.name:
        print("你按下了enter键")
        os.system(r'E:\\test.bat')
        pic = ImageGrab.grab()
        pic.save('E:\\pic.jpg')
        
        pic.show()
    #当监听的事件为enter键，且是按下的时候

if __name__=="__main__":  
    keyboard.hook(abc)
    # keyboard.hook_key('enter', bcd)
    # recorded = keyboard.record(until='esc')
    keyboard.wait()
    


















