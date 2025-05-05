import pyautogui
import time
import platform
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



def click_at(x, y, clicks=1, button='left', delay=0.5):
    """
    Clicks at the specified screen coordinates.

    Args:
        x (int): X-coordinate (horizontal)
        y (int): Y-coordinate (vertical)
        clicks (int): Number of clicks (default: 1)
        button (str): 'left', 'right', or 'middle' (default: 'left')
        delay (float): Delay after moving (seconds, default: 0.5)
    """
    try:
        # Move mouse to (x, y) and click
        pyautogui.moveTo(x, y)  # Smooth movement
        time.sleep(delay)  # Short pause before clicking
        pyautogui.click(clicks=clicks, button=button)
    except Exception as e:
        print(f"Error clicking: {e}")



def print_mouse_position_after_delay(delay_seconds=5):
    """
    Prints the current mouse (x, y) coordinates after a delay.

    Args:
        delay_seconds (int): Delay before printing (default: 5 seconds).
    """
    print(f"Waiting {delay_seconds} seconds... Move your mouse to the target position.")
    time.sleep(delay_seconds)
    x, y = pyautogui.position()
    print(f"Current mouse position: X={x}, Y={y}")
    return x, y


def pressAccept():
    click_at(790, 753)
    print("Clicked Accept")
def pressExit():
    click_at(1107, 560)
    click_at(1107, 600)
    click_at(1107, 640)
    click_at(1107, 680)
    click_at(1107, 620)
    click_at(1107, 620)
    click_at(1107, 580)
    print("Clicked Exit")



# print_mouse_position_after_delay(3)
#X=930, Y=462
#X=790, Y=753