import threading
import time
import random
 
global x
x=[4]
 
def thread_function(name):
    print(f"Thread {name}: starting")
    while True:
      print(f"Thread {name}")      
      time.sleep(1)
      #break
    print(f"Thread {name}: finishing")
 
if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args=("Hello",))
    x.start()
    y = threading.Thread(target=thread_function, args=("There",))
    y.start()

    input("Press Enter to stop...\n")
    print("Quitting")
    
    # Join or no join, there is no convenient way to kill the threads.
    # Kill and terminate attributes would be nice. They exist for processes only.
    #x.join()
    #y.join()
    
    
    

