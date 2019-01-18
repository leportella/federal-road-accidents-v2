from datetime import date, datetime

from tools import clean_date, clean_date_and_hour


def test_clean_dates():
    assert clean_date('2017/01/01') == date(2017, 1, 1)
    assert clean_date('2017-01-01') == date(2017, 1, 1)
    assert clean_date('01-01-2017') == date(2017, 1, 1)
    assert clean_date('17-01-01') == date(2017, 1, 1)
    assert clean_date('17/01/01') == date(2017, 1, 1)


def test_clean_date_and_hour():
    cleaned_date = clean_date_and_hour('2017-01-01', '02:10:37')
    assert cleaned_date == datetime(2017, 1, 1, 2, 10, 37)
