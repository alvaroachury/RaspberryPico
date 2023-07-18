""" Basic PWM servomotor control example.

    The circuit:
      - Servomotor SG90 powered between GND (brown servo wire) and VBUS (red servo wire) RPiPico terminals.
        Control signal (orange servo wire) connected to the GP16 terminal.

    created 2023
    by Alvaro Achury
    modified 18 Aug 2023
    by Alvaro Achury
    
"""

import time 
import machine

pwm = machine.PWM(machine.Pin(16))
pwm.freq(50)

while True:
    position = int(input("Insert position value between 1000 to 8000 ... "))
    pwm.duty_u16(position)
    time.sleep(0.1)
