# define a list of numbers and cars
myList = [1, 2, 3, 4, 5, "Audi", "BMW", "Mercedes", "Toyota", "Honda"]

# Print the list
print(myList)

# Print the length of the list
print(len(myList))

# Print the first element of the list
print(myList[0])

# Print the last element of the list
print(myList[-1])

# Print the first 5 elements of the list
print(myList[0:5])

# Print the last 5 elements of the list
print(myList[-5:])

# Print the list in reverse
print(myList[::-1])

# Append an element to the list
myList.append("Nissan")

# Pop an element from the list
myList.pop()

# Extend the list with another list
myList.extend([6, 7, 8, 9, 10])

# Insert an element at a specific index
myList.insert(5, "Ford")

# Remove an element from the list
myList.remove("Mercedes")

# Count the number of times an element appears in the list
print(myList.count("Toyota"))

# Find the index of an element in the list
print(myList.index("BMW"))







