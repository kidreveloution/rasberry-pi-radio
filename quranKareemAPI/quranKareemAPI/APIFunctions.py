

def changeTrack(num): #Quran Kareem Radio
    fileWrite = open("tmp/currentTrack.txt", "w")
    fileWrite.write(str(num))

def getTrack():
    fileRead = open("tmp/currentTrack.txt", "r")
    currentTrack = int(fileRead.read()) 
    return currentTrack

if __name__ == '__main__':

    getTrack()
    changeTrack(5454)
    getTrack()