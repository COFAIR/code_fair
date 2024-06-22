import requests
import json
import requests
import pyperclip
import time
from PyKakao import Message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
kakao_id = "01048874490"
kakao_pw = "a17178864"
API = Message(service_key = "2e8b2179cbbdcfbf4a32144cdd752e72")
auth_url = API.get_url_for_generating_code()


driver = webdriver.Chrome()
url = 'https://www.google.com'
driver.get(auth_url)


pyperclip.copy(kakao_id) # COMMAND+c가 된 상태
e = driver.find_element(By.NAME, 'loginId')
e.send_keys(Keys.CONTROL, 'v') # COMMAND+v
time.sleep(2)

pyperclip.copy(kakao_pw) # COMMAND+c
e = driver.find_element(By.NAME, 'password')
e.send_keys(Keys.CONTROL, 'v') # cCOMMAND+v
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#mainContent > div > div > form > div.confirm_btn > button.btn_g.highlight.submit').click()
driver.implicitly_wait(10)
variable = driver.current_url
print(variable)


