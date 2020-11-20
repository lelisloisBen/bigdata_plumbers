## Map reduce with python

import re

# read the file
with open('test.txt', 'r') as myfile:
  mystring = myfile.read()
  text = mystring.lower()

# removing ponctuation
x = re.split(' |\n|:|"|;|\.|\'|!|\?|,|>|<|[0-9]|\(|\)', text)

# create empty list
newstr = []

# looping and append every words to the new list
for word in x:
    if word not in newstr:
        newstr.append(word)

# counting the frequency of each word and print them
for word in range(0, len(newstr)):
    print(newstr[word], text.count(newstr[word]))
