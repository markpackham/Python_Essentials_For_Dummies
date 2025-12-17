# Avoid this since it's easy to forget the "close"
f = open('quotes.txt')
filecontents = f.read()
print(filecontents)
f.close()

# Use Contextual syntax "with" so the "close" part already gets done for you
# ---------------- Contextual syntax
with open('quotes.txt') as f:
    filecontents = f.read()
    print(filecontents)
 # The unindented line below is outside the with… block;
print('File is closed: ', f.closed)