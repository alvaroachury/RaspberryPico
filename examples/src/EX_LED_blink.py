""" Basic blinking LED example.
    The Raspberry Pi Pico has a on board led connected to the GP25 terminal.

    The circuit:
      - On board LED connected to the GP25 

    created 2023
    by Alvaro Achury
    modified 18 Aug 2023
    by Alvaro Achury
    
"""

import machine
import time

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
<<<<<<< HEAD
    
    ## alternative solution
    # led.toggle()
    # time.sleep(1)
=======
>>>>>>> 066708685e1cb71f41924f7e4728789dc0d6d8db
