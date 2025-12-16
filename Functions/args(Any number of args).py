# *args let you pass any number of arguments
# WARNING running code this way is slow, only use *args if you really have to

def sorter(*args):
    """ Pass in any number of arguments separated by commas
    Inside the function, they treated as a tuple named args. """
    # Create a list from the passed-in tuple.
    newlist = list(args)
    # Sort and show the list.
    newlist.sort()
    print(newlist)

sorter(1,2,3,-1,-2,-3,1.1,1.2,1.3)