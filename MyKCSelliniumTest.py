#Test 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#import org.openqa.selenium.Keys;


driver = webdriver.Edge()
driver = webdriver.Edge(r'')
driver.maximize_window()


def AUtoLogin():
    driver.get("https://kuttingchaionline.esdev.in/login")

    #driver.get("https://kuttingchaionline.esdev.in/login ")
    time.sleep(10)

    #driver.get(By.CLASS_NAME, value="w-100")

    regButton  = driver.find_element(By.XPATH, value="/html/body/section/div[2]/div[2]/div[1]/div/form/div[4]/input")
    time.sleep(10)
    emailnametext = driver.find_element(By.XPATH, value='/html/body/section/div[2]/div[2]/div[1]/div/form/div[1]/div/input')
    emailnametext.send_keys("owner@kuttingchai.co.uk") 


    compasswor = driver.find_element(By.XPATH, value="/html/body/section/div[2]/div[2]/div[1]/div/form/div[2]/div/input")
    compasswor.send_keys("12345678")
    time.sleep(10)

    regButton.submit()

    time.sleep(10)


def OnlineOrder():
    driver1 = webdriver.Edge()
    driver1 = webdriver.Edge(r'')
    driver1.maximize_window()
    driver1.get("https://kuttingchaionline.esdev.in/catalog/cart")

    #driver.get("https://kuttingchaionline.esdev.in/login ")
    time.sleep(10)

    #driver.get(By.CLASS_NAME, value="w-100")

    regButton  = driver1.find_element(By.XPATH, value="/html/body/section/div/div[1]/div/div/div/div[1]/div[4]/div/button/a")
    time.sleep(10)    
    regButton.click()
    time.sleep(10)

    driver1.get("https://kuttingchaionline.esdev.in/catalog/category")
    time.sleep(10)    
    regButton.click()
    time.sleep(10)

"""
    regButton  = driver1.find_element(By.XPATH, value="/html/body/section/div/div[1]/div/div/div/div[1]/div[4]/div/button/a")
    time.sleep(10)    
    regButton.click()
    time.sleep(10)

    regButton  = driver1.find_element(By.XPATH, value="/html/body/section/div/div[1]/div/div/div/div[1]/div[4]/div/button/a")
    time.sleep(10)    
    regButton.click()
    time.sleep(10)
"""

 

#OnlineOrder()



    # driver = webdriver.Edge()
    # driver = webdriver.Edge(r'')
    # driver.maximize_window()


def KCreg():
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

# KCreg()

def KCweb():
    #driver.get('https://kuttingchaionline.esdev.in')
    # driver.get('https://kuttingchaionline.esdev.in/catalog/gallery')
    # driver.get('https://kuttingchaionline.esdev.in/catalog/video')
    #driver.get('https://kuttingchaionline.esdev.in/catalog/category')
    
    #time.sleep(20)
    driver = webdriver.Edge(r'')
    driver.get("https://kuttingchaionline.esdev.in")

    link_element = driver.find_element(By.XPATH, value="/html/body/header/div/div[2]/ul/li[3]/div/ul/li[1]/a/span[2]")

    print(link_element)
    

    time.sleep(20)


   

#KCweb()


