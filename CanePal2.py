# CanePal
# code modified from ultrasonic_dist_demo and
# servo_demo presented in INFO 697 at Pratt Institute
# with Dr. Maceli and Basem Ali

from microbit import *
from machine import time_pulse_us
import music

trig = pin2
echo = pin1

trig.write_digital(0)
echo.read_digital()

while True:
    trig.write_digital(1)
    trig.write_digital(0)
    microsec = time_pulse_us(echo, 1)
    time_echo = microsec / 1000000
    dist_cm = (time_echo / 2) * 34300
    print((dist_cm,))
    # or in inches
    # dist_inches = dist_cm/2.54
    # print((dist_inches,))
    if dist_cm < 30:
        music.play(music.BA_DING)
    sleep(500)

    # while True:
    # gesture = accelerometer.current_gesture()
    # if gesture == "freefall":
    #  display.show("FALL")
    # else:
    # display.show(Image.HAPPY)

