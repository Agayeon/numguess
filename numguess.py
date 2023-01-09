from random import randint

# Generate answer
answer= randint(1, 100)

# print answer for debugging
print(answer)

#user interaction
username=input("What's your name?")
print("Hello, {}!!".format(username))

guess = int(input("choose one number(1~100), {}!".format(username)))
        print("{}!! you choose {}".format(username.guess))

