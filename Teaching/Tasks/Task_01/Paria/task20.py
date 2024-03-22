first_question = "what time is it now? (please print the time like: hour:minute:second) "
second_question = "what time do you want to set the alarm? (please print the time like: hour:minute:second) "
   
time1 = input(first_question)
time2 = input(second_question)


time1_list = time1.split(":")
time2_list = time2.split(":")
hour1 = int(time1_list[0])
minute1 = int(time1_list[1])
second1 = int(time1_list[2]) 

hour2 = int(time2_list[0])
minute2 = int(time2_list[1])
second2 = int(time2_list[2])


times_dict = {}
times_dict[time1] = {
    "hour" : hour1,
    "minute" : minute1,
    "second" : second1
}
times_dict[time2] = {
    "hour" : hour2,
    "minute" : minute2,
    "second" : second2    
}
def check_hour(hour1, hour2):
    for key, value in times_dict.items():
        if (hour1 and hour2) in range(0, 24):
            return True
        else:
            print("Error set a valid time! ")
            
def check_minute(minute1, minute2):
    for key, value in times_dict.items():
        if (minute1 and minute2) in range(0, 59):
            return True
        else:
            print("Error set a valid time! ")
   
def check_second(second1, second2):
    for key, value in times_dict.items():
        if (second1 and second2) in range(0, 59):
            return True
        else:
            print("Error set a valid time! ")

def second(): 
    while check_second:
        for second in times_dict.items():
            if second1 == second2:
                return return_tomorrow()
            elif second1 < second2:
                return return_time()
            elif second1 > second2:
                return return_tomorrow()
def minute():
    while check_minute:
        for minute in times_dict.items():
            if minute1 == minute2:
                return check_second(second1, second2)
            elif minute1 < minute2:
                return return_time
            elif minute1 > minute2:
                return return_tomorrow
def hour():
    while check_hour:
        for hour in times_dict.items():
            if hour1 == hour2:
                return check_minute(minute1, minute2)
            elif hour1 < hour2:
                return return_time
            elif hour1 > hour2:
                return return_tomorrow

def return_time():

    hour = hour2 - hour1 + 12
    minute = minute2 - minute1
    second = second2 - second1
    if hour < 12:
        hour = hour + 12
    if minute < 0:
        hour = hour - 1
        minute = minute + 60
    if second < 0:
        minute = minute - 1
        second = second + 60
    print(str(hour) + ":" + str(minute) + ":" + str(second))
    
def return_tomorrow():

    hour = hour2 - hour1 + 24
    if hour > 24:
        hour = hour - 24
    minute = minute2 - minute1
    second = second2 - second1


    if minute < 0:
        hour = hour - 1
        minute = minute + 60
    if second < 0:
        minute = minute - 1
        second = second + 60
    print(str(hour) + ":" + str(minute) + ":" + str(second))

print(hour(), minute(), second())