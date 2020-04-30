# -*- coding: utf-8 -*-

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

def main():
    # Input da conta do facebook para login
    usr = "gaguinho_tavares@hotmail.com"
    pwd = "8793120na"
    message = "testing by intera: https://intera.talent-hacking.com/"

    # Lista dos links do facebook que serão acessados
    group_links = ["https://web.facebook.com/groups/686668264688108/?ref=group_browse", "https://web.facebook.com/groups/1566371676935114/?ref=group_browse", "https://web.facebook.com/groups/309165055871622/?ref=group_browse"]


    # Desabilita notificações par não atrapalhar o processo
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2  # 1:allow, 2:block
    })

    driver = webdriver.Chrome(r'C:\Users\guinh\OneDrive\Área de Trabalho\.PyCharmCE2019.2\PycharmProjects\cursoemvideo\chromedriver')
    driver.implicitly_wait(15)  # seconds

    def element_presence(by,xpath,time):
        element_present = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(driver, time).until(element_present)

    # Acessa o facebook
    driver.get("http://www.facebook.com")

    # Busca o campo de texto "Email" pelo ID e preenche com o input de usuario
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    # Busca o campo de texto "Email" pelo ID e preenche com o input de senha
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    # Pressiona a tecla "ENTER" para acessar o facebook
    elem.send_keys(Keys.RETURN)

    for group in group_links:
        
        
        # Busca um link nos grupos do facebook listados
        driver.get(group)

        # Tranforma a caixa de texto do post em uma variável "post_box"
        open_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
        
        # Busca o input de "message" e escreve na caixa de texto
        open_box.send_keys()

        element_presence(By.XPATH,'//*[@id="js_4t"]/div[1]/div/div[1]/div[2]/table',30)
        
        post_box = driver.find_element_by_xpath("//*[@id='js_1o']/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/span/span")
        post_box.send_keys(message)
        # Identifica os elementos com TagName "button", que no caso são botões e faz a ação de clicar no botão "Publicar"
        
        element_presence(By.XPATH,'//*[@id="u_1e_0"]/div[1]/div[1]/span/div[1]/div/a/div/div',30)

        buttons = driver.find_elements_by_tag_name("button")

        for button in buttons:
            if button.text == "Publicar":
                button.click()
                sleep(10)

    # driver.close()


if __name__ == '__main__':
    main()