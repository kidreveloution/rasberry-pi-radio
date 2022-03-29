import subprocess
import signal
from testing import defo

def changeTrack(num):
    if num == 1:
        musicPlay = subprocess.call(["ffplay", "-nodisp", "http://n0e.radiojar.com/8s5u5tpdtwzuv?rj-ttl=5&rj-tok=AAABf8pZIfoAj4LUj-sLh_n6Vw"])
        while True:
            defo()
    if num == 2:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://livstream.xyz:8220/radio.mp3"])
        while True:
            defo()
    if num == 3:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://livstream.xyz:8050/radio.mp3"])
        while True:
            defo()
    if num == 4:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://stream.zeno.fm/wcue1s1g6ehvv"])
        while True:
            defo()
    if num == 5:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://livstream.xyz:8030/radio.mp3"])
        while True:
            defo()
    if num ==6:
        musicPlay =subprocess.call(["ffplay", "-nodisp", "http://livstream.xyz:8190/radio.mp3"])
        while True:
            defo()
    if num == 7:
        os.kill(self.p.pid, signal.CTRL_C_EVENT)
        #musicPlay =subprocess.call(["ffplay", "-nodisp", "https://server03.quran.com.kw:7000/;*.mp3"])