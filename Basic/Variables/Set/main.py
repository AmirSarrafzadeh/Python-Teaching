# Define a set
mySet = {1, 2, 3, 4, 5, "apple", "banana", "cherry"}

# Print the set
print(mySet)

# Add an element to the set
mySet.add(6)

# Remove an element from the set
mySet.remove("apple")

# Check if an element is in the set
print(3 in mySet)

# Union of two sets
anotherSet = {"banana", "orange", "grape"}
unionSet = mySet.union(anotherSet)
print(unionSet)

# Intersection of two sets
intersectionSet = mySet.intersection(anotherSet)
print(intersectionSet)

# Difference of two sets
differenceSet = mySet.difference(anotherSet)
print(differenceSet)
