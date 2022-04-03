from multiprocessing import Process, Queue
import os
from threading import Thread
from MainFunctions import *
from radioPlay import *
import psutil
from datetime import datetime
import psutil

def info(title):
    print("\n")
    print (title)
    #print ('module name:', __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print ('parent process:', os.getppid())
    print ('process id:', os.getpid())
    p = psutil.Process(os.getppid())
    time.sleep(3)
    p.terminate()
    


def testKill(pid):
    os.kill(pid, signal.SIGTERM)
    
    

def ApiChecker(pidNum):
    tempTrack = 0
    while True:
        response = requests.get("http://127.0.0.1:8000/currentTrack")
        currentTrack = int(response.text)
        time.sleep(1)
        print(currentTrack)
        if tempTrack != currentTrack:
            tempTrack = currentTrack
            try:
                subprocess.check_output("Taskkill /PID %d /F" % pidNum)
                print("Task Terminated")
            except:
                print('Fucker')
            
            

    

def playFunction(pidQue):
    pidQue.put(os.getppid())
    #os.kill(os.getpid(), signal.SIGTERM)
    while True:
        time.sleep(1)
        print("Getting it done")
    
   # print(os.getpid())
    #print(type(os.getpid()))
    #currentlyPlaying(2)
    


if __name__ == '__main__':
    pidQue = Queue()

    p2 = Process(target=playFunction,args=(pidQue,))

    p2.start()

    pidNum = pidQue.get()
    p1 = Process(target=ApiChecker,args=(pidNum,))
    p1.start()

    p1.join()    

    p2.join()
\

    

    