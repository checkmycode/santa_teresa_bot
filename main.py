from selenium_project.html_scraper import Parser
import time

with Parser() as bot:
    bot.land_first_page()
    time.sleep(1000)
