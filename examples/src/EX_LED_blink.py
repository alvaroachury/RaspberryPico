import machine
import timmer

led = machine.Pin(15, machine.Pin.OUT)

while True:
    led.value(1)
    timmer.sleep(1)
    led.value(0)
    timmer.sleep(1)