import random
answer = random.randint(1, 100)
#print answer for debugging
print(answer)
#username
#Get and print 
#User interation
username = input("Hi, what your name?")
print(f"Hi!!, {username}, choose answer")
guess = int(input('choose number>'))
if guess == answer:
    print(f'you got it right The anser is {answer}) is 52!!')
elif guess>answer:
    print(f,'keep going, man~! That was too high.. {username}...')
elif guess<answer:
    print(f'keep going8 man That was too low, {username}')
