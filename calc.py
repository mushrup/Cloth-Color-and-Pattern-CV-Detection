
from sys import argv

script, a, b, sign = argv

if sign == '+': 
    print(int(a) + int(b))
elif sign == '-':
    print(int(a) - int(b))
else:
    print('I can only add and subtract')
