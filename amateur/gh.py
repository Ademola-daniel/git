import _random
import random
list=['king','name','date']
rand=random.choice(list)

no_tries=3
tries=0
while tries != no_tries:
    data=input('Guess: ')
    tries+=1
    if data==rand:
        print('correct Guess')
        break
    elif tries==no_tries:
        print('Out of chances')
        break
    else:
        print('try again')




