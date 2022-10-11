import time
import pycom

pycom.heartbeat(False)

# colors in hexadecimal (0xRRGGBB)
colors = [
    0x745d5a, 0xdfd8d2, 0x800000, 0xb26666,
    0xDFFF00, 0xFFBF00, 0xFF7F50, 0xDE3163,
    0x9FE2BF, 0x40E0D0, 0x6495ED, 0xCCCCFF
]

try:
    i = 0
    while True:
        pycom.rgbled(colors[i%len(colors)])
        i+=1
        time.sleep(0.3)
except:
    pycom.heartbeat(True)
