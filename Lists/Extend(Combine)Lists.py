# Create two lists of Names.
list1 = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
list2 = ["Huey", "Dewey", "Louie", "Nader", "Bubba"]

# Add list2 names to list1.
list1.extend(list2)
# Print list 1.
print(list1)
print()

# You can use "+" instead of extend
print("You can use "+" instead of extend")
print(list1+list2+list1+list2)