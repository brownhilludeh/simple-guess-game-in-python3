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






# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Hello Anabel ,chidinma or Chimfunnya, guess a number from 1 to {x}:'))
#         if guess < random_number:
#             print(f'Who ever this is guess what you lost, {guess} is too low.')
#         elif guess > random_number:
#             print(f'Who ever this is guess what you lost, {guess} is too high.')
#      print(f'You guessed the right number congratulations {random_number} was the right guess well I will buy u a car.')

# guess(50)