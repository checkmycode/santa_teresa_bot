from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import selenium_project.constants as const
import requests
import pandas as pd


class Parser(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Parser, self).__init__()

    def login_link(self):
        self.find_element(By.ID, "loginLink").click()
        self.find_element(By.ID, "sessionEmail").send_keys(const.USER_NAME)
        self.find_element(By.ID, "sessionPassword").send_keys(const.PASSWORD)
        self.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/ng-switch/session-login/form/div[4]/input"
        ).click()

    def land_first_page(self):
        self.maximize_window()
        self.get(const.FULL_URL)
        self.implicitly_wait(15)

    def get_info(self):
        page = requests.get(const.JSON_URL)
        tee_times = []
        time_ids = []
        out_of_caps = []
        for i in range(0, len(page.json())):
            start_times = (page.json()[i]['start_time'])
            tee_times.append(start_times)

        for i in range(0, len(page.json())):
            ids = (page.json()[i]['id'])
            time_ids.append(ids)

        for i in range(0, len(page.json())):
            out_of_capacity = (page.json()[i]['out_of_capacity'])
            out_of_caps.append(out_of_capacity)

        data = {
            'Times': tee_times,
            'Ids': time_ids,
            'Out_of_Cap': out_of_caps,
        }

        df = pd.DataFrame(data)
        for index, row in df.iterrows():
            if row['Out_of_Cap']:
                df = df.drop(index)
            return df

    def check_for_availability(self, n, df):
        print('starting this now')
        for index, row in df.iterrows():
            if row['Times'] == const.WANTED_TIME:
                final_id = row['Ids']
                print(final_id)
                final_url = f'https://www.chronogolf.com/club/santa-teresa-golf-club/booking/?source=club#/teetime/review?affiliation_type_ids=109214,109214,109214,109214&teetime_id={final_id}&nb_holes=18&is_deal=false&source=club&new_user=false'
                self.get(final_url)
        else:
            n += 1
            self.check_for_availability(n, df)


