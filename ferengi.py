# Import urllib for getting data from an url
# Import random for generating a random key out of the dictionary
# Import BeautifulSoup for making HTML come in beautiful

import urllib
import random
from BeautifulSoup import *
import sys

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

# Fill the dictionary with all the table contents (rule (minus whitespace) & rule number).
for il in tags:
    x[il.get('value', None)] = str(il.contents[0].strip())

# Pick a random dictionary item
randomdictkey = random.choice(x.keys())  
randomdictvalue = x[randomdictkey]

# If the value is 223, then it contains an <i> tag and I'm making an exception: replace the value
if randomdictkey == 223:
    randomdictvalue = "Beware the man who doesn't make time for oo-mox."
    
# Output the magic.
print "Rule Number " + str(randomdictkey) + ": " + randomdictvalue
