from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(1.5)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
  
    try:
        a1 = pixel(255,450)[0]
    except:
        a1 = pixel(255,450)[0]
    
    try:
        a2 = pixel(330,450)[0]
    except:
        a2 = pixel(330,450)[0]

    try:
        a3 = pixel(397,450)[0]
    except:
        a3 = pixel(397,450)[0]

    try:
        a4 = pixel(458,450)[0]
    except:
        a4 = pixel(458,450)[0]

    if a1 == 0:
        click(255, 450)
        a1=2
        print("1")
    if a2 == 0:
        click(330, 450)
        print("2")
    if a3 == 0:
        click(397, 450)
        print("3")
    if a4 == 0:
        click(458, 450)
        print("4")
