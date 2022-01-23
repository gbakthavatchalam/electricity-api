import datetime


def string_to_date(string, format="%Y-%m-%d %H:%M:%SZ"):
    return datetime.datetime.strptime(string, format).date()
