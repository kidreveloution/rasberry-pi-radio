from multiprocessing import Process, Queue
from radioFile import *
import subprocess
from datetime import datetime
import time
import requests


    
    

def ApiChecker():
    time.sleep(1)
    tempTrack = 1
    while True:
        response = requests.get("https://t06t4i.deta.dev/currentTrack")
        currentTrack = int(response.text)
        time.sleep(1)
        print(currentTrack)
        if tempTrack != currentTrack:
            tempTrack = currentTrack
            
            subprocess.Popen(['pkill', '-9', 'ffplay'])
            subprocess.Popen(['python', 'radioPlay.py', str(tempTrack)])



def playFunction(num):

    p2 = Process(target=currentlyPlaying ,args=(num,))

    p2.start()
    p2.join()
    


if __name__ == '__main__':


    p1 = Process(target=ApiChecker)
    p1.start()
    p1.join()




    

    