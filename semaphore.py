import threading
import time

recieptionact = threading.Semaphore(1)

def enter_examinationroom(n):
    print(f"patient {n} is waiting his turn")
    recieptionact.acquire()
    print(f"patient {n} is in the examinationroom")
    time.sleep(2)
    print(f"patient {n} is out of the examinationroom")
    recieptionact.release()

Patients = []
for i in range(10):
    Patient=threading.Thread(target=enter_examinationroom , args=(i,))
    Patients.append(Patient)
    Patient.start()