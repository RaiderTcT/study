import re

l = []
with open('redata.txt', 'r') as f:
    l = f.readlines()

print(l)

pattern = re.compile(r'^(Sun|Mon|Tue|Wed|Thu|Fri|Sat)\s(\w{3})')
m = pattern.match(l[0])
print(m.group())
print(m.groups())
print(m.group(0), m.group(1))
# ？ ： 非贪婪
pattern = re.compile(r'.+?(\d+-\d+-\d+)')
m = pattern.match(l[0])
print(m.group(1))

m = re.split("::", l[0])

print(m)
