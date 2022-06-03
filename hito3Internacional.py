import time

from selenium import webdriver
from selenium.webdriver import Keys
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

url = "https://www.westerndigital.com/es-es"

#Creamos una cuenta
driver = webdriver.Chrome(service=ser, options=op)

driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/div[2]/button/span').click()
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div[1]/a').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div[1]/div/div/div/div/form/div[2]/select').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div[1]/div/div/div/div/form/div[2]/select').send_keys(Keys.DOWN)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div[1]/div/div/div/div/form/div[2]/select').send_keys(Keys.ENTER)

firstName = names.get_first_name('male')
lastName = names.get_last_name()
correo = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1').json()[0]
randomPass = 'H3JAJAJW1L__'
#Guardamos como json el user creado
userTemp ={
    "name" : firstName,
    "last" : lastName,
    "correo" : correo,
    "contra" : randomPass
}
json_object = json.dumps(userTemp, indent = 4)
# Writing to sample.json
with open("sampleInt.json", "w") as outfile:
    outfile.write(json_object)


driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div[1]/div/div/div/div/form/div[3]/div[2]/div[1]/div[1]/div/input').send_keys(firstName)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div[1]/div/div/div/div/form/div[3]/div[2]/div[1]/div[2]/div/input').send_keys(lastName)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div[1]/div/div/div/div/form/div[3]/div[2]/div[2]/input').send_keys(correo)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div[1]/div/div/div/div/form/div[3]/div[2]/div[3]/input').send_keys(randomPass)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div[1]/div/div/div/div/form/div[3]/div[2]/div[4]/div[1]/label/span[1]').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div[1]/div/div/div/div/form/div[3]/div[2]/div[6]/button').click()

time.sleep(5)
driver.quit()


#input("Presionar enter para logearse")
#--------------------------------------------------- Aqui termina la creacionn -------------------

f = open('sampleInt.json')
data = json.load(f)
correo = data['correo']
randomPass = data['contra']

driver = webdriver.Chrome(service=ser, options=op)
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/div[2]/button/span').click()
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[1]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[1]/div[1]/form/div[2]/input').send_keys(correo)
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[1]/div[1]/form/div[3]/input').send_keys(randomPass)
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[1]/div[1]/form/button').click()

time.sleep(5)
driver.quit()
#input("Presionar enter para restablecer")
#--------------------------------------------------- Aqui termina el Login -------------------



f = open('sampleInt.json')
data = json.load(f)
correo = data['correo']
randomPass = data['contra']
print(correo)
driver = webdriver.Chrome(service=ser, options=op)
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/div[2]/button/span').click()
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[1]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[1]/div[1]/form/div[4]/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div/form/div[2]/div/input').send_keys(correo)
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div/form/div[2]/button').click()

time.sleep(20) #Esperaremos un ratico,,, AQUI ES NECECSARIO ESPERAR, YA QUE TARDA EN ENTREGAR EL TOKEN,...
#SI NO ESPERAMOS, MUERE EL SCRIPTT

driver.quit()

login = correo.split('@')[0]

domain = correo.split('@')[1]
urlCorreo = "https://www.1secmail.com/api/v1/?action=getMessages&login="+login+"&domain="+domain #Aqui accedemos al url a partir del correo
print(urlCorreo)
aers = requests.get(urlCorreo).json()
tam = len(aers)-1
id = aers[0]['id'] #Obtenemos el ultimo ID, que seria el de restablecer...

urlLeerCorreo = "https://www.1secmail.com/api/v1/?action=readMessage&login="+login+"&domain="+domain+"&id="+str(id)
print("ver correo",urlLeerCorreo)
leer = requests.get(urlLeerCorreo).json()['body']
index = leer.find("token")#Index+6 esta perfect!!
indexFin = leer.find("www.westerndigital.com/es/es/my-account/update-password")
token = leer[index+6:indexFin-9]
#print(token)

urlFinFin = "https://www.westerndigital.com/es-es/store/login/pw/change?token="+token
print(urlFinFin)

driver = webdriver.Chrome(service=ser, options=op)
driver.maximize_window()
driver.get(urlFinFin)

time.sleep(5)
newPass = "H2ksldjasd___11Q"
with open("sampleInt.json", "r") as outfile:
    data = json.load(outfile)
data['contra'] = newPass
with open("sampleInt.json", "w") as outfile:
    json.dump(data, outfile)

driver.find_element(By.NAME,'pwd').send_keys(newPass)
driver.find_element(By.NAME,'checkPwd').send_keys(newPass)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div/form/button[1]').click()

time.sleep(5)

driver.quit()

#input("Presionar enter para modificar pass")
#--------------------------------------------------- Aqui termina la Recuperacion -------------------

#Modificacion contraseña
#LLamamos al login
f = open('sampleInt.json')
data = json.load(f)
correo = data['correo']
randomPass = data['contra']

driver = webdriver.Chrome(service=ser, options=op)
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/div[2]/button/span').click()
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[1]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[1]/div[1]/form/div[2]/input').send_keys(correo)
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[1]/div[1]/form/div[3]/input').send_keys(randomPass)
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[1]/div[1]/form/button').click()

time.sleep(5)

driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/button/span').click()
driver.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div[1]/section/div/div/section/div/div[1]/section/div/div[1]/section/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/ul[1]/li[1]/a').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div/div[2]/nav/ul/li[2]/a').click()


driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div/div[3]/div/div/div[3]/div/div/div[1]/div/div[2]/button').click()

driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[1]/input').send_keys(randomPass)
newnewpass = "Jk2ksda__1"

driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[2]/input').send_keys(newnewpass)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[3]/input').send_keys(newnewpass)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/section/div/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/form/div[4]/button[1]').click()
with open("sampleInt.json", "r") as outfile:
    data = json.load(outfile)
data['contra'] = newnewpass
with open("sampleInt.json", "w") as outfile:
    json.dump(data, outfile)


time.sleep(10)
driver.quit()