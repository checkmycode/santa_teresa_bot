
# Santa Teresa Bot

This code was designed to take inputs and automate a website to schedule a tee time. Coupled with Windows Task Scheduler, this code can be ran at 7 A.M., so you don't have to wake up.

## Deployment

To deploy this project run:

Download Python Here:
https://www.python.org/downloads/

    ∙ Make sure to add to PATH // checkbox in first screen
    ∙ Make sure to disable length // checkbox in last screen

Download chromedriver here:
https://chromedriver.chromium.org/downloads

    ∙ Make new folder in C: and name it SeleniumDrivers
        ∙ Extract all files from the downloaded zip to C:\SeleniumDrivers
```bash
  pip install selenium
```
```bash
  pip install pandas
```

# Documentation

## Fill out these parts in constants.py

Date Wanted (XX-XX-XXXX // always add a 0 if single digit (e.g. 01, 02, 03))

    MONTH = '03'
    DAY = '20'
    YEAR = '2023'

How many in your party? // range: 1 - 4 

    PLAYER_COUNT = 4

Uses Military Time (07:00 - 18:52 - make sure time is identical to the tee time list below)

    WANTED_TIME = '07:00'

User Credentials for Santa Teresa Golf Course (chronogolf)

    USER_NAME = 'youremail@email.com'
    PASSWORD = 'password'

Example Tee Times

    tee_time_list = ['07:00', '07:07', '07:15', '07:22', '07:30', '07:37', '07:45', '07:52',
                     '08:00', '08:07', '08:15', '08:22', '08:30', '08:37', '08:45', '08:52',
                     '09:00', '09:07', '09:15', '09:22', '09:30', '09:37', '09:45', '09:52',
                     '10:00', '10:07', '10:15', '10:22', '10:30', '10:37', '10:45', '10:52',
                     '11:00', '11:07', '11:15', '11:22', '11:30', '11:37', '11:45', '11:52',
                     '12:00', '12:07', '12:15', '12:22', '12:30', '12:37', '12:45', '12:52',
                     '13:00', '13:07', '13:15', '13:22', '13:30', '13:37', '13:45', '13:52',
                     '14:00', '14:07', '14:15', '14:22', '14:30', '14:37', '14:45', '14:52',
                     '15:00', '15:07', '15:15', '15:22', '15:30', '15:37', '15:45', '15:52',
                     '16:00', '16:07', '16:15', '16:22', '16:30', '16:37', '16:45', '16:52',
                     '17:00', '17:07', '17:07', '17:22', '17:30', '17:37', '17:45', '17:52',
                     '18:00', '18:07', '18:15', '18:22', '18:30', '18:37', '18:45', '18:52', ]

## Contributing

This project was meant to be cloned and used for your own use case. If you do run into a bug, please let me know!

## Authors

- [@markcuasay](https://github.com/checkmycode)


