from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from time import sleep
from dotenv import load_dotenv
import os
import bs4
import requests
import json

load_dotenv()
# Load the environment variables
username = os.getenv("USER_NAME_PERSON")
password = os.getenv("PASSWORD_PERSON")

def countdown(t):
    '''Countdown'''
    # Countdown
    for i in range(t, 0, -1):
        print(i)
        sleep(1)

def set_driver():
    '''Set the browser driver'''
    # Create a new instance of the browser driver and open the desired webpage
    #headless
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome(r'C:\chromedriver.exe', options=options) # replace with your own path
    return driver


def login(driver, username='', password=''):
    # Enter the username and password
    print(username, password)
    driver.find_element(By.XPATH,'//*[@id="rutcntr"]').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="clave"]').send_keys(password)
    driver.find_element(By.XPATH,'//*[@id="bt_ingresar"]').click()
    sleep(1)
    #close pop up
    try:
        driver.find_element(By.XPATH,'//*[@id="ModalEmergente"]/div/div/div[3]/button').click()
    except Exception as e:
        print("No pop up ", str(e))
    return driver

def issuance_fee_bill(driver):
    driver.get("https://www.sii.cl/servicios_online/1040-1287.html")
    sleep(1)
    #click on button
    driver.find_element(By.XPATH,'//*[@id="modalInforma"]/div/div/div[3]/button').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="headingOne"]/h4/a').click()
    sleep(1)
    #por contribuyente
    # driver.find_element(By.XPATH,'//*[@id="collapseOne"]/div/div/ul/li[1]/a').click()
    # por contribuyente usando datos anteriores
    driver.find_element(By.XPATH,'//*[@id="collapseOne"]/div/div/ul/li[2]/a').click()
    #

    # /html/body/div[2]/center/table[2]/tbody/tr[5]/td/div/center/form/table/tbody/tr[4]/td/ul/li[4]/input[1]

    sleep(20)
    return driver

def download_fee_bills(driver):
    '''download from the page all bills created in the past and save them in a folder
    Aditionally a csv file with all the info scraped
    '''

def F29_declaration(driver):
    pass

# search = user_input()
driver=None
# 1) Set the browser driver
driver=set_driver()

driver.get('https://zeusr.sii.cl//AUT2000/InicioAutenticacion/IngresoRutClave.html?https://misiir.sii.cl/cgi_misii/siihome.cgi')

driver = login(driver,username=username,password=password)

driver = issuance_fee_bill(driver)



