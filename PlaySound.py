from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from WebpageOpen import  *

app = FastAPI()

origins = [
    "file:///C:/Users/aladdin/Desktop/ahlan-salati/FrontEnd/Testing.html"
    "http://192.168.50.189:8080",
    "http://127.0.0.1:8080",
    "https://ahlan-salati.surge.sh/",
    "https://ahlan-salati.surge.sh"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_item():
    return ("Sucsuess")
@app.get("/1")
async def text1():
    playQuranKareem()
    return ("Sucsuess")
@app.get("/2")
async def text2():
    playMahmoudAbdElHakam()
    return ("Sucsuess")
@app.get("/3")
async def text3():
    playSharawi()
    return ("Sucsuess")
@app.get("/4")
async def text4():
    playGaber()
    return ("Sucsuess")
@app.get("/5")
async def text5():
    playHosary()
    return ("Sucsuess")
@app.get("/6")
async def text6():
    playRef3at()
    return ("Sucsuess")
@app.get("/7")
async def text7():
    playAbdelBaset()
    return ("Sucsuess")
@app.get("/stop")
async def stopAudio():
    stop()
    return ("Sucsuess")




