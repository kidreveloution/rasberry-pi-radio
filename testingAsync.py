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
    response = requests.get("http://127.0.0.1:8000/currentTrack")
    currentTrack = int(response.text)
    tempTrack = currentTrack
    while True:
        response = requests.get("http://127.0.0.1:8000/currentTrack")
        currentTrack = int(response.text)
        time.sleep(1)
        print(currentTrack)
        if tempTrack != currentTrack:
            try:
                subprocess.check_output("Taskkill /PID %d /F" % pidNum)
            except:
                print('Fucker')
            
            

    

def playFunction(pidQue):
    pidQue.put(os.getpid())
    #os.kill(os.getpid(), signal.SIGTERM)
    print(os.getpid())
    #print(type(os.getpid()))
    currentlyPlaying(2)
    


if __name__ == '__main__':
    #info('main line')
    pidQue = Queue()

    p2 = Process(target=playFunction,args=(pidQue,))

    p2.start()

    #os.kill(pidNum, signal.SIGTERM)
    pidNum = pidQue.get()
    p1 = Process(target=ApiChecker,args=(pidNum,))
    p1.start()

    #p2.join()
    p1.join()    

    p2.join()
    #testKill(pidNum)

    #os.kill(pidNum, signal.SIGTERM)

    

    