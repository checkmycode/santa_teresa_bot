BASE_URL = 'https://www.chronogolf.com/club/santa-teresa-golf-club#?'
MONTH = '03'
DAY = '15'
YEAR = '2023'
COURSE_ID = 'course_id=22913&'
HOLE_COUNT = 'nb_holes=18&'
PLAYER_COUNT = 4

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
