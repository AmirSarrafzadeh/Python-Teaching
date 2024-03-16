import os 

print(os.path)



# Question 1

# Ask the user their name and store it in a variable
name = input("What is your name? ")

# Greet the user by name
print(f"My name is {name}.")

# Question 2

# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Question 3

# Get three numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Check if the three numbers can form a triangle
if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
    print("Yes, these numbers can form a triangle.")
else:
    print("No, these numbers cannot form a triangle.")

# Question 4

# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is greater than 10
if number > 10:
    print("The program will stop.")
else:
    # Calculate the factorial of the number
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is: {factorial}")

# Question 5

# Get five numbers from the user
numbers = []
for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Print the sorted numbers
print("The numbers in descending order are:", numbers)

# Question 6

# Create empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Get 10 numbers from the user
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print the even and odd numbers
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# Question 7

# Get 10 numbers from the user
numbers = []
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# Find the largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

# Calculate the difference
difference = largest - smallest

# Print the difference
print(f"The difference between the largest and smallest numbers is: {difference}")


# Question 8

def is_prime(num):
    """Checks if a number is prime.

    Args:
        num: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """

    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


# Get a number from the user
number = int(input("Enter a number: "))

# Print the prime numbers less than the given number
print("Prime numbers less than", number, ":")
for i in range(2, number):
    if is_prime(i):
        print(i)

# Question 9

# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Reverse the sentence
reversed_sentence = sentence[::-1]

# Print the reversed sentence
print("The reversed sentence is:", reversed_sentence)


# Question 10

def separate_letters_numbers(text):
    """Separates letters and numbers from a string and stores them in separate strings.

    Args:
        text: The string to separate.

    Returns:
        A tuple containing two strings: one with letters and one with numbers.
    """

    letters = ""
    numbers = ""
    for char in text:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            numbers += char
    return letters, numbers


# Get a string from the user
text = input("Enter a string: ")

# Separate letters and numbers
letters, numbers = separate_letters_numbers(text)

# Print the separated letters and numbers
print("Letters:", letters)
print("Numbers:", numbers)


# Question 11

def fibonacci_up_to(n):
    """Generates a list of Fibonacci numbers up to a given number.

    Args:
        n: The maximum number in the Fibonacci sequence.

    Returns:
        A list of Fibonacci numbers less than or equal to n.
    """

    if n < 1:
        return []
    elif n == 1:
        return [1]
    else:
        fib_sequence = [1, 1]
        while fib_sequence[-1] <= n:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence[:-1]


# Get a number from the user
number = int(input("Enter a number: "))

# Print the Fibonacci numbers less than the given number
print("Fibonacci numbers less than", number, ":")
fibonacci_sequence = fibonacci_up_to(number)
print(fibonacci_sequence)


# Question 12

def count_words(sentence):
    """Counts the number of words in a sentence.

    Args:
        sentence: The sentence to count words in.

    Returns:
        The number of words in the sentence.
    """

    # Split the sentence into words
    words = sentence.split()

    # Return the number of words
    return len(words)


# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Count the number of words
number_of_words = count_words(sentence)

# Print the number of words
print("The sentence has", number_of_words, "words.")


# Question 13

def create_user_info_dict():
    """Creates a dictionary to store user information.

    Returns:
        A dictionary containing user information (name, surname, age, location, favorite movie, favorite color).
    """

    user_info = {}
    user_info["name"] = input("What is your name? ")
    user_info["surname"] = input("What is your surname? ")
    user_info["age"] = int(input("How old are you? "))
    user_info["location"] = input("Where are you from? ")
    user_info["favorite_movie"] = input("What is your favorite movie? ")
    user_info["favorite_color"] = input("What is your favorite color? ")
    return user_info


# Create a dictionary to store user information
user_info = create_user_info_dict()

# Print the user information
print("User information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")


# Question 14

def prime_numbers_down_to(n):
    """Generates a list of prime numbers less than or equal to a given number.

    Args:
        n: The maximum number to check for primality.

    Returns:
        A list of prime numbers less than or equal to n.
    """

    prime_numbers = []
    if n >= 2:
        prime_numbers.append(2)
    for num in range(3, n + 1, 2):
        is_prime = True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers


# Get a four


# Question 15


def compare_dates():
    """Compares two dates entered by the user and prints the earlier date.

    Returns:
        None
    """

    def get_date_as_numbers():
        """Gets a date from the user in YYYY/MM/DD format and converts it to a list of integers.

        Returns:
            A list containing the year, month, and day as integers.
        """

        date_text = input("Enter a date in YYYY/MM/DD format: ")
        year, month, day = map(int, date_text.split("/"))
        return [year, month, day]

    # Get the first date
    print("Enter the first date:")
    date1 = get_date_as_numbers()

    # Get the second date
    print("Enter the second date:")
    date2 = get_date_as_numbers()

    # Compare the dates
    if date1 < date2:
        print("The earlier date is:", "/".join(map(str, date1)))
    else:
        print("The earlier date is:", "/".join(map(str, date2)))


# Call the function to compare dates
compare_dates()


# Question 16

def print_colored_characters():
    """Prints a string's characters in different colors based on their type (number, uppercase letter, lowercase letter).

    Args:
        None

    Returns:
        None
    """

    text = input("Enter a string: ")
    color_codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }

    for char in text:
        if char.isdigit():
            color = color_codes["green"]
        elif char.isupper():
            color = color_codes["red"]
        else:
            color = color_codes["blue"]
        print(color + char + color_codes["reset"], end="")


# Call the function to print colored characters
print_colored_characters()


# Question 17

def calculate_fruit_cost():
    """Calculates the total cost of fruits based on user input and a provided fruit price dictionary.

    Returns:
        None
    """

    fruits_dict = {
        "Sib": 15000,
        "Anbe": 23000,
        "Moz": 12000,
        "Portagal": 20000
    }

    # Get quantities of each fruit
    quantities = {}
    for fruit in fruits_dict.keys():
        quantity = int(input(f"How many kilograms of {fruit} did you buy? "))
        quantities[fruit] = quantity

    # Calculate the total cost for each fruit
    total_costs = {}
    for fruit, quantity in quantities.items():
        total_costs[fruit] = fruits_dict[fruit] * quantity

    # Calculate the total cost of all fruits
    total_cost = sum(total_costs.values())

    # Print the total cost for each fruit and the grand total
    print("Fruit costs:")
    for fruit, cost in total_costs.items():
        print(f"{fruit}: {cost}")
    print(f"Grand total: {total_cost}")


# Call the function to calculate fruit cost
calculate_fruit_cost()


# Question 18

def strong_password_checker():
    """Checks if a password meets strong password criteria.

    Returns:
        True if the password is strong, False otherwise.
    """

    password = input("Enter a password: ")
    minimum_length = 8
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special_char = False
    special_chars = "!@#$%^&*"

    # Check password length
    if len(password) < minimum_length:
        print("Password must be at least", minimum_length, "characters long.")
        return False

    # Check for character types
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special_char = True

    # Check if all criteria are met
    if not all([has_uppercase, has_lowercase, has_number, has_special_char]):
        print("Password must contain at least one uppercase letter, lowercase letter, number, and special character.")
        return False

    # Password meets all criteria
    return True


# Check if the user has a strong password
if strong_password_checker():
    print("Your password is strong!")
else:
    print("Please create a stronger password.")


# Question 19

def count_character_occurrences():
    """Prompts the user for a sentence and creates a dictionary to store the frequency of each character.

    Returns:
        None
    """

    sentence = input("Enter a sentence: ")
    char_counts = {}

    for char in sentence:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1

    # Print the character occurrences (excluding spaces)
    print("Character occurrences (excluding spaces):")
    for char, count in char_counts.items():
        if char != " ":
            print(f"{char}: {count}")


# Call the function to count character occurrences
count_character_occurrences()

# Question 20

def calculate_alarm_time_difference(current_time, alarm_time):
  """Calculates the time difference until the alarm goes off for the first time.

  Args:
      current_time: A list containing the current hour (0-23), minute (0-59), and second (0-59).
      alarm_time: A list containing the alarm hour (0-23), minute (0-59), and second (0-59).

  Returns:
      A list containing the time difference in hours, minutes, and seconds.
  """

  # Handle the case where the alarm time is earlier in the day or the same time
  if (alarm_time[0] < current_time[0]) or \
     (alarm_time[0] == current_time[0] and (alarm_time[1] <= current_time[1] or alarm_time[2] < current_time[2])):
    # Add 24 hours to the alarm time
    alarm_time[0] += 24

  # Calculate the difference in hours, minutes, and seconds
  time_diff_hours = alarm_time[0] - current_time[0]
  time_diff_minutes = alarm_time[1] - current_time[1]
  time_diff_seconds = alarm_time[2] - current_time[2]

  # Handle negative minutes or seconds (borrow from hours or minutes)
  if time_diff_minutes < 0:
    time_diff_hours -= 1
    time_diff_minutes += 60
  if time_diff_seconds < 0:
    time_diff_minutes -= 1
    time_diff_seconds += 60

  return [time_diff_hours, time_diff_minutes, time_diff_seconds]

def format_time_difference(time_diff):
  """Formats the time difference into a string in HH:MM:SS format.

  Args:
      time_diff: A list containing the time difference in hours, minutes, and seconds.

  Returns:
      A string representing the formatted time difference.
  """

  return f"{time_diff[0]:02d}:{time_diff[1]:02d}:{time_diff[2]:02d}"

# Get current time as a list
current_time_str = input("Enter the current time (HH:MM:SS): ").split(":")
current_time = [int(x) for x in current_time_str]

# Get alarm time as a list
alarm_time_str = input("Enter the alarm time (HH:MM:SS): ").split(":")
alarm_time = [int(x) for x in alarm_time_str]

# Calculate the time difference
time_diff = calculate_alarm_time_difference(current_time, alarm_time)

# Format and print the time difference
formatted_time_diff = format_time_difference(time_diff)
print(f"Time until alarm: {formatted_time_diff}")




#finish answer