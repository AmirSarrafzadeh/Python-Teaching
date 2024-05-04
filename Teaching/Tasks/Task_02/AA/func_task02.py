import requests 
from bs4 import BeautifulSoup
import logging



#    Start finde most login ip
def def_ip(sum_ip):
    ip_check = ''
    number = 0
    for ip in sum_ip:

        #  Find the largest IP
        if sum_ip[ip] > number:
            number = sum_ip[ip] 
            ip_check = str(ip)

        #  add if the number of IP entries is equal to the largest 
        elif sum_ip[ip] == number:
            ip_check += str(' , '+ip)

    return ip_check

#    Finish Find Ip






def def_json(link):
    logging.debug(' Start ')
    #      If cant read file, write json file

    print(' not find json file \n wait...')

    # Link git for extract json
    link_website =  requests.get(link).text


    try :


            # filter html code 
        bs = BeautifulSoup(link_website, 'html.parser')

        logging.debug(' take text html code in website')

            # Extract json in td
        # TODO import json
        # TODO soup = bs.find('table').text.strip()
        # TODO data = json.loads(soup)
        td_tag_json = bs.find_all('td' , class_="blob-code blob-code-inner js-file-line")
        logging.debug(' filter td tag in html')

            # open file for Write json
        data = open('data_json_task2.json', 'w+' )

            # Find raw json
        for raw in td_tag_json:
             data.write(raw.text+'\n')

        logging.debug(' filter json in td tag')


            # Read json file
        data = open('data_json_task2.json', 'r+' )
        data = data.read()

        logging.debug(' write in json file and read json')

        return data


    except:
        logging.warning(' eror cant write json file')

