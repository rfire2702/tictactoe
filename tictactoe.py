# tic-tac-toe
# author = Siddhant Chandra Kulshrestha

from os import system

def print_board(score):
    print(score[6] , '|' , score[7] , '|' , score[8])
    print("--+---+---")
    print(score[3] , '|' , score[4] , '|' , score[5])
    print("--+---+---")
    print(score[0] , '|' , score[1] , '|' , score[2])

def checkall(char):
    if score[0] == char and score[1] == char and score[2] == char:
        return True
    elif score[3] == char and score[4] == char and score[5] == char:
        return True
    elif score[6] == char and score[7] == char and score[8] == char:
        return True
    elif score[0] == char and score[3] == char and score[6] == char:
        return True
    elif score[1] == char and score[4] == char and score[7] == char:
        return True
    elif score[2] == char and score[5] == char and score[8] == char:
        return True
    elif score[0] == char and score[4] == char and score[8] == char:
        return True
    elif score[2] == char and score[4] == char and score[6] == char:
        return True
    return False

def place_marker(marker, position):
    score[position] = marker

def full():
    if ' ' not in score:
        return True


score = [1,2,3,4,5,6,7,8,9]
system('cls')
print('Welcome to TIC-TAC-TOE')
print_board(score)
while True:    
    score = [' '] * 9
    #print_board(score)
    while True:
        flag = 0
        if full():
            break
        while True:
            try: 
                x = int(input('Enter position you want to enter:- '))
                if score[x-1] != 'X' and score[x-1] != 'O':
                    place_marker('X', x - 1)
                    break
                else:
                    print("Position already taken")
                    continue
            except:
                print("Enter Valid Number")
                continue
        system('cls')
        print_board(score)
        if checkall('X'):
            print("Player 1 wins.")
            break
        if full():
            flag = 1
            break
        while True:
            try:
                y = int(input('Enter position you want to enter:- '))
                if score[y-1] != 'X' and score[y-1] != 'O':
                    place_marker('O', y - 1)
                    break
                else:
                    print("Position already taken")
                    continue
            except:
                print("Enter Valid Number")
                continue
        system('cls')
        print_board(score)
        if checkall('O'):
            print("Player 2 wins.")
            break
        if full():
            flag = 1
            break
    if flag == 1:
        print("Tie Game")
    choice = input("Wanna play again? Type yes or no:- ")
    if choice.lower() == 'yes':
        score = [1,2,3,4,5,6,7,8,9]
        system('cls')
        print('Welcome to TIC-TAC-TOE')
        print_board(score)
        continue
    elif choice.lower() == 'no':
        break
    else:
        print("No Valid input. Exiting Game")
        break    
