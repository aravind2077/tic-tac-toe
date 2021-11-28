import random
import os
from IPython.display import clear_output
#to display the board
def display():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("     |   |  ")
    print("   "+cell[0]+" | "+cell[1]+" | "+ cell[2])
    print("     |   |  ")
    print("===============")
    print("     |   |  ")
    print("   "+cell[3]+" | "+cell[4]+" | "+ cell[5])
    print("     |   |  ")
    print("===============")
    print("     |   |  ")
    print("   "+cell[6]+" | "+cell[7]+" | "+ cell[8])
    print("     |   |  ")

# to place mark on board
def place_slot(position, mark):
    cell[position-1]= mark

# to check if mark is made on board already
def check_slot(position, slots_taken):
    while position in slots_taken:
        position= int(input("Slot already taken, Please use a different slot"))
    else:
        return position

# to check if win condition has been satisfied or not
def check_win():
    if ((cell[0]==cell[1] and cell[1]==cell[2]) or (cell[3]==cell[4] and cell[4]==cell[5]) or (cell[6]==cell[7] and cell[7]==cell[8]) or (cell[0]==cell[3] and cell[3]==cell[6]) or (cell[1]==cell[4] and cell[1]==cell[7]) or (cell[2]==cell[5] and cell[5]==cell[8]) or (cell[0]==cell[4] and cell[4]==cell[8]) or (cell[2]==cell[4] and cell[4]==cell[6])):
        return False
    else:
        return True

# to check if draw condition is satisfied or not
def check_draw(slots_taken):
    if len(slots_taken) == 9:
        print("Draw")
        return False

cell= ['1','2','3','4','5','6','7','8','9']

def start():
    slots_taken=[]
    cell= ['1','2','3','4','5','6','7','8','9']
    display()
    game1= True
    if random.randint(0, 1) == 0:
        player= 'Player 2'
    else:
        player= 'Player 1'
    print(player+" goes first")
    while game1:
        if player == 'Player 1':
            con= check_draw(slots_taken)
            if con== False:
                break
            position= int(input('Player 1 choose slot'))
            position= check_slot(position, slots_taken)
            place_slot(position, 'X')
            slots_taken.append(position)
            display()
            con= check_win()
            if con== False:
                print(player+" wins !!!")
                break
            player= 'Player 2'
        
        else:
            con= check_draw(slots_taken)
            if con== False:
                break
            position= int(input('Player 2 choose slot'))
            position= check_slot(position, slots_taken)
            place_slot(position, 'O')
            slots_taken.append(position)
            display()
            con= check_win()
            if con== False:
                print(player+" wins !!!")
                break
            player= 'Player 1'
            
def main():
    game= True
    while(game):
        print("Would you like to play TIC TAC TOE?\nYES OR NO")
        play= input()
        if play.lower() =='no':
            print("Goodbye!!!")
            game= False
        elif play.lower()== 'yes':
            start()
            print("\nThanks for playing\n")
        else:
            print('\nInvalid input! please try again\n')

if __name__ == "__main__":
    main()