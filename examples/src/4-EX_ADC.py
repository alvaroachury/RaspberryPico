""" Basic example for the ADC configuration.
    The Raspberry Pi Pico has three 12-bit (0 - 4095) ADCs (GP26, GP27, GP28).
        
    Raises:
      - The ADC reading value is proportional to the voltage level at the middle
        point of the potentiometer.
    
    The circuit:
      - 10K potentiometer with end leads connected to GND and +3.3V (Pin 36),
        middle terminal of potentiometer connected to ADC input (ADC1 - GP27).

    created 2023
    by Alvaro Achury
    modified 18 Aug 2023
    by Alvaro Achury
    
"""

import machine
import utime

adc_input_value = machine.ADC(27)
 
while True:
    reading = adc_input_value.read_u16()     
    print("ADC digital value: ",reading)
    utime.sleep_us(2)