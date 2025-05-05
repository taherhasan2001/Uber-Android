import pyautogui
import time
import platform

# Function to play a sound
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

print("Move your mouse to the TOP-LEFT corner of the region...")
time.sleep(5)
beep()
top_left = pyautogui.position()
print(f"Top-left corner: {top_left}")

print("Now move your mouse to the BOTTOM-RIGHT corner of the region...")
time.sleep(5)
beep()
bottom_right = pyautogui.position()
print(f"Bottom-right corner: {bottom_right}")

# Calculate region (left, top, width, height)
left = top_left.x
top = top_left.y
width = bottom_right.x - top_left.x
height = bottom_right.y - top_left.y

region = (left, top, width, height)
print(f"\nYour region is: {region}")
