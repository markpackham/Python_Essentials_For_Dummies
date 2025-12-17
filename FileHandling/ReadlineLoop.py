# Do this for large files rather then readlines() which reads it all in one go & eat up memory like mad
with open('quotes.txt') as f:
    one_line = f.readline()
    while one_line:
        print(one_line, end='')
        one_line = f.readline()