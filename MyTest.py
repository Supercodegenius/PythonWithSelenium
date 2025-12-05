from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()
driver = webdriver.Edge(r'')
driver.maximize_window()

"""
driver.get('https://kuttingchaionline.esdev.in/login')
nametext = driver.find_element(By.ID, value="name")
nametext.send_keys("TestName11") 

nametext = driver.find_element(By.ID, value="email")
nametext.send_keys("Testemail@gmail.com") 

phone = "07896756715"
nametext = driver.find_element(By.ID, value="phone_no")
nametext.send_keys(phone)



passwor = driver.find_element(By.ID, value="password")
passwor.send_keys("12345678")

compasswor = driver.find_element(By.ID, value="password-confirm")
compasswor.send_keys("12345678")

time.sleep(10)
regButton  = driver.find_element(By.CLASS_NAME, value="row container-fluid mx-auto place-items-center mt-5")
regButton.click()

time.sleep(10)
"""

def NewReg():
    driver = webdriver.Edge()
    driver = webdriver.Edge(r'')
    driver.maximize_window()

    driver.get('https://kuttingchaionline.esdev.in/login')
    nametext = driver.find_element(By.ID, value="name")
    nametext.send_keys("TestName11") 

    nametext = driver.find_element(By.ID, value="email")
    nametext.send_keys("Testemail@gmail.com") 

    phone = "07896756715"
    nametext = driver.find_element(By.ID, value="phone_no")
    nametext.send_keys(phone)



    passwor = driver.find_element(By.ID, value="password")
    passwor.send_keys("12345678")

    compasswor = driver.find_element(By.ID, value="password-confirm")
    compasswor.send_keys("12345678")

    time.sleep(10)
    regButton  = driver.find_element(By.CLASS_NAME, value="row container-fluid mx-auto place-items-center mt-5")
    regButton.click()

    time.sleep(10)




def LoginToShopOwner():

    driver.get('https://kuttingchaionline.esdev.in/login')
    emailtext = driver.find_element(By.ID, value="email")
    emailtext.send_keys("owner@kutting.co.uk") 

    emailtext = driver.find_element(By.ID, value="password")
    emailtext.send_keys("12345678") 

    time.sleep(10)
    logButton  = driver.find_element(By.CLASS_NAME, value="col-md-6 col-12 mx-auto border-none resister_btn")
    logButton.click()

    time.sleep(10)



LoginToShopOwner()

#print("Ambuj")