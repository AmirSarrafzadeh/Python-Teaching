# 1. Function to add two numbers
def add(a, b):
    return a + b


# 2. Function to subtract two numbers
def subtract(a, b):
    return a - b


# 3. Function to multiply two numbers
def multiply(a, b):
    return a * b


# 4. Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


# 5. Function to check if a number is even
def is_even(num):
    return num % 2 == 0


# 6. Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 7. Function to find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# 8. Function to reverse a string
def reverse_string(s):
    return s[::-1]


# 9. Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]


# 10. Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


# 11. Function to find the maximum element in a list
def find_max(lst):
    return max(lst)


# 12. Function to find the minimum element in a list
def find_min(lst):
    return min(lst)


# 13. Function to count the occurrences of each character in a string
def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


# 14. Function to check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


# 15. Function to calculate the nth term of the arithmetic sequence
def arithmetic_sequence(n, first_term, common_difference):
    return first_term + (n - 1) * common_difference


# Test the functions
if __name__ == "__main__":
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(6, 7))
    print(divide(15, 3))
    print(is_even(7))
    print(is_prime(11))
    print(factorial(5))
    print(reverse_string("hello"))
    print(is_palindrome("racecar"))
    print(fibonacci(10))
    print(find_max([3, 8, 1, 6, 9]))
    print(find_min([3, 8, 1, 6, 9]))
    print(count_characters("hello"))
    print(are_anagrams("listen", "silent"))
    print(arithmetic_sequence(5, 2, 3))
