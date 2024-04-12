# Example 1: Checking if a number is positive, negative, or zero
num = 5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Example 2: Checking if a number is even or odd
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 3: Checking if a number is divisible by both 2 and 3
num = 6
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by both 2 and 3")

# Example 4: Checking if a year is a leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Example 5: Checking if a string is empty or not
string = ""
if string:
    print("String is not empty")
else:
    print("String is empty")

# Example 6: Checking if a character is a vowel or consonant
char = 'a'
if char in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")

# Example 7: Checking if a number is within a specific range
num = 25
if 20 <= num <= 30:
    print("Within range")
else:
    print("Outside range")

# Example 8: Checking if a number is a perfect square
num = 16
if num ** 0.5 == int(num ** 0.5):
    print("Perfect square")
else:
    print("Not a perfect square")

# Example 9: Checking the size of a file
file_size = 1024
if file_size < 1024:
    print("Small file")
elif 1024 <= file_size < 1048576:
    print("Medium file")
else:
    print("Large file")

# Example 10: Checking if a number is a multiple of both 5 and 7
num = 35
if num % 5 == 0 and num % 7 == 0:
    print("Multiple of both 5 and 7")
else:
    print("Not a multiple of both 5 and 7")

# Example 11: Checking the type of a variable
variable = 10
if isinstance(variable, int):
    print("Integer")
elif isinstance(variable, float):
    print("Float")
elif isinstance(variable, str):
    print("String")
else:
    print("Unknown type")

# Example 12: Checking if a number is within a specific range using multiple conditions
num = 75
if num < 50:
    print("Less than 50")
elif num >= 50 and num < 100:
    print("Between 50 and 100")
else:
    print("Greater than or equal to 100")

# Example 13: Checking if a year is a common year or not
year = 2023
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("Common year")
else:
    print("Not a common year")

# Example 14: Checking if a string contains only digits
string = "12345"
if string.isdigit():
    print("Contains only digits")
else:
    print("Contains characters other than digits")

# Example 15: Checking if a number is positive, negative, or zero using a ternary operator
num = -5
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(result)
