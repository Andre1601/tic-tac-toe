import time
import random

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
board = [row1, row2, row3]

# board_number = board

# for i in range(0, 3):
#   for j in range(0, 3):
#     temp = str(i+1) + str(j+1)
#     board_number[i][j] = temp

# print(f"{row1}\n{row2}\n{row3}")

print("The Board Number: \n\
['11', '12', '13']\n\
['21', '22', '23']\n\
['31', '32', '33']")
number = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
character = input("Lets choose your pawn!(X or O)\n").upper()

def rule_the_game():
  if board[0][0] == board[0][1] == board[0][2] == character:
    print("You Win")
    return True
  elif board[1][0] == board[1][1] == board[1][2] == character:
    print("You Win")
    return True
  elif board[2][0] == board[2][1] == board[2][2] == character:
    print("You Win")
    return True
  elif board[0][0] == board[1][0] == board[2][0] == character:
    print("You Win")
    return True
  elif board[0][1] == board[1][1] == board[2][1] == character:
    print("You Win")
    return True
  elif board[0][2] == board[1][2] == board[2][2] == character:
    print("You Win")
    return True
    

while(True):
  if rule_the_game() == True:
    break

  player = input("Your Turn! Please place your pawn: ")
  board[int(player[0])-1][int(player[1])-1] = character
  number.remove(player)
  print(f"{row1}\n{row2}\n{row3}\n")
    
  time.sleep(1.5)

  if rule_the_game() == True:
    break

  if len(number) != 0:
    computer = print("Computer Turn!")
    rand1 = random.choices(number)[0]
    board[int(rand1[0])-1][int(rand1[1])-1] = 'O'
    number.remove(rand1)
    print(f"{row1}\n{row2}\n{row3}\n")
  else:
    break



