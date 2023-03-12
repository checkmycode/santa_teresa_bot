from selenium import webdriver
import os
import selenium_project.constants as const


class Parser(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Parser, self).__init__()

    def land_first_page(self):
        self.get(const.FULL_URL)
