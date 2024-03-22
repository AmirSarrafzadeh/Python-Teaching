#task11
# def fibonacci(n):
#     a, b = 0, 1
#     fib_list = []
#     while a < n:
#         fib_list.append(a)
#         a, b = b, a + b
#     return fib_list
#
# num = input("Enter a three-digit number: ")
# if num.isdigit() and len(num) == 3:
#     result = fibonacci(int(num))
#     print(f"Fibonacci numbers less than {num}: {result}")
# else:
#     print("Please enter a valid three-digit number.")
#
#
# #task12
# # TODO The task should be corrected.
# sentence = input("Enter a sentence: ") + (" ")
# words = sentence.split(" ")
# for word in words:
#     print(word)
#
#
# #task13
# answers = {}
# questions = ["how are you? ", "what's your name? ",
#             "What is your surname? ",
#             "How old are you ? ",
#             "Where are you from? ",
#             "What is your favorite movie? ",
#             "What is your favorite color? "
# ]
# for question in questions:
#     answer = input(f"{question}\n answer: ")
#     answers[question] = answer
#
# print("greetings: ")
# for question, answer in answers.items():
#     print(f"{question}: {answer}  ")
#
# #task14
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def display_primes_less_than(num):
#     primes = [i for i in range(2, num) if is_prime(i)]
#     print("Prime numbers less than", num, "are:")
#     for prime in primes:
#         print(prime)
#
# while True:
#     num = input("Enter a four-digit number: ")
#     if len(num) == 4 and num.isnumeric():
#         num = int(num)
#         display_primes_less_than(num)
#         break
#     else:
#         print("Please enter a valid four-digit number.")
#
# #task15
# class date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#     def display(self):
#         return f"{self.year}/ {self.month}/ {self.day}"
#     def earlier_date(self, other):
#         date1 = date(self.year, self.month, self.day)
#         date2 = date(other.year, other.month, other.day)
#         if date1 < date2:
#             return "the first date is earlier! "
#         else:
#             return "the second date is earlier! "
#
#
# '''
#
# answers = {year, month, day}
# questions = ["Enter first date: ",
#              "Enter second date: "]
# for question in questions:
#     answer = date(input(f"{question}\n {year}/ {month}/ {day} "))
#     answers[question] = {year}, {month}, {day}
#
# answer[0] = date.date1
# answer[1] = date.date2
#
#
# print(date.earlier_date(answer[0], answer[1]))
# '''
# #natunestam benevisam
#
#
#
# #task16
# string_a = "B5tkjnsds9890djhjhjd�BBJGH77383KK090eklksldshjh98797234kKkkJJKHFSJH9"
# upper_strings = []
# lower_strings = []
# numbers = []
# length_str = len(string_a)
# list_str = list(string_a[0:length_str])
#
# for i in list_str:
#     if i.isdigit():
#         numbers.append(i)
#     elif i.isalpha():
#         if i.isupper():
#             upper_strings.append(i)
#         else:
#             lower_strings.append(i)
#
# green = "\033[0;32m"
# print(green)
# print(numbers)
# red = "\033[0;31m"
# print(red)
# print(upper_strings)
# blue = "\033[0;34m"
# print(blue)
# print(lower_strings)
#
#
# #task17
# Fruits = {
# "sib": 15000,
# "anbe": 23000,
# "moz": 12000,
# "portaghal": 20000
# }
# questions = ["Chand kilo Sib kharidid? ",
# "Chand kilo Anbe Kharidid? ",
# "Chand kilo Moz Kharidid? ",
# "Chand kilo Portagal Kharidid? "]
# answers = []
# for question in questions:
#     answer = int(input(question + " "))
#     answers.append(answer)
#
# qeymate_sib = 15000 * answers[0]
# qeymate_anbe = 23000 * answers[1]
# qeymate_moz = 12000 * answers[2]
# qeymate_potaghal = 20000 * answers[3]
# #ba dict balad nashodam:))
# print(qeymate_sib, qeymate_anbe, qeymate_moz, qeymate_potaghal)


#task18
def valid_password(password):
    for char in password:
        if char.isdigit():
            if int(char) %2 == 0:
                has_even = True
                for i in range(len(password) - 3):
                    if password[i:i+3].isdigit():
                        return False
                    else:
                        return True
            else:
                has_odd = True
        elif char.isalpha():
            if str(char).isupper:
                has_upper = True
                for i in range(len(password) - 1):
                    if password[i].isupper() != password[i + 1].isupper():
                        not_side_by_side = True
                    else:
                        return False
            else:
                has_lower = True
        elif (password[i]for i in range(len(password))) in ['@', '#', '$', '!', '%']:
            has_special_char = True
        else:
            return False
        
password = input("Enter password: ")            
while valid_password(password) == False:
    password = input("Error! try again: ")
print("valid password: ", password)
    

print(valid_password(password))


#task19
#task20