#http://n0e.radiojar.com/8s5u5tpdtwzuv?rj-ttl=5&rj-tok=AAABf8pZIfoAj4LUj-sLh_n6Vw
import webbrowser
import os
import subprocess
import requests
import signal

import asyncio

async def currentlyPlaying(num):
    if num == 1:
        musicPlay = subprocess.call(["ffplay", "-nodisp", "http://n0e.radiojar.com/8s5u5tpdtwzuv?rj-ttl=5&rj-tok=AAABf8pZIfoAj4LUj-sLh_n6Vw"])
    if num == 2:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://livstream.xyz:8220/radio.mp3"])
    if num == 3:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://livstream.xyz:8050/radio.mp3"])
    if num == 4:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://stream.zeno.fm/wcue1s1g6ehvv"])
    if num == 5:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://livstream.xyz:8030/radio.mp3"])
    if num ==6:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://livstream.xyz:8190/radio.mp3"])
    if num == 7:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "https://server03.quran.com.kw:7000/;*.mp3"])


async def kill(self):
    os.kill(self.p.pid, signal.CTRL_C_EVENT)

async def mainFunction():
    killCommand = False
    while killCommand == False:
        f1 = loop.create_task(mainFunction())
        await asyncio.wait([f1, f2])
        response = requests.get("http://127.0.0.1:8000/currentTrack")
        currentTrack = int(response.text)
        print(currentTrack)
        if currentTrack == 0:
            kill(self)
        elif currentTrack == 1:
            stop()
            playQuranKareem()
        elif currentTrack == 2:
            stop()
            playMahmoudAbdElHakam()
        elif currentTrack == 3:
            stop()
            playSharawi()
        elif currentTrack == 4:
            stop()
            playGaber()
        elif currentTrack == 5:
            stop()
            playHosary()
        elif currentTrack == 6:
            stop()
            playRef3at()
        elif currentTrack == 7:
            stop()
            playAbdelBaset()
        elif currentTrack == 44:
            kill()

loop = asyncio.get_event_loop()
loop.run_until_complete(mainFunction())
loop.close()