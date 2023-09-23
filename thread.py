import logging
import threading
import time
import random
 
global x
x=[4]
 
def thread_function(name):
    print(f"Thread {name}: starting")
    while True:
      p.append(name)
      print(f"Thread {name}: in loop {p} id={id(p)}")      
      time.sleep(1)
      #break
    print(f"Thread {name}: finishing")
 
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
 
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=("Hello",))
    logging.info("Main    : before running thread 1")
    x.start()
    y = threading.Thread(target=thread_function, args=("There",))
    logging.info("Main    : before running thread 2")
    y.start()
 
    logging.info("Main    : wait for the thread to finish")
    input("Press Enter to stop...")
    x.terminate()
    y.terminate()
    x.join()
    y.join()
    logging.info("x=%s", x)
    logging.info("Main    : all done")
