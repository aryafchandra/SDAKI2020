import SDALabADT as ADT

stack = ADT.Stack()
char = input()
S = []
count = 1
correct = True


for i in char:
    x = (i, count)
    if stack.isEmpty():
        stack.push(x)
    elif i == ')' and stack.peek()[0] == '(':
        y = stack.pop()
        S.append((y[1],x[1]))
    elif i == '}' and stack.peek()[0] == '{':
        y = stack.pop()
        S.append((y[1],x[1]))
    elif i == ']' and stack.peek()[0] == '[':
        y = stack.pop()
        S.append((y[1],x[1]))
    elif i in (')','}',']'):
        correct = False
        break
    else:
        stack.push(x)
    count+=1

if not stack.isEmpty():
    correct = False

if correct:
    S = sorted(S)
    print('VALID')
    print(len(S))
    for i in S:
        print(str(i[0]) + " " + str(i[1]))
else:
    print('INVALID')
