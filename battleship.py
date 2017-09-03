from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print ""
print ""
print ""
print ""
print "WELCOME TO BATTLESHIP, by Antonio Ortega"
print ""
print "You must guess and enter two numeric values from 0 to 4 in order to sink my ship."
print "If at any point you want to leave, just type 'e' and press Enter."
print "Please note that if you already made an attempt, you should enter a valid numeric value before being prompted to enter 'e' to exit."
print ""
print "GOOD LUCK!!! :)"
print ""

print_board(board)
print ""

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


# for loop!
# indented four spaces!

for turn in range(4):
    r = raw_input("Guess Row:")
    if r == 'e':
        print "Thank you for playing! Have a nice day!"
        break
    while not r.isdigit() and 'e':
        r = raw_input("You must enter a Valid Guess Row:")
    guess_row = int(r)

    h = raw_input("Guess Col:")
    if h == 'e':
        print "Thank you for playing! Have a nice day!"
        break
    while not h.isdigit() and 'e':
        h = raw_input("You must enter a valid Guess Col:")
    guess_col = int(h)
    
    if guess_row == ship_row and guess_col == ship_col:
        print ""
        print "Congratulations! You sunk my battleship!"
        print ""
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0     or guess_col > 4):
            print ""
            print "Oops, that's not even in the ocean."
            print "Try again!"
            print ""
        elif(board[guess_row][guess_col] == "X"):
            print ""
            print "You guessed that one already."
            print "Keep up!"
            print ""
        else:
            print ""
            print "You missed my battleship!"
            print "I know you can do better..."
            print ""
            board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
        print_board(board)
    if turn == 3:
        print ""
        print "Don't worry just keep on tr-, wait... G A M E   O V E R"
        print ""
        print 'Sorry!'
        print 'Come back soon! :D'
        break
    elif turn == 2:
        print ""
        print "Strike 3 OUT!!! But no worries, here's one more chance, just because it's you."
        print ""
    else:
        print ""
        print "Strike",turn+1
        print ""
    
