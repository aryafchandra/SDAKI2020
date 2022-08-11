from sys import stdin

lst = []

for line in stdin:

    if line.strip() == '':
        break
    else:
        a = int(line) * 2
        
        lst.append(a)

for i in lst:
    print(i)