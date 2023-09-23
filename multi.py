import logging
from multiprocessing import Process
from multiprocessing.managers import SharedMemoryManager
import time
import random
import sys
import pickle

pp1=None
pp2=None

def thread_function():
  while True:
    print(f"Hello from thread. {pp1}")
    time.sleep(2)
      
def process_controller():
  sys.stdin = open(0) # <--- Here's the magic line...you'll need to "import sys" above too
  global pp1, pp2
  pp2 = Process(target=thread_function, args=())
  pp2.start()   
  while True:
    key = input("Enter x to quit")
    if key=="x":
      pp1.kill()
      pp2.kill()
      print(f"Hello from controller. {pp1}")
      break
 
if __name__ == "__main__":
  pp1 = Process(target=thread_function, args=())
  pp1.start()
  #pp2 = Process(target=thread_function, args=())
  #pp2.start() 
  z=Process(target=process_controller, args=())
  z.start()
  z.join()
  print ("Exiting")

