from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.04"},
    {"name": "John1 Doe", "birthday": "1985.01.03"},
    {"name": "John2 Doe", "birthday": "1985.06.15"},
    {"name": "John3 Doe", "birthday": "1985.06.21"},
    {"name": "Jane Smith", "birthday": "1990.06.17"}
]

date_format = "%Y.%m.%d"

# as_of_date parameter for testing of function as of specified date(near next year), todays by default
def get_upcoming_birthdays(users: list, as_of_date: datetime.date = datetime.today().date()) -> list:
    
    result = list()

    for user in users:
        birth_date = datetime.strptime(user["birthday"], date_format).date()
        birth_date_this_year = birth_date.replace(year = as_of_date.year)
        if birth_date_this_year < as_of_date: # move to next year
            birth_date_this_year = birth_date.replace(year = as_of_date.year + 1)
        
        if (birth_date_this_year - as_of_date).days <= 7:

            day = birth_date_this_year.isoweekday()
            match day:
                case 6:
                    congratulation_date = birth_date_this_year + timedelta(days=2)
                case 7:
                    congratulation_date = birth_date_this_year + timedelta(days=1)
                case _:
                    congratulation_date = birth_date_this_year
                    
            result.append(
                {
                    "name": user["name"],
                    "congratulation_date": datetime.strftime(congratulation_date, date_format)
                }
            )

    return result

print(get_upcoming_birthdays(users))
print(get_upcoming_birthdays(users, as_of_date = datetime(2026, 12, 30).date()))