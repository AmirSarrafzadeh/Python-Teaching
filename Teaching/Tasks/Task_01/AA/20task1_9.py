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
                                    len(         \
                                    sentence)     \
                                     -i - 1]

print (reverse_sentence)


# To not clear the page
x = input ('\n Next  ')  
