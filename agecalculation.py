
"""
my fancy age calculation

"""

def calculate_age(birthdate, today):
    """
        my fancy age calculation

    """
    year_difference = today.year - birthdate.year
    no_birthday_this_year = (today.month, today.day) < (birthdate.month, birthdate.day)

    if no_birthday_this_year :
        return year_difference -1
    return year_difference
