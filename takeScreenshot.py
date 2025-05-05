import platform,time
import random

import os
import pyautogui
region = (597, 508, 363, 198)

def beep():
    system = platform.system()
    if system == "Windows":
        import winsound
        winsound.Beep(1000, 300)  # frequency=1000Hz, duration=300ms
    elif system == "Darwin":  # macOS
        import os
        os.system('say "done"')  # macOS voice synth
    else:
        print('\a')  # Linux fallback: system bell





def start(name:str,region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(name)




def startindir(name: str, region=None):
    screenshot = pyautogui.screenshot(region=region)

    # Save with full path
    filepath = os.path.join("screenshots", name)
    screenshot.save(filepath)
    print(f"Screenshot saved to: {filepath}")

