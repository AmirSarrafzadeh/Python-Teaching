# Define a dictionary
myDict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Print the dictionary
print(myDict)

# Access value by key
print(myDict["name"])

# Change value by key
myDict["age"] = 35

# Add new key-value pair
myDict["gender"] = "Male"

# Remove a key-value pair
myDict.pop("city")

# Print keys of the dictionary
print(myDict.keys())

# Print values of the dictionary
print(myDict.values())

# Check if a key is in the dictionary
print("name" in myDict)

# Nested dictionary
nestedDict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(nestedDict)
