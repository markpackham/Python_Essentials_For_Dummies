# All params with a default argument must be put at the end

# If you want to list both required parameters and optional parameters in a function, you have to put all the required ones first (in any order). Then the optional parameters can be listed after that with their = signs (in any order).

def hello(fname, lname, datestring=''):
    msg = 'Hello ' + fname + ' ' + lname
    if len(datestring) > 0:
        msg += ' The date is ' + datestring
    print(msg)

hello('Bob', 'Smith', '11/11/2020')
hello('John', 'Smith', '')