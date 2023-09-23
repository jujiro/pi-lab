# Example: Button
from gpiozero import Button
from time import sleep

#Refer to the gpio.jpg for pin layout.
btn = Button(17)

while True:
	btn.wait_for_press()
	print("Button pressed")
	break

