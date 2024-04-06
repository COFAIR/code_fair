import requests
import json

def sms(address):
    with open(r"C:\코드페어\code_fair\src\kakao_code.json","r") as fp:
         tokens = json.load(fp)


    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers={
          "Authorization" : "Bearer " + tokens["access_token"]
          }

    data={
         "template_object": json.dumps({
              "object_type":"text",
              "text":"사용자의 전체 지번 주소: " + address["documents"][0]["address_name"] ,
              "link":{
                    "web_url":f"http://map.naver.com/index.nhn?slng=127&slat=37.5&elng=127.5&elat=37.4&pathType=0&showMap=true&etext={ address["documents"][0]["address_name"]}&menu=route",
                    "mobile_web_url":f"http://map.naver.com/index.nhn?slng=127&slat=37.5&elng=127.5&elat=37.4&pathType=0&showMap=true&etext={ address["documents"][0]["address_name"]}&menu=route"
                    }
                })
        }

    response = requests.post(url, headers=headers, data=data)
    response.status_code
    print(response.status_code)
    if response.json().get('result_code') == 0:
       print('메시지를 성공적으로 보냈습니다.')
    else:
       print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))