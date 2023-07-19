""" K type termocouple reading control with arduino board MAX6675.

    The circuit:
      - Power supply of MAX6675 guarantee with GND and VBUS connection.
      - MAX6675 'CS' terminal attached to GP1.
      - MAX6675 'SCK' terminal attached to GP14.
      - MAX6675 'SO' terminal attached to GP15.

    created 2023
    by Alvaro Achury
    modified 19 Aug 2023
    by Alvaro Achury
    
"""


from machine import Pin,I2C
import utime as time
from max6675 import MAX6675


T0_so = Pin(15, Pin.IN)
T0_sck = Pin(14, Pin.OUT)
T0_cs = Pin(1, Pin.OUT)

T0_reading = MAX6675(T0_sck, T0_cs, T0_so)

while True:
    print("T0:", T0_reading.read())
    time.sleep(2)
    
    
    