net = ''
rain = False
wet = True
sun = False


while True:
    net = input('> ')
    ner = net.lower()
    if ner == 'rain':
        if rain:
            print('rain is already falling')

        else:
            rain = True
            print('rain is falling')
    elif ner == 'wet':
        if wet:
            print('it is quite wet today.')
        else:
            wet = True
            print('Due to the rain it is wet')
    else:
        print('rain is not faling')
        break



