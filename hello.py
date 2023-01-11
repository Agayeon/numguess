from random import randint
from time import sleep

answer = random.randint(1, 100)

#print answer for debugging
print(answer)

username = input("Hi, what your name?")
print(f"Hi!!, {username}, choose answer")
guess = int(input('choose number>'))
print(f'Well choice {username}~~ You picked {guess}!!')

if guess == answer:
    print(f'You got it right!! The answer is {answer}!!')
elif guess>answer:
    print(f,'keep going, man~! That was too high.. {username}...')
elif guess<answer:
    print(f'keep going8 man That was too low, {username}')
