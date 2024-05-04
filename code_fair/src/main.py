import datetime
from Location import *
from kakao import *
from PyKakao import Message
API = Message(service_key = "2e8b2179cbbdcfbf4a32144cdd752e72")

# def home_plus(a):
#     home = a
#     return home
home = (37.4923615,127.0292881)


class Timetracker:
    """
    Timetracker 클래스는 현재 시간을 추적하고, 특정 조건에 따라 상태를 변경하는 기능을 제공합니다.
    """
    def __init__(self):
        """
        Timetracker 객체를 초기화합니다.
        """
        self.current_time = datetime.datetime.now()
        self.condition = False
        self.message_sent = False  

    def update_time(self):
        """
        조건이 참일 경우 현재 시간을 업데이트합니다.
        """
        if self.condition:
            self.current_time = datetime.datetime.now()

    def change_condition(self, new_condition):
        """
        객체의 조건을 새로운 상태로 변경합니다.
        
        :param new_condition: 새로운 조건의 상태 (True 또는 False)
        """
        self.condition = new_condition

    def check_time_difference(self):
        """
        현재 시간과 이전에 기록된 시간의 차이가 1초 이상인지 확인합니다.
        
        :return: 시간 차이가 1초 이상이면 True, 그렇지 않으면 False
        """
        return (datetime.datetime.now() - self.current_time).total_seconds() >  1
    
tm = Timetracker()

while True:
    # 사용자와 집 사이의 거리를 계산합니다.
    distance = Location_home(home)
    
    # 사용자가 지정된 거리 이상 떨어졌을 경우
    if distance > 1:
        if not tm.condition:
            tm.change_condition(True)
            tm.update_time()

        # elif tm.check_time_difference()and not tm.message_sent:
        #     # 조건을 만족했을 때 메시지를 전송하는 코드 구현 부분(미구현(카톡 서버 인증과정에서 오류 발생 하므로 다른 걸 써야함))
        #     # sms(user_Location()) # 카톡 메세지 발송
        #     tm.message_sent = True

    # 사용자가 지정된 거리 안으로 돌아왔을 경우
    elif tm.condition:
        tm.change_condition(False)
        tm.update_time(False)