from microbit import *
while True:
    a = accelerometer.get_values()
    print(a)
    sleep(100)




"""
from microbit import *
while True:
    a = accelerometer.get_values()
    gesture = accelermeter.current_gesture()
    if gesture == "face up":
        display.show(shooter)
    elif gesture == "right":
        display.show(right)
    elif gesture == "left":
        display.show(left)
    elif gesture == "top":
        display.show(top)
    elif gesture == "bottom":
        display.show(bottom)
    else:
        pass
    print(a)
    sleep(100)
"""