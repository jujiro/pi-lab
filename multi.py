import logging
from multiprocessing import Process
from multiprocessing.managers import SharedMemoryManager
import time
import random
import sys
import pickle


def print_shared():
  print(p)

def thread_function(p):
  while True:
    i=random.randrange(0,7)
    print(i)
    #p[i]=[True, False, "ABCDEFGHTTTT", b"998sssssss9", pickle.dumps({"a":4, "b":6}), 77.987, None][i] 
    p[i]=['howdyTT', b'HoWdYTT', -273.154, 100, "DDDD", 99, b"998sssssss9"][i] 
    time.sleep(2)
      
def process_controller():
  sys.stdin = open(0) # <--- Here's the magic line...you'll need to "import sys" above too
  while True:
    key = input("Enter a string: ")
    if key=="x":
      print(f"You entered {key}")
      break
 
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    smm=SharedMemoryManager()
    smm.start()
    global p
    lst=['howdy', b'HoWdY', -273.154, 100, None, "x", b"998"]
    print(lst)
    p=smm.ShareableList(lst)

    print(p)
    z=Process(target=process_controller, args=())
    z.start()

    x = Process(target=thread_function, args=(p,))
    x.start()
    
    y = Process(target=thread_function, args=(p,))
    y.start()
    z.join()
            
    x.terminate()
    y.terminate()
    x.join()
    y.join()

    print(p)
    print_shared()
