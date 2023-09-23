# Example: Button
from gpiozero import Button
from time import sleep, perf_counter

def process_button_pressed(btn):
  print(f"Pressed {perf_counter()} {btn.is_pressed} {btn.is_held}")

def process_button_held(btn):
  print(f"Held {perf_counter()}")

def process_button_released(btn):
  print(f"Released {perf_counter()}")

def main():
  b=Button(17, hold_time=2)
  b.hold_repeat=False
  b.when_pressed = process_button_pressed
  b.when_held = process_button_held
  b.when_released = process_button_released
  while True:
    sleep(1)
  
if __name__ == "__main__":
  main()

