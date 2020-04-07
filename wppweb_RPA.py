from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

message_text = ""

dicionario = {
    "nome1":"55711111111",
    "nome2":"55712222222"
    }

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

driver = webdriver.Chrome(r'C:\Users\guinh\OneDrive\Área de Trabalho\.PyCharmCE2019.2\PycharmProjects\cursoemvideo\chromedriver')
driver.get("http://web.whatsapp.com")

sleep(10)

def send_whatsapp_msg(phone_no, name):
    driver.get("https://web.whatsapp.com/send?phone={}".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box = driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        txt_box.send_keys(message_text.format(name))
        txt_box.send_keys("\n")

        sleep(10)

    except Exception as e:
        print("Número de contato invalido :"+str(phone_no))

for pessoa in dicionario.items():
    try:
        send_whatsapp_msg(pessoa[1], pessoa[0])
    
    except Exception as e:
        sleep(10)
