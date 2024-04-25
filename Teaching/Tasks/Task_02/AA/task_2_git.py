from bs4 import BeautifulSoup
from  func_task02 import def_ip,def_json
import json 
import sys
import requests 
import logging
from configparser import ConfigParser

logging.basicConfig(level=logging.DEBUG, filename='task_2.log', filemode='a+', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info('# run task_2_git\n-----------------------------------------------------------')


loads_ini = ConfigParser()
loads_ini.read('app.ini')
config_link = loads_ini['Data']['link']

try :
    # check response == 200
    if requests.get(config_link).status_code != 200:

        logging.debug(' internet cant connect')
        sys.exit()

    logging.info(' internet connect')
    try:
        #  Read json file
        open_r_file = open('data_json_task2.json', 'r+' )
        data = open_r_file.read()

        logging.debug(' read file json')

    except:
        #  extract json in site

        logging.debug(' not found json file')
        print('data')
        data = def_json(config_link)
        logging.debug(' json file created')

except:
    print('check your intenet')
    logging.error(' internet error and exit')
    sys.exit()







data = json.loads(data)  #  load json file


user_id = 0              #  Sum Id User 
email_verified = 0  #  Sum Email
sum_ip = {}             #  Sum Ip

max_login = ''         #  sum last ip
max_num = '0'       



for check in range(5):

    #  find user
    if 'user_id' in data [check]:
        user_id += 1
    logging.info('finde  user id ')

    #  Find email verified
    if data [check]['email_verified'] == True:
        email_verified += 1
    logging.info(' finde emailverified')

    #  add ip in dictionary 
    if 'last_ip' in data [check]:

        #  If ip already in the dictionary, add one
        if data [check]['last_ip'] in sum_ip:
            sum_ip [data [check]['last_ip']] = \
            sum_ip [data [check]['last_ip']]+1

        #  if ip not in the dictionary , its one
        elif data [check]['last_ip'] not in sum_ip:
            sum_ip [data [check]['last_ip']] = 1
    logging.info(' finde last ip')


    #  Convert the last login to a number
    if 'last_login' in data [check] :

         log = data [check]['last_login'].replace('-', '.'). replace(':','.'). replace('Z',''). replace('T','.'). replace ('.','')

        #  If the last login larger is found, put it
         if max_num < log :

             max_num = log
             max_login = data [check]['last_login']

    logging.info(' finde last login')


print (' top ip           : ' ,def_ip(sum_ip))
print (' user             : ' ,user_id)
print (' email verified   : ' , email_verified)
print (' last login       : ' , max_login)