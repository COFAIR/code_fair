import requests
import json
from dotenv import load_dotenv
from haversine import haversine
import pprint

# Comments!
class home:
    """
    home 클래스는 사용자의 집 위치를 나타내는 클래스입니다.
    """
    def __init__(self, home):
        """
        home 객체를 초기화합니다.
        
        :param home: 집의 위치를 나타내는 튜플 (위도, 경도)
        """
        self.home = home
        
# 실시간 위치 추적
def Location():
    """
    사용자의 실시간 위치를 Google Geolocation API를 사용하여 추적합니다.
    
    :return: 현재 위치의 위도와 경도를 포함하는 딕셔너리
    """
    load_dotenv(verbose=True)
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCBhBG16Zjr8dJvrrZJpRfOjiq6jWdSzE4'
    data = {
        'considerIp': True,
    }
    result = requests.post(url, json=data)
    data = json.loads(result.text)
    return data["location"]

load_dotenv(verbose=True)
url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCBhBG16Zjr8dJvrrZJpRfOjiq6jWdSzE4'
data = {
    'considerIp': True,
}
result = requests.post(url, json=data)
data = json.loads(result.text)
print( data["location"])
# 두 지점 사이의 거리 계산
def Location_home(home):
    """
    사용자의 현재 위치와 집(home) 사이의 거리를 계산합니다.
    
    :param home: 집의 위치를 나타내는 튜플 (위도, 경도)
    :return: 사용자의 현재 위치와 집 사이의 거리 (km 단위)
    """
    realtime = Location() 
    # home_plus()
    a = (realtime["lat"], realtime["lng"])
    distance = haversine(a, home, unit = 'km')
    return distance

def user_Location():
    """
    카카오 지역 검색 API를 사용하여 사용자의 현재 위치에 대한 주소를 조회합니다.
    
    :return: 사용자의 현재 위치에 대한 전체 주소 정보를 포함하는 딕셔너리
    """
    a = Location()
    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x="+str(a["lng"])+"&y="+str(a["lat"])
    headers = {"Authorization": "KakaoAK 2e8b2179cbbdcfbf4a32144cdd752e72"}
    api_json = requests.get(url, headers=headers)
    full_address = json.loads(api_json.text)
    return full_address