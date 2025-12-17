import os
# Get current working directory
print(os.getcwd())

# This is just Try & Catch but in Python they use Except

# A variable that starts out False.
file_is_open = False

try:
    # Open the file named people.csv
    the_file = open("people.csv")
 # Watch for common error and stop program if it happens.
except FileNotFoundError:
    print("Sorry, I don't see a file named people.csv here")
 # Otherwise, if nothing bad has happened by now, just keep going.
else:
    # File must be open by now. Set the open status to True.
    file_is_open = True
    # Show the file contents.
    for one_line in the_file:
        print(one_line)
finally:
    # This executes no matter what. So if the file is open, it's closed.
    if file_is_open:
        the_file.close()
    print("File is closed now")