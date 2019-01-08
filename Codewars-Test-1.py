# 09.01.2019

import re

def disemvowel2(string):
    newstring = ''
    for char in string:
        if char not in 'aoeiu':
            newstring += char
    return newstring

def disemvowel3(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

def disemvowel4(string):
    return string.translate(None, 'aeiouAEIOU')

def disemvowel5(string):
    return re.sub(r"[aeiouAEIOU]", "", string)

def disemvowel6(string):
    for i in "aeiouAEIOU":
        string = string.replace(i,'')
    return string

def disemvowel(string):
    nstr = re.findall(r"[^aeiouAEIOU]*",string)
    return "".join(nstr)

print(disemvowel("This website is for losers LOL!"))