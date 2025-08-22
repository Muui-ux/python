# Create an empty list
my_list = []

# Append into list
my_list.append (10)
my_list.append (20)
my_list.append (30)
my_list.append (40)

# Print list
print(my_list)

# Insert 15 into second position
my_list.insert(1, 15)
print(my_list)

# Extend list with more values
my_list.extend([50, 60, 70])
print(my_list)

# Remove last element
my_list.pop()
print(my_list)

# Sort in ascending order
my_list.sort()
print(my_list)

# Find and print index of 30
print(my_list.index(30))

# Results
print("Final list:", my_list)
print("Index of 30:", my_list.index(30))
