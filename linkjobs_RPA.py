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
import pandas as pd

driver = webdriver.Chrome(r'C:\Users\guinh\OneDrive\Área de Trabalho\.PyCharmCE2019.2\PycharmProjects\cursoemvideo\chromedriver')
wait = WebDriverWait(driver, 60)

perfil_urls = []
perfil_names = []
perfil_emails = []
perfil_phones = []
perfil_states = []

driver.get("https://www.linkedin.com/talent/hire/360351026/discover/applicants")
driver.implicitly_wait(15)

separator = " "

def log_in_linkedin():
    usr = "diegocastro27f@gmail.com"
    pwd = "growthintera34"
    
    elem_usr = driver.find_element_by_xpath("//*[@id='username']")
    elem_usr.send_keys(usr)
    sleep(1)
    
    elem_psw = driver.find_element_by_xpath("//*[@id='password']")
    elem_psw.send_keys(pwd)
    sleep(1)
    
    elem_psw.send_keys(Keys.RETURN)
    sleep(5)
    
    open_perfil = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/form/ol/li[1]/div/article/div/article/div/div/div[1]/section/div/div[2]/span/span[1]/div/a")
    open_perfil.click()
    sleep(3)
    
def get_perfil_urls():
    
    sleep(5)
  
    link_perfil_elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/a")
    perfil_url = link_perfil_elem.get_attribute("href") 
    if perfil_url in perfil_urls:
        print("PERFIL REPETIDO")
        return True
     
    print(perfil_url)
         
    name_perfil_elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[2]/div/div/span/div/div/div[2]/div[1]/header/section/div/div[1]/section/div/div[2]/span/span[1]/div")
    perfil_name = name_perfil_elem.text
    sleep(1)
    print(perfil_name)
                      
    local_perfil_elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[2]/div/div/span/div/div/div[2]/div[1]/header/section/div/div[1]/section/div/div[2]/div[3]/div")
    if local_perfil_elem.text == "Brasil":
        perfil_Local = "Brasil, São Paulo"
    else:
        perfil_local = local_perfil_elem.text
    
    print(perfil_local)
    
    
    sleep(1)               
    email_exist_perfil_elem = driver.find_elements_by_xpath("/html/body/div/div/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[2]/div/div/span/div/div/div[2]/div[1]/header/section/div/div[1]/div[1]/section[1]/ol/li[1]/span[1]")
    if email_exist_perfil_elem:
        perfil_email = email_exist_perfil_elem[-1].text
    else:
        perfil_email = "Sem email"
    sleep(1)
    print(perfil_email)
                             
    phone_exist_perfil_elem = driver.find_elements_by_xpath("/html/body/div/div/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[2]/div/div/span/div/div/div[2]/div[1]/header/section/div/div[1]/div[1]/section[2]/ol/li[1]/span[1]")
    if phone_exist_perfil_elem:
         perfil_phone = phone_exist_perfil_elem[-1].text
    else:
         perfil_phone = "Sem número de celular"
    sleep(1)
    print(perfil_phone.replace("-", "").replace("+55", "").replace("+5555", "").replace(" ", "").replace("(", "").replace(")", ""))
    
    perfil_urls.append(perfil_url)
    perfil_names.append(perfil_name)
    perfil_emails.append(perfil_email)
    perfil_phones.append(perfil_phone)
    perfil_states.append(perfil_local)
    
    print(perfil_urls, "\n" , "\n" ,
    perfil_names, "\n" , "\n" ,
    perfil_emails, "\n" , "\n" ,
    perfil_phones , "\n" , "\n" ,
    perfil_states)
                                  
    button_next_page =  driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[3]/section/div[2]/div/div/div[1]/div[2]/div/div/span/div/div/div[1]/div/nav/a[2]")
    button_next_page.click()
    sleep(5)
    return False


    
def excel_data():
    df = pd.DataFrame({ "Vaga" : "BE/Creditas",
                        "Nomes": perfil_names,
                        "Links" : perfil_urls,
                        "Email" : perfil_emails,
                        "Celular" : perfil_phones,
                        "Local" : perfil_states })
    
    df.to_excel("Creditas-back-2-teste-oficial.xlsx")

def testing(names, emails, last_names, citys, state,  phones, linkedins):
    states = {
    ' Acre' : 2 ,
    ' Alagoas' : 3 ,
    ' Amapá' : 4 ,
    ' Amazonas' : 5 ,
    ' Bahia' : 6 ,
    ' Ceará' : 7 ,
    ' Distrito Federal' : 8 ,
    ' Espírito Santo' : 9 ,
    ' Goiás' : 10, 
    ' Maranhão' : 11, 
    ' Minas Gerais' : 12, 
    ' Mato Grosso do Sul' : 13, 
    ' Mato Grosso' : 14, 
    ' Pará' : 15, 
    ' Paraíba' : 16, 
    ' Pernambuco' : 17,  
    ' Piauí' : 18,  
    ' Paraná' : 19,   
    ' Rio de Janeiro' : 20, 
    ' Rio Grande do Norte' : 21, 
    ' Rondônia' : 22,  
    ' Roraima' : 23,   
    ' Rio Grande do Sul' : 24,
    ' Santa Catarina' : 25,   
    ' Sergipe' : 26, 
    ' São Paulo' : 27, 
    ' Tocantins' : 28, 
    }  
     
    driver.get("https://vagas.byintera.com/ifood/software-engineer-back-end/?utm_source=Linkedin&utm_medium=vaga&utm_content=32-5&utm_campaign=Diego&cr=growth")
    sleep(5)
    name_input_elem = driver.find_element_by_xpath("//*[@id='form-field-name']")
    name_input_elem.send_keys(names)
    
    last_name_input_elem = driver.find_element_by_xpath("//*[@id='form-field-4310bd1']") 
    last_name_input_elem.send_keys(last_names)
    
    email_input_elem = driver.find_element_by_xpath("//*[@id='form-field-ac76dea']")
    email_input_elem.send_keys(emails)
    
    city_input_elem = driver.find_element_by_xpath("/html/body/div/div/div/div/main/article/div/div/div/div/section[13]/div/div/div/div/div/div[7]/div/form/div/div[24]/input")
    city_input_elem.send_keys(citys)
    
    state_input_elem = driver.find_element_by_xpath("/html/body/div/div/div/div/main/article/div/div/div/div/section[13]/div/div/div/div/div/div[7]/div/form/div/div[25]/div/select/option[{}]".format(states[state]))
    state_input_elem.click()
    
    phone_input_elem = driver.find_element_by_xpath("//*[@id='form-field-4135e28']")
    phone_input_elem.send_keys(phones)
    
    linkedin_input_elem = driver.find_element_by_xpath("//*[@id='form-field-4f77959']")
    linkedin_input_elem.send_keys(linkedins)
    
    apply_button_elem = driver.find_element_by_xpath("//*[@id='post-13580']/div/div/div/div/section[13]/div/div/div/div/div/div[7]/div/form/div/div[32]/button/span/span[2]")
    apply_button_elem.click()    
    sleep(5)
        
log_in_linkedin()

while True:
    if get_perfil_urls():
        break;
    excel_data()
    
for i in range(len(perfil_names)):
    testing(perfil_names[i].split(" ")[0], perfil_emails[i], separator.join(perfil_names[i].split(" ")[1:]), perfil_states[i].split(",")[0], perfil_states[i].split(",")[1], perfil_phones[i].replace("-", "").replace("+55", "").replace("+5555", "").replace(" ", "").replace("(", "").replace(")", ""), perfil_urls[i])
    print(i)
        
