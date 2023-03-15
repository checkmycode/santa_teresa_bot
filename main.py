from selenium_project.html_scraper import Parser
import time
import selenium_project.constants as const

def main():
    with Parser() as bot:
        # bot.land_first_page()
        # bot.login_link()
        bot.land_first_page()
        bot.get_info()
        bot.check_for_availability(const.n, bot.get_info())
        time.sleep(1000)

if __name__ == '__main__':
    main()