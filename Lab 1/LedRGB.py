import time
import pycom

pycom.heartbeat(False)

# colors in hexadecimal (0xRRGGBB)
colors = [
    0x745d5a, 0xdfd8d2, 0x800000, 0xb26666,
]

try:
    i = 0
    while True:
        pycom.rgbled(colors[i%len(colors)])
        i+=1
        time.sleep(0.3)
except:
    pycom.heartbeat(True)
