from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import streamlit as st
import time

#Test Ambuj



driver = webdriver.Edge()
driver = webdriver.Edge(r'')
driver.maximize_window()

def AutoBrouse():
    driver.get("https://braincal.com/")

    #driver.get("https://kuttingchaionline.esdev.in/login ")
    time.sleep(10)

    driver.get("https://braincal.com/11-plus/")

    time.sleep(10)

    driver.get("https://braincal.com/11-plus/11-plus-maths/")

    #driver.get(By.CLASS_NAME, value="w-100")

    
    time.sleep(10)

    driver.get("https://braincal.com/maths_11/level-3/")

    #driver.get(By.CLASS_NAME, value="w-100")

    
    time.sleep(10)

#AutoBrouse()


    driver.get("https://braincal.com/")

    #driver.get("https://kuttingchaionline.esdev.in/login ")
    time.sleep(10)

    driver.get("https://braincal.com/11-plus/")

    time.sleep(10)

    driver.get("https://braincal.com/11-plus/11-plus-maths/")

    #driver.get(By.CLASS_NAME, value="w-100")

    
    time.sleep(10)

    driver.get("https://braincal.com/maths_11/level-3/")

    #driver.get(By.CLASS_NAME, value="w-100")

    
    time.sleep(10)

