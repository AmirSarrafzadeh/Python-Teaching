from typing import Callable, Any
from colorama import Fore
# question 1
def whatname() -> str:
    answer = input('what is your name? ')
    return f'My name is {answer}. '


# -------------------------------------------
# question 2
def even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


# -------------------------------------------
# question 3
def triangle(a: float, b: float, c: float) -> bool:
    if a > 0 or b > 0 or c > 0:
        if a + b > c:
            return True
        else:
            return False
    else:
        return (f'warning: numbers are negative.....')

    # -------------------------------------------


# question 4
def factorial(number: int) -> any:
    Factorial = 1
    while True:
        if number > 10:
            print('function stoped!!!')
            break
        else:
            for Num in range(1, number + 1):
                Factorial *= Num
            else:
                return Factorial


# -------------------------------------------
# question 5
def descending(*numbers) -> list[int] :
    main_list = []
    if type(numbers) != list :
        for data in numbers :
            main_list.append(data)
        main_list.sort(reverse= False)
        return main_list
        
    else:
        numbers.sort(reverse= True)
        return numbers

    

# -------------------------------------------
# question 6
def even_odd(*numbers: int) -> list[int]:
    even = []
    odd = []
    for Num in numbers:
        if Num % 2 == 0:
            even.append(Num)
        else:
            odd.append(Num)
    else:
        return ('the even numbers are {}\nthe odd numbers are {}'.format(even, odd))


# -------------------------------------------
#  question 7
def diffrence(*numbers: float):
    Ma = max(numbers)
    Mi = min(numbers)
    return (f'the maximum number = {Ma}\nthe minimum number = {Mi}')


# -------------------------------------------
# question 8
def prime_numbers(number:int)-> list: 
    out = list()
    for x in range(1, number+1):
        if all(x % i != 0 for i in range (2, int(x**.5)+1)):
            out.append(x)
    return out

# -------------------------------------------
# question 9
def revers(sentense: str) -> str:
    mylist = sentense.split(' ')
    mylist.reverse()
    answer = ' '.join(mylist)
    return answer


# -------------------------------------------
# question 10
def number_or_alphabet(sentense: str) -> dict:
    My_dictionary = {}
    number = 0
    alphabet = 0
    for data in sentense:
        if data.isdigit() == True:
            number += 1
        else:
            alphabet += 1
    My_dictionary['number'] = number
    My_dictionary['alphabet'] = alphabet
    return My_dictionary


# -------------------------------------------
# question 11
def fibo(number: int) -> tuple:
    a = 0
    b = 1
    ans = 1
    mylist = [0, 1]

    while True:
        if ans < number:
            ans = a + b
            a = b
            b = ans
            if ans > number:
                break
            else:
                mylist.append(ans)
        else:
            break
    return (tuple(mylist))


# -------------------------------------------
# question 12
def spell_sen(sentence: str) -> int: 
    number_list = sentence.split(' ')
    return len(number_list)

# -------------------------------------------
# question 13
def ask() -> dict : 
    name = input('what is your name? ')
    surname = input('what is your surname? ')
    age = int(input('how old are you? '))
    region = input('where are you from: ')
    movie = input('what is your favorite movie? ')
    color = input('what is your favorite color? ')
    you = {}
    you['name'] = name
    you['surname'] = surname
    you['age'] = age
    you['region'] = region
    you['movie'] = movie
    you['color'] = color
    return you

# -------------------------------------------
# question 14
def prime_numbers4(number:int)-> list: 
    out = list()
    for x in range(1, number+1):
        if all(x % i != 0 for i in range (2, int(x**.5)+1)):
            out.append(x)
            out.sort(reverse=False )
    return out

# -------------------------------------------
# question 15
def date(date1: str , date2: str) -> 'date' :
    list_date1_string = date1.split("/")
    list_date2_string = date2.split("/")
    dic1 = {}
    dic2 = {}

    list_date1_number = []
    list_date2_number = []

    for data in list_date1_string:
        new = int(data)
        list_date1_number.append(new)

    for data2 in list_date2_string:
        new2 = int(data2)
        list_date2_number.append(new2)
    dic1['year1'] = list_date1_number[0]
    dic1['mounth1'] = list_date1_number[1]
    dic1['day1'] = list_date1_number[2]

    dic2['year2'] = list_date2_number[0]
    dic2['mounth2'] = list_date2_number[1]
    dic2['day2'] = list_date2_number[2]    

    if dic1['year1'] < dic2['year2'] : 
        return f'{date1} date is earlier...!'
    elif dic2['year2'] < dic1['year1'] :
        return f'{date2} date is earlier...!'
    else : 
            if dic1['mounth1'] < dic2['mounth2'] : 
                return f'{date1} date is earlier...!'
            elif dic2['mounth2'] < dic1['mounth1'] : 
                return f'{date2} date is earlier...!'
            else : 
                if dic1['day1'] < dic2['day2'] : 
                    return f'{date1} date is earlier...!'
                elif dic2['day2'] < dic1['day1'] :
                    return f'{date2} date is earlier...!'
                else :
                    return 'You have entered two identical dates.'


# -------------------------------------------
# question 16
exa = 'B5tkjnsds9890djhjhjdfhBBJGH77383KK090eklksldshjh98797234kKkkJJKHFSJH9'
for char in exa :
    if char.isupper() == True :
        print(Fore.RED , char , end='')
    elif char.isdigit() == True:
        print(Fore.GREEN , char ,end='')
    else:
        print(Fore.BLUE , char , end='')    

# -------------------------------------------
# question 17
def ask_question() -> dict :
    sib = input('chand kilo sib kharidid?')
    anbe = input('chand kilo anbe kharidid?')
    moz = input('chand kilo moz kharidid?')
    portagal = input('chand kilo portagal kharidid?')
    fruits = {}
    fruits['sib'] = sib
    fruits['anbe'] = anbe
    fruits['moz'] = moz
    fruits['portagal'] = portagal
    return fruits

# -------------------------------------------
# question 18
def password() -> Callable[[], str]:
    user_input = input('enter the password: ')
    carrotnumber = 0
    list_of_number = []
    list_of_odd = []
    list_of_even = []
    list_of_upper = []
    list_of_lower = []
    list_of_character = ['@', '#', '$', '%', '!']
    while True:
        for data in user_input:
            if data.isdigit() == True:
                list_of_number.append(data)
            elif data.isupper() == True:
                list_of_upper.append(data)
            elif data in list_of_character:
                list_of_character.append(True)
            else:
                list_of_lower.append(data)
        if len(list_of_number) < 1:
            user_input = input('there arent number\nplease correct the password: ')
            list_of_number.clear()
            list_of_lower.clear()
            list_of_upper.clear()
            list_of_odd.clear()
            list_of_even.clear()
            # list_of_character.remove(True)
            continue
        else:
            carrotnumber += 1
            for Num in list_of_number:
                if int(Num) % 2 == 0:
                    list_of_even.append(Num)
                else:
                    list_of_odd.append(Num)
            else:
                if len(list_of_even) < 1:
                    user_input = input('there arent even number\nplease correct the password: ')
                    list_of_number.clear()
                    list_of_lower.clear()
                    list_of_upper.clear()
                    list_of_odd.clear()
                    list_of_even.clear()
                    carrotnumber -= 1
                    # list_of_character.remove(True)
                    continue
                else : 
                    carrotnumber += 1

                if len(list_of_odd) < 1:
                    user_input = input('there arent odd number\nplease correct the password: ')
                    list_of_number.clear()
                    list_of_lower.clear()
                    list_of_upper.clear()
                    list_of_odd.clear()
                    list_of_even.clear()
                    carrotnumber -= 2
                    # list_of_character.remove(True)
                    continue
                else: 
                    carrotnumber += 1

        if len(list_of_lower) < 1:
            user_input = input('there arent lower alphabet\nplease correct the password: ')
            list_of_number.clear()
            list_of_lower.clear()
            list_of_upper.clear()
            list_of_odd.clear()
            list_of_even.clear()
            carrotnumber -= 3
            # list_of_character.remove(True)
            continue
        else :
            carrotnumber += 1

        if len(list_of_upper) < 1:
            user_input = input('there arent upper alphabet\nplease correct the password: ')
            list_of_number.clear()
            list_of_lower.clear()
            list_of_upper.clear()
            list_of_odd.clear()
            list_of_even.clear()
            carrotnumber -= 4
            # list_of_character.remove(True)
            continue
        else : 
            carrotnumber += 1

        if True not in list_of_character:
            user_input = input('there arent character\nplease correct the password: ')
            list_of_number.clear()
            list_of_lower.clear()
            list_of_upper.clear()
            list_of_odd.clear()
            list_of_even.clear()
            carrotnumber -= 5
            # list_of_character.remove(1)
            continue
        else :
            carrotnumber += 1

        for i in user_input :
            if i in list_of_upper :
                if user_input[user_input.index(i) + 1].isupper() == True :
                    user_input = input('You wrote two capital letters in a row\nplease correct the password: ')
                    list_of_number.clear()
                    list_of_lower.clear()
                    list_of_upper.clear()
                    list_of_odd.clear()
                    list_of_even.clear()
                    carrotnumber -= 6 
                else:
                    carrotnumber += 1    
        if len(user_input) > 5 :
            for j in user_input : 
                if j.isdigit() == True : 
                    if user_input[user_input.index(j) + 1].isdigit() == True and user_input[user_input.index(j) + 2].isdigit() == True :
                        user_input = input('You wrote three number letters in a row\nplease correct the password: ')        
                        list_of_number.clear()
                        list_of_lower.clear()
                        list_of_upper.clear()
                        list_of_odd.clear()
                        list_of_even.clear()    
                        carrotnumber -= 7    
                    else :
                        carrotnumber += 1        
                            
        if carrotnumber >= 8 :
            # print(f'is password {user_input}')
            break



    return f'ecellent. your password:({user_input}) is cattect '


# -------------------------------------------
# question 19
def count_character(word: str) -> dict:
    dic = {}
    for char in word:
        reapet = word.count(char)
        rep = word.replace(char, '')
        if char == ' ':
            char = '*SPACE'
        dic[char] = reapet
    return dic


# -------------------------------------------
# question 20 
def clock():
    """
    This function is a wake-up alarm that receives two inputs:
            first clock : Current time
            second clock : The time you set to wake up
    """
    time1 = input('format -> hh:mm:ss\nenter the first clock: ')
    time2 = input('format -> hh:mm:ss\nenter the second clock: ')
    list_time1_string = time1.split(":")
    list_time2_string = time2.split(":")
    dic1 = {}
    dic2 = {}

    list_time1_number = []
    list_time2_number = []

    for data in list_time1_string:
        new = int(data)
        list_time1_number.append(new)

    for data2 in list_time2_string:
        new2 = int(data2)
        list_time2_number.append(new2)

    dic1['hour1'] = list_time1_number[0]
    dic1['min1'] = list_time1_number[1]
    dic1['sec1'] = list_time1_number[2]

    dic2['hour2'] = list_time2_number[0]
    dic2['min2'] = list_time2_number[1]
    dic2['sec2'] = list_time2_number[2]

    if dic1['min1'] == 0 and dic1['sec1'] == 0:
        if dic1['hour1'] > dic2['hour2']:
            ans_h = (24 - dic1['hour1']) + dic2['hour2']

            return (f'{ans_h}:{dic2["min2"]}:{dic2["sec2"]}')
        else:
            ans_h = dic2['hour2'] - dic1['hour1']
            return (f'{ans_h}:{dic2["min2"]}:{dic2["sec2"]}')

    if dic1['min1'] != 0 or dic1['sec1'] != 0:
        ans_s = 60 - dic1['sec1']
        if ans_s < 60:
            dic1['min1'] += 1
        else:
            pass

        ans_m = 60 - dic1['min1']
        if ans_m < 60:
            dic1['hour1'] += 1
        else:
            pass

        if dic1['hour1'] > dic2['hour2']:
            ans_h = (24 - dic1['hour1']) + dic2['hour2']

        else:
            ans_h = dic2['hour2'] - dic1['hour1']

        if dic2['sec2'] != 60:
            ans_s += dic2['sec2']
            if ans_s > 60:
                m = ans_s // 60
                ans_s = ans_s % 60
                ans_m += m

        if dic2['min2'] != 0:
            ans_m += dic2['min2']
            if ans_m > 60:
                h = ans_m // 60
                ans_m = ans_m % 60
                ans_h += h

        return (f'{ans_h}:{ans_m}:{ans_s}')
