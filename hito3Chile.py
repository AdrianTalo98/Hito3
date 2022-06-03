import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import random
import requests
import json



import names #Generamos nombres aleatorios
from itertools import cycle

from selenium.webdriver.support.wait import WebDriverWait


def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

ser = Service("./chromedriver")
op = webdriver.ChromeOptions()
op.add_argument("--incognito")

url = "https://www.lapolar.cl/"



#Creamos una cuenta
driver = webdriver.Chrome(service=ser, options=op)

driver.get(url)
driver.maximize_window()


register = driver.find_element(By.CSS_SELECTOR, 'div.header-user')
register.click()
registerBtn = driver.find_element(By.PARTIAL_LINK_TEXT,'Registrarse')
registerBtn.click()
firstName = names.get_first_name('male')
lastName = names.get_last_name()
number = random.randint(10**7,10**8)
rut = random.randint(1000000,3000000)
rut = int(str(rut) + str(digito_verificador(rut)))



correo = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1').json()[0]
randomPass = 'H3JAJAJW1L__'
print(correo)
#Guardamos como json el user creado
userTemp ={
    "name" : firstName,
    "last" : lastName,
    "number" : number,
    "rut" : rut,
    "correo" : correo,
    "contra" : randomPass
}
#print(userTemp)
# Serializing json
json_object = json.dumps(userTemp, indent = 6)
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)


driver.find_element(By.NAME,'dwfrm_profile_customer_firstname').send_keys(firstName)
driver.find_element(By.NAME,'dwfrm_profile_customer_lastname').send_keys(lastName)
driver.find_element(By.NAME,'dwfrm_profile_customer_phone').send_keys(number)
driver.find_element(By.NAME,'dwfrm_profile_customer_rut').send_keys(rut)
driver.find_element(By.NAME,'dwfrm_profile_customer_email').send_keys(correo)
driver.find_element(By.CSS_SELECTOR,'label.custom-control-label.account-dash__label.account-dash__gender-label').click()

driver.find_element(By.NAME,'dwfrm_profile_login_password').send_keys(randomPass)
driver.find_element(By.NAME,'dwfrm_profile_login_passwordconfirm').send_keys(randomPass)

driver.find_element(By.XPATH,'//*[@id="register"]/form/button').click()
#print(driver.find_element(By.CSS_SELECTOR, 'button.account-dash__submit-btn'))


#Hasta aqui generamos el usario y guardamos los datoss
time.sleep(5)
driver.quit()


#input("Presionar enter para logearse")
#--------------------------------------------------- Aqui termina la creacionn -------------------
#Haremos el login

driver = webdriver.Chrome(service=ser, options=op)
driver.maximize_window()
driver.get(url)

f = open('sample.json')
data = json.load(f)
corrreo = data['correo']
contr = data['contra']
#print(corrreo)
driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div[2]/div/div[4]/div[1]/div[2]/div/a/span[2]').click()
driver.find_element(By.XPATH,'//*[@id="login-form-email"]').send_keys(corrreo)
driver.find_element(By.XPATH,'//*[@id="login-form-password"]').send_keys(contr)

driver.find_element(By.XPATH,'//*[@id="login"]/form/div[5]/button').click()

time.sleep(5)

driver.quit()

#input("Presionar enter para restablecer")
#--------------------------------------------------- Aqui termina el Login -------------------

#Restablecimiento

driver = webdriver.Chrome(service=ser, options=op)
driver.maximize_window()
driver.get(url)
driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div[2]/div/div[4]/div[1]/div[2]/div/a/span[2]').click()
driver.find_element(By.XPATH,'//*[@id="login"]/form/div[6]/a').click()
time.sleep(0.5)# Podemos variarlo
driver.find_element(By.XPATH,'//*[@id="reset-password-email"]').send_keys(corrreo)
driver.find_element(By.XPATH,'//*[@id="submitEmailButton"]').click()

time.sleep(20) #Esperaremos un ratico

driver.quit()


login = corrreo.split('@')[0]

domain = corrreo.split('@')[1]
urlCorreo = "https://www.1secmail.com/api/v1/?action=getMessages&login="+login+"&domain="+domain #Aqui accedemos al url a partir del correo

aers = requests.get(urlCorreo).json()
tam = len(aers)-1
id = aers[tam]['id'] #Obtenemos el ultimo ID, que seria el de restablecer...

urlLeerCorreo = "https://www.1secmail.com/api/v1/?action=readMessage&login="+login+"&domain="+domain+"&id="+str(id)
print("ver correo",urlLeerCorreo)
leer = requests.get(urlLeerCorreo).json()['body']
index = leer.find("Haz click")
token = leer[index-(3+45):index-2]
print("----")
#print(token)
urlFinalFinal = 'https://www.lapolar.cl/Configurar-clave/?token='+token
print(urlFinalFinal)

driver = webdriver.Chrome(service=ser, options=op)
driver.maximize_window()
driver.get(urlFinalFinal)

time.sleep(5)


contrN = 'jJ2JSAH1_Q'

#Guardamos la nueva pass

with open("sample.json", "r") as outfile:
    data = json.load(outfile)
data['contra'] = contrN
with open("sample.json", "w") as outfile:
    json.dump(data, outfile)


driver.find_element(By.XPATH,'//*[@id="newPassword"]').send_keys(contrN)
driver.find_element(By.XPATH,'//*[@id="newPasswordConfirm"]').send_keys(contrN)

driver.find_element(By.CSS_SELECTOR,'button.account-resetpassword-mail__save-button.lp-button.lp-button--inverted.ms-full-width').click()

time.sleep(10)

driver.quit()

#input("Presionar enter para modificar pass")
#--------------------------------------------------- Aqui termina la Recuperacion -------------------

#Modificacion contraseña

#LLamamos al login

driver = webdriver.Chrome(service=ser, options=op)
driver.maximize_window()
driver.get(url)

f = open('sample.json')
data = json.load(f)
corrreo = data['correo']
contr = data['contra']
#print(corrreo)
driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div[2]/div/div[4]/div[1]/div[2]/div/a/span[2]').click()
driver.find_element(By.XPATH,'//*[@id="login-form-email"]').send_keys(corrreo)
driver.find_element(By.XPATH,'//*[@id="login-form-password"]').send_keys(contr)

driver.find_element(By.XPATH,'//*[@id="login"]/form/div[5]/button').click()

time.sleep(2)#Modificar esto en caso de..
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/ul/li[2]/div[2]/a').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/form/div[1]/input').send_keys(contr)

newnew = 'H2dsad___1'
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/form/div[2]/input').send_keys(newnew)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/form/div[3]/input').send_keys(newnew)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/form/button').click()

#Guardamos la nueva pass

with open("sample.json", "r") as outfile:
    data = json.load(outfile)
data['contra'] = contrN
with open("sample.json", "w") as outfile:
    json.dump(data, outfile)
time.sleep(5)


driver.quit()



















