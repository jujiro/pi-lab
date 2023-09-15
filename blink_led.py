# Example: Blinking LED
from gpiozero import LED
from time import sleep

#Refer to the gpio.jpg for pin layout.
led = LED(17)

while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
