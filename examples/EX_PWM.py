from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(16))
pwm.freq(50)

while True:
#     for position in range(1000,4500,50):
    position = int(input("Insert position ... "))
    pwm.duty_u16(position)
    sleep(0.01)
#     for position in range(9000,1000,-50):
#         pwm.duty_u16(position)
#         sleep(0.01)