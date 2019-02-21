#!/usr/bin/env python
import string
import random

words = [line.strip() for line in open('./wordlist')]
#the "wordlist" has to be a file and has to be in the same directory for this to work, otherwise please update the directory for your needs

for x in range (0,10):
    pwd = []
    pwd.append(random.choice(string.digits)) #random number 0-9
    pwd.append(random.choice(string.digits))
    pwd.append(random.choice(words))
    pwd.append(random.choice(string.punctuation)) #random punctuation sign like ".", "!", "%" etc.
    print "".join(pwd)
    
#prints 10 passwords such as: 09Influenza!
