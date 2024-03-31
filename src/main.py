import datetime
from Location import *
from kakao import *
from PyKakao import Message
API = Message(service_key = "2e8b2179cbbdcfbf4a32144cdd752e72")

# def home_plus(a):
#     home = a
#     return home
home = (37.4923615,127.0292881)


# 기준 시간 변경
class Timetracker:
    def __init__(self):
        self.current_time = datetime.datetime.now()
        self.condition = False
        self.message_sent = False  

    def update_time(self):
        if self.condition:
            self.current_time = datetime.datetime.now()

    def change_condition(self, new_condition):
        self.condition = new_condition

    def check_time_difference(self):
        return (datetime.datetime.now() - self.current_time).total_seconds() >  1
    
tm = Timetracker()

try:
    while True:
        
        distance = Location_home(home)
        if distance > 1:
            if not tm.condition:
                tm.change_condition(True)
                tm.update_time()

            elif tm.check_time_difference()and not tm.message_sent:
                sms(user_Location())
                tm.message_sent = True

        elif tm.condition:
            tm.change_condition(False)
            tm.update_time(False)

except KeyboardInterrupt:
    print("프로그램 종료")