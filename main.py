import random
players=[]

                
def roll():
    while True:
        ans = input('would you like to roll the dice? y/n ').lower()
        if ans in ['y', 'n']:
            break
        else:
            print('please enter y or n')
    if ans == 'y':
        value = random.randint(1,6)
        return value
    elif ans == 'n':
        value = 0
        print('you choose not to roll the dice')
        return value
        

def number_player():
    while True:
        players_number = input('number of players')
        if players_number.isdigit():
            players_number=int(players_number)
            if players_number >1:
                break
            else:
                print("please enter at least 2 or more players ")
        else:
            print('enter a valid number')
    for _ in range(players_number):
        players.append(0)
    print(players)
    while True:
        for _ in range(players_number):
            if players[_]>49:
                return
        for _ in range(players_number):
            total = 0
            print(f'player {_+1}:')
            
            while True:
                value = roll()
                if total+players[_]>49:
                    print(f'player {_+1} wins as total is already 50 or above')
                    return
                elif value == 0:
                    break
                elif value == 1:
                    print(f'you rolled a 1 hence your total is now 0 and your universal total is {players[_]} ')
                    total=0
                    break
                elif value == 2 or 3 or 4 or 5 or 6:
                    total += value
                    print(f'you rolled a {value} hence your current total is {total} and your universal total is {players[_]}')
                    if players[_] >= 50:
                        print(f'player {_+1} wins')
                        return
            players[_] += total
    

number_player()

