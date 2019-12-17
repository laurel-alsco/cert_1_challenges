# Author: Laurel Miller
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Searches:
    def __init__(self, driver):
        self.driver = driver

    def find_car(self, make):
        wait = WebDriverWait(self.driver, 200)
        search = self.driver.find_element_by_id('input-search')
        search.send_keys(make)
        for button in self.driver.find_elements_by_xpath \
                ('//*[@id="search-form"]//button[@type = "submit" and @ng-click = "search()"]'):
            button.click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//tbody//tr')))



