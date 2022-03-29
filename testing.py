import asyncio
import requests
import os
import subprocess
import signal
import time
from radioCall import *


def getApiValue():
    response = requests.get("http://127.0.0.1:8000/currentTrack")
    currentTrack = int(response.text)
    return currentTrack
  

def defo():
    old_temp = None
    while True:
        time.sleep(1)
        temp = getApiValue()
        if old_temp != temp:
            os.kill(self.p.pid, signal.CTRL_C_EVENT)

            old_temp = temp
            changeTrack(temp)

if __name__ == '__main__':
    old_temp = None
    while True:
        time.sleep(1)
        temp = getApiValue()
        if old_temp != temp:
            old_temp = temp
            changeTrack(temp)