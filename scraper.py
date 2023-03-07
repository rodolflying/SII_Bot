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
username = os.getenv("USER_NAME_RODO")
password = os.getenv("PASSWORD_RODO")

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


search = user_input()
driver=None
# 1) Set the browser driver
driver=set_driver()

driver.get('https://zeusr.sii.cl//AUT2000/InicioAutenticacion/IngresoRutClave.html?https://misiir.sii.cl/cgi_misii/siihome.cgi')
driver = login(driver,username=username,password=password)
countdown(10)

