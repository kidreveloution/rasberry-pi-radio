from multiprocessing import Process, Queue
import subprocess
from datetime import datetime
import time
import requests
from radioFile import *


    
    

def ApiChecker():
    time.sleep(1)
    tempTrack = 1
    while True:
        #response = requests.get("https://t06t4i.deta.dev/currentTrack")
        currentTrack = 2
        time.sleep(1)
        #intTrack = int(currentTrack)
        print(currentTrack)

        if tempTrack != currentTrack:
            tempTrack = currentTrack
            
            subprocess.Popen(['pkill', '-9', 'ffplay'])
            subprocess.Popen(['python', 'radioPlay.py', str(tempTrack)])



if __name__ == '__main__':


    p1 = Process(target=ApiChecker)
    p1.start()
    p1.join()




    

    