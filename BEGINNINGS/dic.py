def function():
    counter = 0
    while counter < 5:
        yield counter
        counter +=1


for x in function():
    print((lambda x: x**2)(x))

