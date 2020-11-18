import re

fh = open('actual.txt')
lst = []
for line in fh:
    l = re.findall('[0-9]+', line)
    if len(l)>0:
        for i in l:
            i = int(i)
            lst.append(i)
print(sum(lst))
