dictionary={
    'king':'The royal one',
    'is':'with others',
    'here':'is here'
}

data=input('> ')
data2=data.split(' ')
output=' '
for i in data2:
    output+=dictionary.get(i ,'!') + ' '

print(output)
