# A tuple can’t be modified
# You have to use parentheses to create them
prices = (29.95, 9.98, 4.95, 79.98, 2.95) 

print(len(prices)) 

# You can use .count() to see how many times an item appears in a tuple
print(prices.count(4.95)) 

# You can use in to see whether a value exists in a tuple which returns True or False
print(4.95 in prices)