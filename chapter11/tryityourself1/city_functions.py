def city_country(city_name, country_name):
    """Function that returns neatly formatted string of a city and it's country"""
    return f"{city_name.title()}, {country_name.title()}"

def modified_city_country(new_city_name, new_country_name, population):
    """Modified city country function that accepts a third argument"""
    return f"{new_city_name.title()}, {new_country_name.title()} - population {population}"