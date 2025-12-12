# A while loop keeps going while a variable named counter is less than 10. Inside the loop, the variable named number is assigned a random number in the range of 1 to 999.

import random
print("Odd numbers")
counter = 0
while counter < 10:
    # Get random number
    number = random.randint(1,999)
    if int(number / 2) == number / 2:
        # If even don't print
        continue
    # If odd print it
    print(number)
    counter += 1
    print("Loop is done")