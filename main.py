import random

import pytesseract
import platform
import pressMouse
import pyautogui
import os
from datetime import datetime
import sendEmail


import takeScreenshot
import extractDollarFromImages
# Global counter for screenshot numbering
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
lowestPriceAccepted = 29
allScreenRagion = (739, 39, 447, 971)
NormalScreenRagion = (763, 376, 409, 549)

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


def start():
    takeScreenshot.start("screenshot.png",region=NormalScreenRagion)
    dollars =extractDollarFromImages.start('screenshot.png')
    if dollars:
        now = datetime.now()
        print(f"Extracted dollars: {dollars} ==> {now}")
        beep()
        beep()
        if dollars > lowestPriceAccepted:
            # Add your logic here for when dollars is greater than 4
            pressMouse.pressAccept()
            return 1
            # strDollars= str(dollars)
            # filename = f"{strDollars}_screenshot{random.randint(1000, 9999)}.png"
            # takeScreenshot.start(filename, region=allScreenRagion)
            # pressMouse.pressExit()
            # sendEmail.start(filename)

        else:
            # Add your logic here for when dollars is not greater than 4
            pressMouse.pressExit()


while True:
    if start():
        break
