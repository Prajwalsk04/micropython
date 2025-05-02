#program to beep the buzzer continuosuly

import time,machine

buz=machine.Pin(21,machine.Pin.OUT)

while(1):
    buz.on()
    time.sleep(1)
    buz.off()
    time.sleep(1)
