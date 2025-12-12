age = 31
if age < 21:
    # If under 21, no alcohol
    beverage = "milk"
elif age >= 21 and age < 80:
    # Ages 21 - 79, suggest beer
    beverage = "beer"
else:
    # If 80 or older, prune juice might be a good choice.
    beverage = "prune juice"
print("Have a " + beverage)