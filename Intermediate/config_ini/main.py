"""
Read JSON file from a url and write the data into a CSV file

Author: Amir Sarrafzadeh Arasi
Date: 2024-02-16

Purpose: This script reads the data from a JSON file in the given url and writes the data into a CSV file.

Steps:
1. Create a custom logger and configure it with the custom formatter
2. Read the config.ini file
3. Send a request to the given URL and get the data
4. Parse the data and get the JSON data from the HTML using BeautifulSoup
5. Convert the JSON data to a DataFrame and write it to a CSV file
6. Sort the DataFrame by the created_at column
7. Get the name and family name of the first user and write it to a text file
"""

# Import the necessary libraries
import os
import sys
import logging
import configparser


if __name__ == '__main__':

    # Create a custom logger and configure it with the custom formatter
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='file.log',
                        filemode='w')

    # Read the config.ini file
    try:
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_path)
        logging.info("The config.ini file is read successfully.")
    except Exception as e:
        logging.error(f"Error in reading the config.ini file from directory with Error: {e}")
        sys.exit(1)


    # Get the information from the config.ini file
    try:
        name = config['config']['name']
        surname = config['config']['surname']
        age = config['config']['age']
        nationality = config['config']['nationality']
        favorite_color = config['config']['favorite_color']
        favorite_food = config['config']['favorite_food']
        username = config['credentials']['username']
        password = config['credentials']['password']
        email = config['contact']['email']
        phone = config['contact']['phone']
        address = config['contact']['address']
        logging.info("The URL is read from the config.ini file.")
    except Exception as e:
        logging.error(f"Error in reading the url from the config.ini file. Error: {e}")
        sys.exit(1)


    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Age: {age}")
    print(f"nationality: {nationality}")
    print(f"Favorite Color: {favorite_color}")
    print(f"Favorite Food: {favorite_food}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Address: {address}")



