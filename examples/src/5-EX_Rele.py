""" Basic Rele control example.

    The circuit:
      - Rele arduino module connected to GND (GND rele terminal) and VBUS (VCC rele terminal) RPiPico terminals.
        The IN rele terminal is controled with a 2n2222 transistor to change the voltage levels.
        GP14 attached to transistor base terminal through a 330 resistor, the transistor emitter terminal is
        connected to GND, while the transistor collector terminal is attached to VBUS through a 330 resistor.
        The IN rele terminal is attached to the transistor collector terminal.

    created 2023
    by Alvaro Achury
    modified 18 Aug 2023
    by Alvaro Achury
    
"""

import machine
import time

rele_control_signal = machine.Pin(14, machine.Pin.OUT)
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    
    if button.value() == 0:
        print(" >*> " ,button.value())
        rele_control_signal.value(1)
        time.sleep(10)
    rele_control_signal.value(0)
    