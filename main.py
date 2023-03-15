from selenium_project.html_scraper import Parser
import time


def main():
    with Parser() as bot:
        bot.land_first_page()
        bot.login_link()
        bot.get_info()
        bot.check_for_availability(bot.get_info())
        bot.land_final_page(bot.check_for_availability(bot.get_info()))
        time.sleep(10)


if __name__ == '__main__':
    main()
