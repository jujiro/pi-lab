import logging
from multiprocessing import Process
from multiprocessing.managers import SharedMemoryManager
import time
import random
import sys
import pickle

pp1=None
pp2=None

def child(my_name):
  while True:
    print(f"Hello from thread, {my_name}")
    time.sleep(2)
      
def controller():
  sys.stdin = open(0) # <--- Here's the magic line...you'll need to "import sys" above too
  global pp1, pp2
  pp2 = Process(target=child, args=("Dick",))
  pp2.start()   
  while True:
    key = input("Enter x to quit\n")
    if key=="x":
      pp1.kill()
      pp2.kill()
      print(f"Uh oh. Time to go.")
      break

if __name__ == "__main__":
  pp1 = Process(target=child, args=("Tom",))
  pp1.start()
  c=Process(target=controller, args=())
  c.start()
  c.join()
  print ("Exiting")

