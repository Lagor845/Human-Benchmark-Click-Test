import pyautogui
import keyboard

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
while True:
    try:
        target = pyautogui.locateOnScreen('Target.PNG',confidence=0.4)
        print(target)
        target = pyautogui.center(target)
        pyautogui.click(target.x,target.y)
        print("Clicked")
        if keyboard.is_pressed('space'):
            break 
    except:
        print("Not found")