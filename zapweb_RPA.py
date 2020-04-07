from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

usr = "user@byintera.com"
pwd = "password"

message_text = ""

dicionario = {
    "nome1" : "55711111111",
    "nome2" : "55712222222", 
    }

driver = webdriver.Chrome(r'C:\Users\guinh\OneDrive\Área de Trabalho\.PyCharmCE2019.2\PycharmProjects\cursoemvideo\automacoes_web\chromedriver')
wait = WebDriverWait(driver, 60)

driver.get("https://chat.whatsweb.app/login/t8pf6s8")
driver.implicitly_wait(15)

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def main():
    # Busca o campo de texto "Email" pelo ID e preenche com o input de usuario
    elem_usr = driver.find_element_by_xpath("//input[@type='text']")
    elem_usr.send_keys(usr)
    sleep(1)
    # Busca o campo de texto "Email" pelo ID e preenche com o input de senha
    elem_psw = driver.find_element_by_xpath("//*[@id='addlogin']/div[2]/input[2]")
    elem_psw.send_keys(pwd)
    sleep(1)
    # Pressiona a tecla "ENTER" para acessar o facebook
    elem_psw.send_keys(Keys.RETURN)
    sleep(60)
def send_whatsapp_msg(phone_no, name):
    # try:
    #     driver.switch_to.alert()
    # except Exception as e:
    #     pass

    try:
        new_chat_elem = driver.find_element_by_xpath("//*[@id='Layer_1']") #wait.until(EC.element_to_be_clickable((By.ID, "layer_1")))
        new_chat_elem.click()
        sleep(2)

        phone_box = driver.find_element_by_xpath("//*[@id='novochat-telefone']") #wait.until(EC.element_to_be_clickable((By.ID, 'novochat-telefone')))
        phone_box.send_keys(phone_no)
        sleep(1)

        txt_box = driver.find_element_by_xpath("//*[@id='novochat-msg']")
        txt_box.send_keys(message_text.format(name))
        sleep(1)

        send_msg_elem = driver.find_element_by_xpath("//*[@id='modal-novaConversa']/div/p/input")
        send_msg_elem.click()
        sleep(2)

        press_enter = driver.find_element_by_xpath("//*[@id='formSend']")
        press_enter.send_keys(Keys.RETURN)
        sleep(5)

    except Exception as e:
        print("Número de contato invalido :" + str(phone_no))

main()


for pessoa in dicionario.items():
    try:
        send_whatsapp_msg(pessoa[1], pessoa[0])

    except Exception as e:
        sleep(10)

