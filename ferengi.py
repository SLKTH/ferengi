# Import urllib for getting data from an url
# Import random for generating a random key out of the dictionary
# Import BeautifulSoup for making HTML come in beautiful

import urllib
import random
from BeautifulSoup import *

# No copyright infrigment intended: thanks Stephen Jacob!
# I generate this content from his website: www.sjtrek.com
# Please show your support and take a look ;-)

# The URL
url = 'http://www.sjtrek.com/trek/rules/'

# From the urllib library: Open/Retrieve URL and read() text
html = urllib.urlopen(url).read()

# Use BeautifulSoup library to tidy HTML
soup = BeautifulSoup(html)

# Index all <li> tags which contains a number and a Ferengi rule
tags = soup('li')

# A dictionary for all the rules ('Oh silly me. But of course, it's a dictionary!')
x = {}

# Fill the dictionary with all the table contents (rule & rule number)
for il in tags:
    x[il.get('value', None)] = str(il.contents[0])

# Pick a random dictionary item
randomdict = random.choice(x.keys())  

# Output the magic.
print "Rule Number " + randomdict + ":" + x[randomdict]
    

