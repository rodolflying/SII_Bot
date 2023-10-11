from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os
from datetime import datetime
import locale
from time import sleep

# Set timezone and locale
os.environ['TZ'] = 'America/Santiago'
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')


class SiiAutomation:

    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = self._set_driver()
        self.wait = WebDriverWait(self.driver, 10)  # 10-second implicit wait

    def _set_driver(self):
        options = Options()
        # options.add_argument('headless')
        return webdriver.Chrome(self.driver_path, options=options)

    def countdown(self, t):
        for i in range(t, 0, -1):
            print(i)
            self.wait_for_seconds(1)

    @staticmethod
    def wait_for_seconds(seconds):
        sleep(seconds)

    def login(self, url, username, password):
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rutcntr"]'))).send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="clave"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="bt_ingresar"]').click()
        self.countdown(2)
        # Close pop-up if it appears
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ModalEmergente"]/div/div/div[3]/button'))).click()
        except Exception as e:
            print("No pop up ", str(e))

    def _select_period(self):
        self.countdown(2)
        periodos_container = self.driver.find_element(By.CSS_SELECTOR,'#declaracionPeriodoMes')
        periodos = periodos_container.find_elements(By.TAG_NAME,'option')

        now = datetime.now()
        month = now.month
        past_month = (month-1) if month > 1 else 12

        # Convert month number to Spanish month name
        past_month = datetime.strptime(str(past_month), "%m").strftime("%B")

        self.countdown(2)
        for periodo in periodos:
            if periodo.text.lower() == str(past_month).lower():
                periodos_container.click()
                self.wait.until(EC.visibility_of(periodo)).click()
                break

    def _select_year(self):
        self.countdown(2)
        years_container = self.driver.find_element(By.CSS_SELECTOR,'select[ng-model="declaracion.periodoAnioSeleccionado"]')
        years = years_container.find_elements(By.TAG_NAME,'option')
        now = datetime.now()
        month = now.month
        past_month_year = now.year if month > 1 else now.year-1

        for year in years:
            if year.text == str(past_month_year):
                years_container.click()
                self.wait.until(EC.visibility_of(year)).click()
                break

    def _submit_declaration(self):
        button_container = self.driver.find_element(By.XPATH, '//*[@id="my-wrapper"]/div[2]/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[3]/button')
        button_container.click()
        self.countdown(5)
        try:
            button_container = self.driver.find_element(By.XPATH, '//*[@id="my-wrapper"]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/button')
            button_container.click()
            self.countdown(3)
            send_button_container = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/button[2]')
            send_button_container.click()
            self.countdown(10)
        except Exception as e:
            print("This month it's already OK!", str(e))

    def F29_declaration(self):
        self.countdown(2)
        self.driver.get("https://www4.sii.cl/propuestaf29ui/index.html#/default")
        self._select_period()
        self._select_year()
        self._submit_declaration()

    def close(self):
        self.driver.quit()
    def download_fee_bills(self):
        '''download from the page all bills created in the past and save them in a folder
        Aditionally a csv file with all the info scraped
        '''
        self.driver.get("https://www.sii.cl/servicios_online/1040-1287.html")
        sleep(1)

def main():
    # Main execution
    load_dotenv()
    username = os.getenv("USER_NAME_SPA")
    password = os.getenv("PASSWORD_SPA")

    sii_bot = SiiAutomation(driver_path=r'C:\chromedriver.exe')
    sii_bot.login(url='https://zeusr.sii.cl//AUT2000/InicioAutenticacion/IngresoRutClave.html?https://misiir.sii.cl/cgi_misii/siihome.cgi', username=username, password=password)
    sii_bot.F29_declaration()
    # Other methods can be called here
    sii_bot.close()

if __name__ == '__main__':
    main()