# Use "continue" instead of "break" to jump back to the top of the loop & carry on if the
# continue criteria (eg something weird happens) occurs

answers = ["A", "C", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        continue
print(answer)
print("Loop is done")