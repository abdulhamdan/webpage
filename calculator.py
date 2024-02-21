#if/else/calculator/
a=int(input('enter a value : '))
b=int(input('enter b value : '))
op=(input('enter operator(+,-,*,/,%) : '))

if op =='+':
    print(a+b)
elif op =='-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
elif op == '%':
    print(a%b)
else:
    print('invalid')
