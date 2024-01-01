from datetime import date, datetime, timedelta

def get_birthdays_per_week(users: list) -> dict:
    get_date_today = date.today()
    get_next_week = get_date_today + timedelta(days=7)

    # create dick for birthdays dates
    get_users_birthdays = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday",
                                             "Friday", "Saturday", "Sunday"]}

    if not users:
        return get_users_birthdays

    for user in users:
        if isinstance(user, dict):
            birthday = user.get("birthday")

            if isinstance(birthday, datetime):
                birthday = birthday.date()

            # Checking if the birthday has not occurred yet in the current year
            birthday_this_year = date(get_date_today.year, birthday.month, birthday.day)

            if get_date_today <= birthday_this_year < get_next_week:
                day_of_week = birthday_this_year.strftime("%A")  # Get the day of the week as a string

                if day_of_week in ["Saturday", "Sunday"]:
                    day_of_week = "Monday"

                get_users_birthdays[day_of_week].append(user.get("name"))

    # Remove days without birthdays
    get_users_birthdays = {day: names for day, names in get_users_birthdays.items() if names}

    return get_users_birthdays



if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")