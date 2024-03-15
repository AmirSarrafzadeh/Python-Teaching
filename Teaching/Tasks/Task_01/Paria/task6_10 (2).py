#task6

even_numbers = []
odd_numbers = []
for _ in range(0, 10):
    numbers = int(input("enter number: "))
    
    if numbers %2 == 0:
        even_numbers.append(numbers)

    else:
        odd_numbers.append(numbers)
print(even_numbers)
print(odd_numbers)


#task7
my_list = []
for _ in range(0, 10):
    numbers = int(input("enter number: "))
    my_list.append(numbers)

biggest_num = max(my_list)
smallest_num = min(my_list)
print(biggest_num - smallest_num)


#task8
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes_less_than(num):
    primes = [i for i in range(2, num) if is_prime(i)]
    print("Prime numbers less than", num, "are:")
    for prime in primes:
        print(prime)

while True:
    num = input("Enter a three-digit number: ")
    if len(num) == 3 and num.isnumeric():
        num = int(num)
        display_primes_less_than(num)
        break
    else:
        print("Please enter a valid three-digit number.")

#task9
sentence = input("write your sentence: ")
print("".join(reversed(sentence)))


#task10
string_a = "Lkij0986jhjjhs76575bjh879jkms00902kj0099iiu87hjhhSSWe56672hjkmm"

strings = []
numbers = []
length_str = len(string_a)
list_str = list(string_a[0:length_str])

for i in list_str:
    if i.isdigit():
        numbers.append(i)
    elif i.isalpha():
        strings.append(i)
    
print(numbers)
print(strings)