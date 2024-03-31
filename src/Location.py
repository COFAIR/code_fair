import requests
import json
from dotenv import load_dotenv
from haversine import haversine
import pprint

class home:
    def __init__(self, home):
        self.home = home
        
# 실시간 위치 추적
def Location():
    load_dotenv(verbose=True)
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCBhBG16Zjr8dJvrrZJpRfOjiq6jWdSzE4'
    data = {
        'considerIp': True,
    }
    result = requests.post(url, json=data)
    data = json.loads(result.text)
    return data["location"]

# 두 지점 사이의 거리 계산
def Location_home(home):
    realtime = Location() 
    # home_plus()
    a = (realtime["lat"], realtime["lng"])
    distance = haversine(a, home, unit = 'km')
    return distance

def user_Location():
    a = Location()
    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x="+str(a["lng"])+"&y="+str(a["lat"])
    headers = {"Authorization": "KakaoAK 2e8b2179cbbdcfbf4a32144cdd752e72"}
    api_json = requests.get(url, headers=headers)
    full_address = json.loads(api_json.text)
    return full_address