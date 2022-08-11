from sys import stdin

lst = []

for line in stdin:

    if line.strip() == '':
        break

    a = (int(i) for i in line.split())

    lst.append(a)

for i in lst:
    print(sum(i))