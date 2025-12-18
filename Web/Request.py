# Import the request module from urllib library.
from urllib import request
# URL (address) of the desired page. Use 1st World Wide Web page
sample_url = 'https://info.cern.ch/'
# Request the page and put it in a variable named the_page.

the_page = request.urlopen(sample_url)
# Put the response code in a variable named status.
status = the_page.code
# What is the data type of the page?
print(type(the_page))
# What is the status code?
print(status)