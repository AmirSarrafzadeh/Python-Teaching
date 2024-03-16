#task1
name = input(" what is your name? ")
print("my name is " + name)


#task2
number = int(input("please enter your number: "))
if number %2 == 0:
    print("the number is even!")
elif number %2 == 1:
    print("the number is odd!")
else:
    print("please enter a valid number!")
    
#task3
first_side = input("please enter the first side: ")
second_side = input("please enter the second side: ")
third_side = input("please enter the third side: ")
a = first_side
b = second_side
c = third_side

#the condition of forming a triangle
if a < b + c and b < c + a and c < a + b:
    print(" the triangle can be formed! ")
else:
    print(" the triangle can't be formed! ")

#task4
number = int(input("please enter your number:"))

if number > 10:
    print("None")
elif number <= 10:
    def factorial(number):
        
        if number < 0:
            print("the number is negative!")
        elif number == 0:
            return 1
        else:
            return number * factorial(number - 1)
    print(factorial(number))
    
#task5
num_list = []

for _ in range(0, 5):
    numbers = int(input("enter: "))
    num_list.append(numbers)

num_list.sort(reverse=True)
print(num_list)