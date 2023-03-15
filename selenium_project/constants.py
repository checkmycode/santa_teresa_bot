# Date Wanted
MONTH = '03'
DAY = '21'
YEAR = '2023'

# How many in your party?
PLAYER_COUNT = 3

# Uses Army Time (07:00 - 18:00 - pick from tee time list below)
WANTED_TIME = '08:00'

# User Credentials
USER_NAME = 'markcuasay@gmail.com'
PASSWORD = 'Golf408$'

# This picks Santa Teresa and 18 hole only -- do not touch anything below this line
BASE_URL = 'https://www.chronogolf.com/club/santa-teresa-golf-club#?'
COURSE_ID = 'course_id=22913&'
HOLE_COUNT = 'nb_holes=18&'


# Adjust date
DATE = f'date={YEAR}-{MONTH}-{DAY}&'

# Adjust Player Count
if PLAYER_COUNT == 4:
    PLAYER_COUNT = 'affiliation_type_ids=109214,109214,109214,109214'
elif PLAYER_COUNT == 3:
    PLAYER_COUNT = 'affiliation_type_ids=109214,109214,109214'
elif PLAYER_COUNT == 2:
    PLAYER_COUNT = 'affiliation_type_ids=109214,109214'
elif PLAYER_COUNT == 1:
    PLAYER_COUNT = 'affiliation_type_ids=109214'

FULL_URL = BASE_URL + DATE + COURSE_ID + HOLE_COUNT + PLAYER_COUNT
JSON_URL = f'https://www.chronogolf.com/marketplace/clubs/18876/teetimes?date={YEAR}-{MONTH}-{DAY}' \
           f'&course_id=22913&affiliation_type_ids%5B%5D=109214&affiliation_type_ids%5B%5D=109214' \
           f'&affiliation_type_ids%5B%5D=109214&affiliation_type_ids%5B%5D=109214&nb_holes=18'

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

n = tee_time_list.index(WANTED_TIME)
