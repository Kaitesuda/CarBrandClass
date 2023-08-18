import pickle
import base64
import cv2
import requests

brand_map = {
    0:"Audi", 
    1:"Hyundai Creta", 
    2:"Mahindra Scorpio", 
    3:"Rolls Royce",
    4:"Swift", 
    5:"Tata Safari", 
    6:"Toyota Innova"
}


def predict_car(img,model): 
    
    url = "http://172.17.0.2/api/genhog"
    
    
    response = requests.get(url, json={"dataImage":img})
    if response.status_code == 200:
        try:
            resdatajson = response.json()
            responseList = [resdatajson[key] for key in resdatajson]
            car = model.predict(responseList)
            result_brand=brand_map.get(car[0])

            return result_brand
        except requests.exceptions.JSONDecodeError as e:
            print("JSON Decode Error:", e)
    else:
        print("API Request Error. Status Code:", response.status_code)
        return None