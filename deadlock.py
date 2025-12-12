import threading
import time

resourse_1=threading.Lock()
resourse_2=threading.Lock()

def thread_1 ():
    with resourse_1:
        print("thread 1 acquire resource 1")
        time.sleep(1)
        print("thread 1 waiting resource 2")
        with resourse_2:
            print("thread 1 acquire resource 2 complete")

def thread_2 ():
    with resourse_2:
        print("thread 2 acquire resource 2")
        time.sleep(1)
        print("thread 2 waiting resource 1")
        with resourse_1:
            print("thread 2 acquire resource 1 complete")

a=threading.Thread(target=thread_1)
b=threading.Thread(target=thread_2)

a.start()
b.start()