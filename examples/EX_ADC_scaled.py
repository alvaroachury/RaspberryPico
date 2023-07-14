import machine
import utime
 
analog_value = machine.ADC(27)
conversion_factor = 3.3 / (65535)

while True:
    reading = analog_value.read_u16()     
    print("ADC: ",reading*conversion_factor)
    utime.sleep(0.2)