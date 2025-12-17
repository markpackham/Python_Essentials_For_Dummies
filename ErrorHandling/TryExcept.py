import os
# Get current working directory
print(os.getcwd())

# This is just Try & Catch but in Python they use Except
try:
    the_file = open('people.csv')
    print('\n\n', the_file.readline())
    the_file.close()

except FileNotFoundError:
    print('Sorry that file cannot be found here')

except Exception as err:
    print(err)

else:
    # File must be open by now if we got here.
    print('\n') # Print a blank line.
    # Print each line from the file.
    for one_line in the_file:
        print(one_line)
    the_file.close()
    print("Success!")