import random
def guess():
    n = random.randint(1,50)
    g = 0
    while g != n:
        g = int(input('Hello, Guess a number '))
        if g < n:
            print('Too low')
        elif g > n:
            print('Too high')
    print('Good brain')
guess()
