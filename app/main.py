from fastapi import FastAPI,Request
import pickle
import base64
import cv2
import numpy as np
from app.code import predict_car
import os


m = pickle.load(open(os.getcwd()+r'/model/model.pkl', 'rb'))

app = FastAPI()

@app.get("/")
def root():
    return "hello world"



@app.post("/api/carbrand")
async def read_str(data : Request):
    json=await data.json()
    img_string=json["img"]
    car = predict_car(img_string,m)
    return {"brand":car}