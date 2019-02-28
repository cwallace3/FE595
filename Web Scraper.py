# Note: I used the class notes and this tutorial video
# ( https://www.youtube.com/watch?v=v5DDW5dyfyc)
# as a guide for this assignment

import requests
from flask import Flask

men = []
women = []
for i in range(50):
    r = requests.get('https://theyfightcrime.org/')

# Raw HTML (look at page source)
# Use find method to locate single tag that matches a pattern in HTML (<P>)
    raw = r.text.split('<P>')
    
# As discussed in class, the '.' is sometimes lost so extract is defined by
# "she's" and "they fight"      
    Male = raw[1].find(" She's")
    Female = raw[1].find(" They fight")
 
# Add to empty matrices    
    men.append(raw[1][:Male])
    women.append(raw[1][Male:Female])
   
# Create Text files     
with open('Men.txt', 'w') as txt:
    txt.write('\n'.join(men))
    txt.close()

with open('Women.txt', 'w') as txt:
    txt.write('\n'.join(women))
    txt.close()

