def plus(x, y):
    z = x + y
    return z

def minus(x, y):
    z = x - y
    return z

def mnozh(x, y):
    z = x * y
    return z

def delen(x, y):
    z = x / y
    return z

print('Фунцiя додавання - 1\nфунцiя вiднiмання - 2\nфункцiя множення - 3\nфункцiя дiлення - 4\n' )
    

num = int(input('Виберiть функцiю:' ))

if num == 1:
    a = float(input('введiть перше число: '))
    b = float(input('введiть друге число: '))
    print('вiдповiдь: ')
    print(plus(a,b))

if num == 2:
    a = float(input('введiть перше число: '))
    b = float(input('введiть друге число: '))
    print('вiдповiдь: ')
    print(minus(a,b))

if num == 3:
    a = float(input('введiть перше число: '))
    b = float(input('введiть друге число: '))
    print('вiдповiдь: ')
    print(mnozh(a,b))

if num == 4:
    a = float(input('введiть перше число: '))
    b = float(input('введiть друге число: '))
    print('вiдповiдь: ')
    print(delen(a,b))
