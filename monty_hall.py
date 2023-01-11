#make a doors for list and shuffle car and goats.
from random import shuffle, choice
result = {
        'stay_to_win': 0,
        'move_to_win':0,
}
doors = [0,0,1] 
for _ in range(10000):
    shuffle(doors)
    #print(doors)
    user_choice = choice(doors)
    #print(user_choice)
    if user_choice ==0:
        result['move_to_win'] +=1
    else:
        result['stay_to_win]+=1
