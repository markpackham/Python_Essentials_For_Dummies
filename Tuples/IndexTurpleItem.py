# Return Index of item in tuple otherwise return -1 if it doesn't exist
prices = (29.95, 9.98, 4.95, 79.98, 2.95, 12345, 0.01)

look_for = 12345
if look_for in prices:
    position = prices.index(look_for)
else:
    position = -1
print(position)