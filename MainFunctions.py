#http://n0e.radiojar.com/8s5u5tpdtwzuv?rj-ttl=5&rj-tok=AAABf8pZIfoAj4LUj-sLh_n6Vw
import webbrowser
import os
import subprocess
import sys
import time
import requests
import signal




def kill(self):
    sys.exit()

def mainFunction(pidNum):
    tempTrack = 1
    while True:
        response = requests.get("http://127.0.0.1:8000/currentTrack")
        currentTrack = int(response.text)
        time.sleep(1)
        print(currentTrack)
        if tempTrack != currentTrack:
            print("CHANGED")
            os.kill(os.getppid(), signal.SIGTERM)

            tempTrack = currentTrack
            if currentTrack == 0:
                print("Fucker")
            elif currentTrack == 1:
                print("\n Playing Track: ", currentTrack)

                #currentlyPlaying(1)

            elif currentTrack == 2:
                print("\n Playing Track: ", currentTrack)

                #currentlyPlaying(2)
            elif currentTrack == 3:
                print("\n Playing Track: ", currentTrack)

                #currentlyPlaying(3)
            elif currentTrack == 4:
                print("\n Playing Track: ", currentTrack)
                #currentlyPlaying(4)
            elif currentTrack == 5:
                print("\n Playing Track: ", currentTrack)

               #currentlyPlaying(5)
            elif currentTrack == 6:
                print("\n Playing Track: ", currentTrack)

                #currentlyPlaying(6)
            elif currentTrack == 7:
                print("\n Playing Track: ", currentTrack)

                #currentlyPlaying(7)
            elif currentTrack == 44:
                kill()
            else:
                print("Invalid, try again")

if __name__ == '__main__':
    killCommand = False
    tempTrack = 1
    while killCommand == False:
        
        response = requests.get("http://127.0.0.1:8000/currentTrack")
        currentTrack = int(response.text)
        if tempTrack != currentTrack:
            tempTrack = currentTrack
            if currentTrack == 0:
                kill()
            elif currentTrack == 1:
                currentlyPlaying(1)
            elif currentTrack == 2:
                currentlyPlaying(2)
            elif currentTrack == 3:
                currentlyPlaying(3)
            elif currentTrack == 4:
                currentlyPlaying(4)
            elif currentTrack == 5:
                currentlyPlaying(5)
            elif currentTrack == 6:
                currentlyPlaying(6)
            elif currentTrack == 7:
                currentlyPlaying(7)
            elif currentTrack == 44:
                kill()

