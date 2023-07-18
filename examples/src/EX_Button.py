""" Basic blinking LED with button example.
    The Raspberry Pi Pico has a on board led connected to the GP25 terminal.

    The circuit:
      - On board LED connected to the GP25
      - Button connected between GND and GP19 (Pin 25).
        GP19 configured with internal pullup resistor.

    created 2023
    by Alvaro Achury
    modified 18 Aug 2023
    by Alvaro Achury
    
"""

import machine
import time

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value() == 1: 
        led.toggle()
        time.sleep(1)
    
