import pyautogui
import webbrowser
from PIL import ImageChops
import keyboard
import time


def open_browser(u,p):
    try:
        webbrowser.get(p).open(u)
    except Exception as e:
        print(f"Error in opening")
    time.sleep(3)
    pyautogui.press('space')

def take_ss(regions):
    return pyautogui.screenshot(region=regions).convert("1")

def main():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    url = "https://elgoog.im/dinosaur-game/"
    open_browser(url,chrome_path)
 
    is_game=True
    while is_game:
        background_down=take_ss((160,100,300,1))
        background_up=take_ss((160,200,300,1))
        down=take_ss((200,592,300,1))
        up=take_ss((200,496,280,1))

        if ImageChops.difference(background_down,down).getbbox():
            pyautogui.press('space')
        elif ImageChops.difference(background_up,up).getbbox():
            pyautogui.keyDown('down')
            time.sleep(0.25)
            pyautogui.keyUp('down')
        
        if keyboard.is_pressed('q'):
            print("Quiting")
            is_game=False

if __name__=='__main__':
    main()  