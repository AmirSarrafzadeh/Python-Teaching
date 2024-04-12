# Example 1: Counting from 1 to 10
count = 1
while count <= 10:
    print(count)
    count += 1

# Example 2: Printing Even Numbers up to 20
num = 2
while num <= 20:
    print(num)
    num += 2

# Example 3: Countdown from 10 to 1
count = 10
while count >= 1:
    print(count)
    count -= 1

# Example 4: Sum of Numbers from 1 to 100
sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print("Sum of numbers from 1 to 100:", sum)

# Example 5: User Input Validation
password = ""
while password != "secret":
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted!")
    else:
        print("Access denied. Try again.")

# Example 6: Displaying Characters of a String
string = "Hello, World!"
index = 0
while index < len(string):
    print(string[index])
    index += 1

# Example 7: Finding Factorial of a Number
num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial of 5:", factorial)

# Example 8: Reversing a String
string = "hello"
reversed_string = ""
index = len(string) - 1
while index >= 0:
    reversed_string += string[index]
    index -= 1
print("Reversed string:", reversed_string)

# Example 9: Generating Fibonacci Series
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b

# Example 10: Simulating a Dice Roll until a Specific Number is Rolled
import random
target_number = 6
rolls = 0
while True:
    rolls += 1
    result = random.randint(1, 6)
    print("Roll", rolls, "- Result:", result)
    if result == target_number:
        print("Target number reached!")
        break

# Example 11: Printing Multiplication Table of 7
num = 1
while num <= 10:
    print("7 *", num, "=", 7 * num)
    num += 1

# Example 12: Repeating a String
string = "Hello"
repeats = 5
while repeats > 0:
    print(string)
    repeats -= 1

# Example 13: Generating Odd Numbers up to 20
num = 1
while num <= 20:
    print(num)
    num += 2

# Example 14: Checking if a Number is Prime
num = 17
is_prime = True
divisor = 2
while divisor <= num // 2:
    if num % divisor == 0:
        is_prime = False
        break
    divisor += 1
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Example 15: Finding the Largest Element in a List
numbers = [5, 10, 3, 8, 15, 7]
largest = numbers[0]
index = 1
while index < len(numbers):
    if numbers[index] > largest:
        largest = numbers[index]
    index += 1
print("The largest number in the list is:", largest)
