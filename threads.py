import threading
import time 

def print_1 ():
    print("starting of a thread" , threading.current_thread().name)
    time.sleep(2)
    print("finishing of a thread" , threading.current_thread().name)
    
def print_2 ():
    print("starting of a thread" , threading.current_thread().name)
    time.sleep(1)
    print("finishing of a thread" , threading.current_thread().name)

a = threading.Thread(target=print_1 , name="Thread 1")
b = threading.Thread(target=print_2 , name="Thread 2")

a.start()
b.start()