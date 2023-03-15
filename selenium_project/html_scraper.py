import time
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
        self.implicitly_wait(15)

    def login_link(self):
        self.find_element(By.ID, "loginLink").click()
        self.find_element(By.ID, "sessionEmail").send_keys(const.USER_NAME)
        self.find_element(By.ID, "sessionPassword").send_keys(const.PASSWORD)
        time.sleep(2)
        self.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/ng-switch/session-login/form/div[4]/input"
        ).click()

    def land_first_page(self):
        self.get(const.FULL_URL)

    @staticmethod
    def get_info():
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

    @staticmethod
    def check_for_availability(df):
        list_of_times = []
        list_of_ids = []
        looper = True

        for index, row in df.iterrows():
            list_of_times.append(row['Times'])

        for index, row in df.iterrows():
            list_of_ids.append(row['Ids'])

        idx = const.tee_time_list.index(const.WANTED_TIME)

        while looper:
            if const.tee_time_list[idx] in list_of_times:
                id_idx = list_of_times.index(const.tee_time_list[idx])
                final_id = list_of_ids[id_idx]
                final_url = f'https://www.chronogolf.com/club/santa-teresa-golf-club/booking/' \
                            f'?source=club#/teetime/review' \
                            f'?affiliation_type_ids=109214,109214,109214,109214' \
                            f'&teetime_id={final_id}' \
                            f'&nb_holes=18&is_deal=false&source=club&new_user=false'
                return final_url
            else:
                idx += 1

    def land_final_page(self, final_url):
        self.get(final_url)
        time.sleep(3)

        self.find_element(
            By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[1]/booking-confirmation/div/form/'
                      'div[2]/div[1]/reservation-review-terms/label/div/input'
        ).click()

        self.find_element(
            By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[1]/booking-confirmation/div'
                      '/form/div[2]/div[2]/reservation-review-submit-button/button'
        ).click()
