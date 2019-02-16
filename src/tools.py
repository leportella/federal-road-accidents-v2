import re
from datetime import date, datetime

from unidecode import unidecode

def clean_date(dirty_date):
    pattern = '(?:(\d{4}|\d{2})[-/](\d{2})[-/](\d{4}|\d{2}))'
    groups = re.match(pattern, dirty_date).groups()

    if len(groups[0]) == 4:
        year = groups[0]
        month = groups[1]
        day = groups[2]

    if len(groups[2]) == 4:
        year = groups[2]
        month = groups[1]
        day = groups[0]

    if len(groups[0]) == 2 and len(groups[2]) == 2:
        year = '20' + groups[2]
        month = groups[1]
        day = groups[0]

    return date(int(year), int(month), int(day))


def clean_date_and_hour(dirty_date, dirty_hour):
    cleaned_date = clean_date(dirty_date)
    hour, minute, sec = dirty_hour.split(':')

    return datetime(cleaned_date.year, cleaned_date.month, cleaned_date.day,
                    int(hour), int(minute), int(sec))


def clear_string(string):
    return unidecode(str(string).lower().strip())


def period_of_day(hour):
    if hour >= 0 and hour <= 5:
        return 'night'
    if hour >=6 and hour <= 11:
        return 'morning'
    if hour >=12 and hour <=17:
        return 'afternoon'
    if hour >= 18:
        return 'evening'
