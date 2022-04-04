import subprocess
import sys
def currentlyPlaying(num):
    #subprocess.run(['python'])

    if num == 1: # Quran Kareem Radio
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://stream.radiojar.com/8s5u5tpdtwzuv"])
    elif num == 2:#Al Sha3arawi, not working
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8090/radio.mp3"])
    elif num == 3: #Al Housary Radio
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8050/radio.mp3"])
    elif num == 4: #Shiekh Ref3at
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8140/radio.mp3"])
    elif num == 5: #Shiekh Abd El Baaset
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "https://Qurango.net/radio/abdulbasit_abdulsamad_mojawwad.mp3"])
    elif num ==6: #Moustafa Isma3eel
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://quraan.us:9786/;*.mp3"])
    elif num == 7:#El Menshaway
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8070/radio.mp3"])
    elif num == 8:  # El Bana
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8110/radio.mp3"])
    elif num == 9:  # El Tablawi
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8130/radio.mp3"])
    elif num == 10:  # Ali Mahmoud
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8060/radio.mp3"])
    elif num == 11:  # Mahmoud Abd El Hakm
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8100/radio.mp3"])
    elif num == 12:  # El Naqshabandi
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8190/radio.mp3"])
    elif num == 13:  # Mahmoud Abd El Hakm
        musicPlay = subprocess.call(
            ["ffplay", "-nodisp", "http://livstream.xyz:8070/radio.mp3"])
    elif num == 0:
        print("Waiting for response")
    else:
        print("Invalid Choice")


if __name__ == '__main__':
    temp = sys.argv[1]
    num = int(temp)
    print(type(num))
    currentlyPlaying(num)
