data = int(input('> '))
try:
    a = data
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('Mathematical Error')
finally:
    print('Welcome!')
