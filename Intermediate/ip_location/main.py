"""
    This script uses the requests library to get the user's location based on their IP address.

    Author : Amir Sarrafzadeh Arasi
    Date : 2024-04-17

    This script uses the requests library to get the user's location based on their IP address.
"""

# Import the requests libraries
import requests
import pycountry
from pycountry_convert import country_alpha2_to_continent_code

# Create a dictionary to map the continent code to the continent name
continent_dictionary = {
    'AF': 'Africa',
    'AS': 'Asia',
    'EU': 'Europe',
    'NA': 'North America',
    'SA': 'South America',
    'OC': 'Oceania',
    'AN': 'Antarctica'
}


# Create a function to get the user's location
def get_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        city = data.get('city', '')
        country_code = data['country']
        country_name = pycountry.countries.get(alpha_2=country_code).name
        if country_name:
            continent_code = country_alpha2_to_continent_code(country_code)
            continent = continent_dictionary.get(continent_code)
        else:
            continent = None
        return city, country_name, continent
    except Exception as e:
        print("Error:", e)
        return None, None


if __name__ == "__main__":
    user_city, user_country, user_continent = get_location()
    if user_city and user_country:
        print("You are currently in {}, {}, {}".format(user_city, user_country, user_continent))
    else:
        print("Unable to determine your location.")


