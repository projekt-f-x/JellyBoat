## print("Hello Jelly Boat World")
import win32api, win32con, time
from pynput.mouse import Button, Controller

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

mouse = Controller()


#while True:
 #try:
  #click(200,200)
  #time.sleep(1)
 #except KeyboardInterrupt:
     #exit()


while True:
 try:
  mouse.position = (200, 200)
  mouse.press(Button.left)
  #time.sleep(2)
  mouse.release(Button.left)
  mouse.position = (500, 200)
  mouse.press(Button.left)
 except KeyboardInterrupt:
     exit()