import time 
import random
from datetime import datetime

def sleep_scraper() -> None:
    time.sleep(random.uniform(12,19))


def convert_abbr_month_format(date_str: str) -> str:
    date_obj = datetime.strptime(date_str, "%b %d, %Y")

    return date_obj.strftime("%Y-%m-%d")

def convert_nba_date_to_iso8601(date_str: str) -> str:
    date_obj = datetime.strptime(date_str, "%a, %b %d, %Y")
    return date_obj.strftime("%Y-%m-%d")

def convert_nba_time(time_str: str) -> str:
    stripped_time = time_str.strip()

    stripped_time = stripped_time[ :-1]
    indicator = stripped_time[-1]
    time_split = stripped_time.split(':')
    hour = time_split[0]
    minutes = time_split[1]

    if indicator.lower() == 'a':
        return f"{hour}:{minutes}"
    elif indicator.lower() == 'p':
        return f"{hour + 12}:{minutes}"
    else:
        return time_str


def convert_12hr_to_24hr(time_str: str) -> str:
    stripped_time = time_str.strip()
    if (stripped_time[-2:].upper() in ["AM", "PM"]) and stripped_time[-3] != " ":
        stripped_time = stripped_time[:-2] + " " + stripped_time[-2:]

    if not stripped_time:
        return time_str

    time_obj = datetime.strptime(stripped_time, "%I:%M %p")
    return time_obj.strftime("%H:%M")






