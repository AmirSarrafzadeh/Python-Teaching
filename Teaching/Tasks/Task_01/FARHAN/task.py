"""soal_1
name = input("what is your name? ")


print(f"my name is, {name}")"""



"""#soal_2
def even_or_odd(n):
        if n % 2 == 0:
            return "even"
        elif n % 2 != 0:
            return "odd"

try:
    n = int(input("Enter a number: "))
    print(even_or_odd(n))

except ValueError:
    print("you must enter a number!!")
"""




    

"""#soal_5
numbers = []

for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)
    
print("your numbers is:" , numbers)


numbers.sort(reverse=True)


print("numbers reverse:", numbers)"""


"""#soal_6
numbers = []

for number in range(10):
    a = int(input(f"enter number {number+1}: "))
    numbers.append(a)


even =  [x for x in numbers if x % 2 == 0]

odd =  [x for x in numbers if x % 2 != 0]


print(even , odd)"""



"""soal_7

numbers = []

for i in range(10):
    number = int(input(f"Enter number {i+1}:"))
    numbers.append(number)
    

print(max(numbers) - min(numbers))"""
 




"""soal_9
jomle = input("write:")


print("".join(reversed(jomle)))"""








"""soal_12
jomle = input("write: ")


print("len:",len(jomle))"""
    
 
 
    
"""soal_16
chars = "B5tkjnsds9890djhjhjdfhBBJGH77383KK090eklksldshjh98797234kKkkJJKHFSJH9"


if any(char.isdigit() for char in chars):   #age hadaghal ye charactor dar chars bashe(any) va char adad bashe (char.isdigit) print kon green 
    
    
    print("green")
    

if any(char.isupper() for char in chars):   #isupper yani harf bozorg

    
    print("red")


if any(char.islower() for char in chars):  #islower yani harf kochek
    
    
    print("blue")"""       




#soal_13
"""class reading:
    def __init__(self , uname , usurname , uage, ulocation, umovie, ucolor):
        self.uname = uname
        self.usurname = usurname        
        self.uage = uage       
        self.ulocation = ulocation
        self.umovie = umovie
        self.ucolor = ucolor
    def profile(self):       
        total_read_dict = {
            "name": self.uname,
            "surname": self.usurname,
            "age": self.uage,
            "location": self.ulocation,
            "movie": self.umovie,
            "color": self.ucolor
        }
        
        
        return total_read_dict
    
name = input("what is your name? ")

surname = input("what is your surname? ")

age = input("how old are you? ")

location = input("where are you from? ")

movie = input("what is your favorite movie? ")

color = input("what is your favorite color? ")   




user1 = reading(name, surname , age, location, movie , color)


print(user1.profile())"""



"""#soal_17
s = dict()


s1 = int(input("chand kilo sib kharidi: "))

s2 = int(input("chand kilo anbe kharidi: "))

s3 = int(input("chand kilo moz kharidi: "))

s4 = int(input("chand kilo portegal kharidi: "))

s["sib"] = s1


s["anbe"] = s2


s["moz"] = s3


s["portegal"] = s4

print("fruits =", s)

print("total =" , s["sib"] + s["anbe"] + s["moz"] + s["portegal"])"""




"""#soal_20
s = input("write: ")
s2 = dict()


for i in s:
    if i in s2:
        s2[i] += 1
    else:
        s2[i] = 1

print("Mydictionary", s2)"""






"""#soal_18
password = input ("enter pass: ")
while True:
    dig = any(char.isdigit() for char in password)
    low = any(char.islower() for char in password)
    upp = any(char.isupper() for char in password)            na tamam... !!! 
    zoj = any() 
    if len(password) < 1  or not (dig and low and upp):
        print("Error, pass must be digit and upp and low")
    
    else:
        print("good")
    password = input ("enter pass: ")"""
    
    


"""#soal_10
string = "Lkij0986jhjjhs76575bjh879jkms00902kj0099iiu87hjhhSSWe56672hjkmm"

digits = ""
letters = ""


for char in string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
        
print("digits:", {digits}, "letters:", {letters})"""



"""
#soal_19
string = input("write: ")
string2 = dict()
for char in string:
    if char in string2:
        string2[char] += 1
    else:
        string2[char] = 1
    
print("My_dictionary:",string2)"""

"""#soal_8
def is_prime(n):
    for i in range(2, n):
        
        if n % i ==0:
            return False
        else:
            return True
n = int(input("num: "))
for i in range(1,n):
    
    if is_prime(i):
        print(i)"""
        
#soal_18
import re 
password = input("enter pass: ")
nums  = re.findall(r"\d+", password)

even = False
odd = False
      
while True:
    dig = any(char.isdigit() for char in password)
    low = any(char.islower() for char in password)
    upp = any(char.isupper() for char in password)          
    h = any(char in "#@!$%" for char in password)
    for num in nums:
        
        if int(num) % 2 == 0:
            print(f"{num} is even")
            even = True

        else:
            print(f"{num} is odd")
            odd = True
    if not even:
        print("no even")
    if not odd:
        print("no odd")        




    if len(password) < 1  or not (dig and low and upp and h):
        print("Error, pass must be digit and upp and low")
    
    else:
        print("good")
    password = input ("enter pass: ")


"""soal_1
name = input("what is your name? ")


print(f"my name is {name}")"""



"""#soal_2
def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    elif n % 2 != 0:
        return "odd"

n = int(input("enter a number: "))
print(even_or_odd(n))"""




    

"""#soal_5
numbers = []

for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)
    
print("your numbers is:" , numbers)


numbers.sort(reverse=True)


print("numbers reverse:", numbers)"""


"""#soal_6
numbers = []

for number in range(10):
    a = int(input(f"enter number {number+1}: "))
    numbers.append(a)


even = list(filter(lambda x: x % 2 == 0 , numbers)) 

odd = list(filter(lambda x: x % 2 != 0 , numbers ))


print(even , odd)"""


"""soal_7

numbers = []

for i in range(10):
    number = int(input(f"Enter number {i+1}:"))
    numbers.append(number)
    

print(max(numbers) - min(numbers))"""
 

"""#soal_8
def is_prime(n):
    for i in range(2, n):
        
        if n % i ==0:
            return False
        else:
            return True
n = int(input("num: "))
for i in range(1,n):
    
    if is_prime(i):
        print(i)"""





"""#soal_9
jomle = input("write:")


print("".join(reversed(jomle)))"""








"""soal_12
jomle = input("write: ")


print("len:",len(jomle))"""
    


#soal_13
"""class reading:
    def __init__(self , uname , usurname , uage, ulocation, umovie, ucolor):
        self.uname = uname
        self.usurname = usurname        
        self.uage = uage       
        self.ulocation = ulocation
        self.umovie = umovie
        self.ucolor = ucolor
    def profile(self):       
        total_read_dict = {
            "name": self.uname,
            "surname": self.usurname,
            "age": self.uage,
            "location": self.ulocation,
            "movie": self.umovie,
            "color": self.ucolor
        }
        
        
        return total_read_dict
    
name = input("what is your name? ")

surname = input("what is your surname? ")

age = input("how old are you? ")

location = input("where are you from? ")

movie = input("what is your favorite movie? ")

color = input("what is your favorite color? ")   




user1 = reading(name, surname , age, location, movie , color)


print(user1.profile())"""
 
    


"""soal_16
chars = "B5tkjnsds9890djhjhjdfhBBJGH77383KK090eklksldshjh98797234kKkkJJKHFSJH9"


if any(char.isdigit() for char in chars):   #age hadaghal ye charactor dar chars bashe(any) va char adad bashe (char.isdigit) print kon green 
    
    
    print("green")
    

if any(char.isupper() for char in chars):   #isupper yani harf bozorg

    
    print("red")


if any(char.islower() for char in chars):  #islower yani harf kochek
    
    
    print("blue")"""       








"""#soal_17
s = dict()


s1 = int(input("chand kilo sib kharidi: "))

s2 = int(input("chand kilo anbe kharidi: "))

s3 = int(input("chand kilo moz kharidi: "))

s4 = int(input("chand kilo portegal kharidi: "))

s["sib"] = s1


s["anbe"] = s2


s["moz"] = s3


s["portegal"] = s4

print("fruits =", s)

print("total =" , s["sib"] + s["anbe"] + s["moz"] + s["portegal"])"""



"""
#soal_19
string = input("write: ")
string2 = dict()
for char in string:
    if char in string2:
        string2[char] += 1
    else:
        string2[char] = 1
    
print("My_dictionary:",string2)"""



"""#soal_20
s = input("write: ")
s2 = dict()


for i in s:
    if i in s2:
        s2[i] += 1
    else:
        s2[i] = 1

print("Mydictionary", s2)"""