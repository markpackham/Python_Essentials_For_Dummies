# The square brackets surrounding the output tell you that it’s a list. Each item in the list is surrounded by quotation marks and separated by commas. The \n at the end of each item is the newline character that ends the line in the file.

# If the file is small don't use readline() unless you only want to read ONE line or use a loop with it, use the plural

# However the plural readlines() can eat a lot of memory

with open('quotes.txt') as f:
    content = f.readlines()
    print(content)

# Only use readline SINGULAR if the file is massive & you have a loop that can handle the size