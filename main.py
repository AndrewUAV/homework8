"""
This script defines a function to get birthdays per week and provides an example usage.
"""
from datetime import date, timedelta
def get_birthdays_per_week(users: list) -> dict:
    """
    Function for get birthdays per week for the given list of users.
    :param users: List of dictionaries containing user information.
    :return: A dictionary with weekdays as keys and a list of names as values.
    """
    birthdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    days_name = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Monday",
        6: "Monday",
    }

    current_date = date.today()
    delta = timedelta(days=6)
    end_of_week = current_date + delta

    current_year = current_date.year
    current_month = current_date.month

    for user in users:
        birthday = user["birthday"]
        if current_month == 12 and birthday.month == 1:
            birthday_to_check = birthday.replace(year=current_year + 1)
        else:
            birthday_to_check = birthday.replace(year=current_year)

        if current_date <= birthday_to_check <= end_of_week:
            name_of_the_day = days_name[birthday_to_check.weekday()]
            birthdays[name_of_the_day].append(user["name"])
        else:
            continue

    clean_list_of_birthdays = {}
    for key, value in birthdays.items():
        if len(value) > 0:
            clean_list_of_birthdays[key] = value

    return clean_list_of_birthdays
