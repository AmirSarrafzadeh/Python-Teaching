# Example 1: Counting from 1 to 10
for count in range(1, 11):
    print(count)

# Example 2: Printing Even Numbers up to 20
for num in range(2, 21, 2):
    print(num)

# Example 3: Countdown from 10 to 1
for count in range(10, 0, -1):
    print(count)

# Example 4: Sum of Numbers from 1 to 100
sum = 0
for num in range(1, 101):
    sum += num
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
for char in string:
    print(char)

# Example 7: Finding Factorial of a Number
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of 5:", factorial)

# Example 8: Reversing a String
string = "hello"
reversed_string = ""
for char in string[::-1]:
    reversed_string += char
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
for num in range(1, 11):
    print("7 *", num, "=", 7 * num)

# Example 12: Repeating a String
string = "Hello"
for _ in range(5):
    print(string)

# Example 13: Generating Odd Numbers up to 20
for num in range(1, 21, 2):
    print(num)

# Example 14: Checking if a Number is Prime
num = 17
is_prime = True
for divisor in range(2, num // 2 + 1):
    if num % divisor == 0:
        is_prime = False
        break
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Example 15: Finding the Largest Element in a List
numbers = [5, 10, 3, 8, 15, 7]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("The largest number in the list is:", largest)
