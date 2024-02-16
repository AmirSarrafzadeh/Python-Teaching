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
import json
import logging
import requests
import configparser
import pandas as pd
from bs4 import BeautifulSoup
pd.set_option('display.max_columns', 100)


# Create a custom formatter to add the line number to the log
class LineNumberFormatter(logging.Formatter):
    def format(self, record):
        # Get the line number of the calling frame
        record.lineno = getattr(record, 'lineno', 'unknown')
        return super().format(record)


if __name__ == '__main__':
    # Create a custom logger and configure it with the custom formatter
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the formatter and save the logs in the file.log file
    handler = logging.FileHandler("file.log")
    formatter = LineNumberFormatter('%(levelname)s | %(asctime)s | Line %(lineno)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("All the setting of the logging is done correctly.")

    # Read the config.ini file
    try:
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_path)
        logger.info("The config.ini file is read successfully.")
    except Exception as e:
        logger.error(f"Error in reading the config.ini file from directory {config_path}. Error: {e}")
        sys.exit(1)

    # Get the configuration data from the config.ini file
    try:
        url = config['config']['url']
        csvFileName = config['config']['csvFileName']
        sortColumnName = config['config']['sortColumnName']
        nameColumnName = config['config']['nameColumn']
        FamilyNameColumnName = config['config']['FamilyNameColumn']
        txtFileName = config['config']['txtFileName']
        logger.info("The URL is read from the config.ini file.")
    except Exception as e:
        logger.error(f"Error in reading the url from the config.ini file. Error: {e}")
        sys.exit(1)

    # Send a request to the given URL and get the data
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the data and get the JSON data from the HTML using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser').find('table').text.strip()
            data = json.loads(soup)
            logger.info("The request to the URL is successful, and the data is parsed successfully.")

            # Convert the JSON data to a DataFrame and write it to a CSV file
            df = pd.DataFrame(data)
            df.to_csv(f'{csvFileName}', index=False)
            logger.info(f"The data is written to the {csvFileName} file successfully.")

            # Sort the DataFrame by the created_at column
            dfSorted = df.sort_values(by=f'{sortColumnName}')
            logger.info(f"The DataFrame is sorted by the {sortColumnName} column successfully.")

            # Get the name and family name of the first user
            firstUserName = dfSorted.iloc[0][f'{nameColumnName}']
            firstUserFamilyName = dfSorted.iloc[0][f'{FamilyNameColumnName}']
            logger.info(f"The name and family name of the first user are extracted successfully.")

            # Write name and family name of the first user to a text file
            with open(txtFileName, 'w') as file:
                file.write(f"Hi there!\n\n")
                file.write("This is just a simple project to learn python")
                file.write(f"Name of the first user is: {firstUserName}\n")
                file.write(f"Family Name of the first user is: {firstUserFamilyName}\n\n")
                file.write(f"Thank you for your time!\n")

            logger.info(f"The name and family name of the first user are written to the {txtFileName} file successfully.")
        else:
            logger.error(f"The request to the URL is not successful. Status code: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        logger.error(f"Error in sending the request to the URL. Error: {e}")
        print(e)
        sys.exit(1)


