import os

clear = input (' Hi, Whts your system?(win , linux) \n \
default(linux) : ')

if clear == 'win':
    clear = 'cls'

else:
    clear = 'clear' 



    # Start_20_question
#———————————————————————————

os.system( clear ) # To clear the page
print('Question_1 \n')

  # Question_1


Name = input(' What is your name : ')

print(' My name is', Name)


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_2 \n')

  # Question_2


Even = int( input(' Type your number : '))

if Even%2 == 1:
    print (' its odd')
    
else:
    print (' its even ')


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_3 \n')

  # Question_3

print ('its triangle?\n')

list = []

for i in range(1, 4):
    
    list.append(
    int(
    input(f'Type {i} number : ')
    ))


if  list[0] >= list[1] \
      and \
      list[0] >= list[2]:
     
    print (
    list[0] <
    list[1] + list[2]
    )
    
    
elif list[1] >= list[0] \
      and \
      list[1] >= list[2]:
          
    print (
    list[1] 
    < list[0] + list[2]
    )
    

else:
    
    print (
    list[2] 
    < list[0] + list[1]
    )
    
    
# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_4 \n')

  # Question_4
  
  
factor = int (input (' Type your factorial : '))
sum_factor = 1


if factor <= 10 \
      and \
      factor != 0:
          
    for i in range (1, factor+1):
        sum_factor *= i

else:
    print(' \n Your number is bigger 10\n ')

print (f' factorial {factor} is {sum_factor}')


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_5 \n')

  # Question_5


My_list = []

for i in range (0, 5):
    
    number = int( input( f' number {1 + i} : ')) 
    My_list.append(number)
    
print (' ' . join(
    map(
    str , sorted(
    My_list))),'\n --->')


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_6 \n')

  # Question_6


list_even = []
list_odd = []

for i in range (0 ,10):
    
    its_even = int( input ( f' number {i+1} : '))

    if its_even%2 == 1 :
        list_even.append( its_even)
        
    else:
        
        list_odd.append( its_even)
        
print(f' \n \n even : {list_odd} \n odd : {list_even}')   
        

# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_7 \n')

  # Question_7


list_aa = []
for i in range (0 ,10):
    
    append_list = int( input ( f' number {i+1} : '))
    list_aa.append( append_list)
   
print (f'\n min : {min(list_aa)} \
            \n max : {max(list_aa)}\
            \n {max(list_aa)} - {min(list_aa)}  =  {max(list_aa) - min(list_aa)}')


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_8 \n')

  # Question_8


number = int( input (' Type your range : '))
list_prime = [1, 2]

for check  in range (2, number + 1):
    prime = 0
    
    print ('check --->  ', check)
    
    for i in range (2, check):
        
        if check % i == 0:
            prime = 0
            break 
        
        else:
            prime = check
        
    if prime != 0 :
        list_prime.append(prime)
        
print('\n',list_prime)        


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_9 \n')

  # Question_9


sentence = input ('write a sentence for reverse : ')

reverse_sentence = ' '

for i in range (len(sentence)):
    
    reverse_sentence += sentence[        \
                                    len(                         \
                                    sentence)                \
                                     -i - 1]

print (reverse_sentence)


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_10 \n')

  # Question_10

str_order = ' '
int_order = ' '

order = ' Lkij0986jhjjhs76575bjh879jkms00902kj0099iiu87hjhhSSWe56672hjkm '

for i in order:
    
    if i.isdigit():
        
        int_order += i
        
    else:
        
        str_order += i
        
print (f'\n str order : { str_order} \
              \n int order : { int_order}')


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_11 \n')

  # Question_11


fibonacci = [0 ,1]

while True:
    
    number = int ( input (' Type your fibonacci : '))
    if len (str (number)) == 3 :
        break 
        
    else:
        print ('len ')



while True :
    
    if fibonacci[ -1] +       \
        fibonacci[ -2]           \
        <= number:
        
        fibonacci.append(     
            fibonacci[ -1] +        
            fibonacci[ -2])
        
    else :
      break 

print (fibonacci)


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_12 \n')

  # Question_12


Sentence = input (' Type Sentence : ')

print(' \n word : ' ,
    len( 
    Sentence.split( ) ) )


# To not clear the page
x = input ('\n Next  ')  


#———————————————————————————

os.system( clear ) # To clear the page
print('Question_13 \n')

  # Question_13


my_dic = {}

list_word = [ ' What is your name? ' 
, ' What is your surname? '  
, ' How old are you ? '  
, ' Where are you from? ' 
, ' What is your favorite movie? '  
, ' What is your favorite color? '   
]

for i in range ( len( list_word)):
    
    word = input (list_word[ i])
    my_dic.update( { list_word[ i] : word})

print (my_dic)


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_14 \n')

  # Question_14


number = int( input (' Type your range : '))
list_prime = [2, 1]

for check  in range (1, number + 1):
    prime = 0
    
    for i in range (2, check):
        
        if check % i == 0:
            break 
        
        else:
            prime = check
        
    if prime != 0 :
        list_prime.insert(0, prime)
        
print('\n',list_prime)        


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————
os.system( clear ) # To clear the page
print('Question_15 \n')

  # Question_15


print ('The date should be written like this  (2024/3/10)\n')

date1 = input('Enter the date 1 : ') #.split ('/') 
date2 = input('Enter the date 2 : ')#. split ('/')

for i in range (0 ,3):
    
    if date1.split( '/')[ i]  \
    > date2.split( '/')[ i] :
        
        print (date2)
        break

    elif date1. split( '/')[ i]  \
        < date2. split( '/')[ i]:
        
        print (date1)
        break


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_16 \n')

  # Question_16


char = 'B5tkjnsds9890djhjhjdfhBBJGH77383K\
K090eklksldshjh98797234kKkkJJKHFSJH9'

word = ''

for x in char:
    
    if ord(x) >= 65    \
    and    \
    ord(x) <= 90:
        
        word += '\033[31m'+x#+'\033[0m'
        
        
    elif ord(x) >= 97    \
    and    \
    ord(x) <= 122:
        
        word += '\033[34m'+x#+'\033[0m'
        
    
    elif ord(x) >= 48    \
    and    \
    ord(x) <= 57:
        
        word += '\033[32m'+x#+'\033[0m'
        
    
    else :
        print ('its character : ',x)

print (word+'\033[30m')


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_17 \n')

  # Question_17


Fruits = {
'Sib': 15000,
'Anbe': 23000,
'Moz': 12000,
'Portagal': 20000
}


Sib = float( input (' Chand kilo Sib kharidid? '  ))
Anbe = float( input(' Chand kilo Anbe Kharidid? '))
Moz = float( input (' Chand kilo Moz Kharidid? '))
Portagal = float( input (' Chand kilo Portagal Kharidid? '))


print (f"\n  \
Sib      : { Fruits[ 'Sib'] * Sib}   \n  \
Anbe     : { Fruits[ 'Anbe'] * Anbe}  \n  \
Moz      : { Fruits[ 'Moz'] * Moz}  \n  \
Portagal : { Fruits[ 'Portagal'] * Portagal}  \n\n  \
\
Total purchase of fruits :  \n  {  ( Fruits[ 'Sib'] * Sib )  +  ( Fruits[ 'Anbe'] * Anbe )   +  ( Fruits[ 'Moz'] * Moz )  +  ( Fruits[ 'Portagal'] * Portagal )}  \
")


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_18 \n')

  # Question_18



print ('''
قوانین:

حداقل باید یک عدد فرد و یک عدد زوج داشتھ باشد. 
\n
حداقل باید یک کاراکتر کوچک و یک کاراکتر بزرگ داشتھ باشد. 
\n
حداقل یکی از کاراکتر ھای زیر را داشتھ باشد. 
@ # $ ! %
\n
دو عدد کاراکتر بزرگ پشت سر ھم نمی توانند باشند. 
\n
سھ عدد پشت سر ھم نمی توانند باشند. 

''')
my_true = True
while my_true :
    print ('————————————————————————————')
    its_pass = 0
    my_pass = input('Use pass : ')
    
    
    
#2 number even and odd
    x = 0
    for i in my_pass:
        
        if i.isdigit():
            
            if x == 0 and (int(i) % 2 == 0 or int(i) % 2 == 1) :
                zoj = int(i) % 2
                x += 1
                
            if zoj == 0 and int(i) %2 == 1:
                
                x += 1
            elif zoj != 0 and int(i) %2 == 0:
                 x += 1
                 
    if x >= 2:
        its_pass += 1
        
    else:
        print ('Error for not find number even and odd\n')



#'find upp and min'
    x = 0
    g = 0
    for i in my_pass:
        
        
        if x == 0    \
        and    \
        ord(i) >= 97    \
        and    \
        ord(i) <= 122:
            
            x += 1
            
            
        elif g == 0    \
        and    \
        ord(i) >= 65    \
        and    \
        ord(i) <= 90:
            
            g += 1
            
    if g+x >= 2:
        its_pass += 1

    else:
        print ('Error for not find big and small letters \n')


        
#find @ ,# ,$ ,! ,%         
    if  '@' in my_pass        \
    or        \
    '#' in my_pass        \
    or        \
    '$' in my_pass        \
    or        \
    ' !' in my_pass        \
    or        \
    '%' in my_pass :


        its_pass += 1
        
    else:
        print ('Error for not find (@ ,# ,$ ,! ,% ) \n')
        

#2 capital letters 
    for i in my_pass:
    
        if (not i.isdigit())    \
        and    \
        i.upper() == i:
            
            x += 1
                        
            if x == 2 :
                print ('There is more than one capital word in a row\n')
        
                break 
        
        else :
            x = 0
            
    if x <= 1:
        its_pass += 1
    
    
#3 numbers consecutive
    for i in my_pass:
        
        if i.isdigit():
            x += 1
            
            if x == 3 :
                print ('There are 3 numbers in a row\n ')
                
                break

        
        else :
            x = 0
            
        if x < 3 :
            its_pass += 1
        
#fine pass
    if its_pass == 5:
        print ('\n\n\n\n\n\n    its ok : ',my_pass)
        break 
        
    

# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_19 \n')

  # Question_19


word = input (' Type Sentence : ')

dict = {}

for i in word:
    
    if i in dict:
        
        dict[i] = dict.get(i)+1
        
    else:
        dict.update({i:1})
    
print(dict)   


# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————

os.system( clear ) # To clear the page
print('Question_ 20\n')

  # Question_20


while True:
    start_time = input (' start time : ').split(':')
    finish_time = input (' finish time : ').split(':')
    integer = True
    try:
        for i in range(3):
            if int(start_time[i]) < 0:
                print(f'The number {start_time[i]} is below zero')
                integer = False
                break
            elif int(finish_time[i]) < 0:
                print(f'The number {finish_time[i]} is below zero')
                integer = False
                break
            elif not start_time[i].isdigit():
                print('its not integer ', start_time[i])
                integer = False
                break
            elif not finish_time[i].isdigit():
                print('its not integer ', finish_time[i])
                integer = False
                break
            elif len(finish_time) != 3:
                print(f'The len {finish_time} is not equal to 3')
                integer = False
                break
            elif len(start_time) != 3:
                print(f'The len {start_time} is not equal to 3')
                integer = False
                break
    
    except ValueError:
        print ('Use integer')
    
    try :
        if integer:
            S_split = (int(start_time[0]) * 3600 + int(start_time[1]) * 60 + int(start_time[2]))
            F_split = (int(finish_time[0]) * 3600 + int(finish_time[1]) * 60 + int(finish_time[2]))
        
            if S_split > F_split:
                x = 86400 - (S_split - F_split)
                hurs = x // 3600
                min = (x % 3600) // 60
                sc = ((x % 3600) % 60)
                print(str(hurs) + ":" + str(min) + ':' + str(sc))
        
            elif S_split < F_split:
                x = F_split - S_split
                hurs = x // 3600
                min = (x % 3600) // 60
                sc = ((x % 3600) % 60)
                print(str(hurs) + ":" + str(min) + ':' + str(sc))
    
    except :
        print ('try agin')
    
    ended = input(' you need continue ? (y,n)')
    if ended == 'n':
        print ('bay')
        break

    else:
        print (' continue ')
        

# To not clear the page
x = input ('\n Next  ')  

#———————————————————————————
