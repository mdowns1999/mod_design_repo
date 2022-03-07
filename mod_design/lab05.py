# 1. Name:
#      Mike Downs
# 2. Assignment Name:
#      Lab 05 : Sudoku Program
# 3. Assignment Description:
#     Working Game of Suduko with working rules
# 4. What was the hardest part? Be as specific as possible.
#   The hardest part for me was figuring out the check square and display hints option.  The other functions I was able to figure out.  I did need to ask for help on those
# two functions.  I was graetful to get help from the TA and my teammates on those two functions.
# 5. How long did it take for you to complete the assignment?
#      3.5 Hours

import json


def main():
    # user_file_input = input('Where is your board located?: ')

    user_file_input = choose_board()
    #Get the Board
    board = read_board(user_file_input)
    user_input = ''
    while user_input != 'Q' or 'q':
        display_board(board)

        #Validate the users coordinates
        user_input = valid_input(board)
        if user_input == 'q':
            save_board(user_file_input, board)
            break

        #Send the point to the board to update it.
        point = parseInput(user_input)
        print(point)
        row = point[0]
        column = point[1]




        #Get Guess
        user_guess = guess_in_board(board, row, column, user_input)

        if user_input == 's':
            num_options(board, row, column)

        #Update the Board
        board = update_board(board, row, column, user_guess)

def valid_input(board):
    """This function will prompt the user and call another function to check the input until it is correct. """
    valid = False
    while not valid:
        user_input = input("Specify a coordinate to edit or 'Q' to save and quit: \n>\u001b[1m") #\u001b[1m Will bold the input
        print('\u001b[0m', end='') #Will Unbold Line
        if valid_coordinate(user_input) and len(user_input) == 2:
            if spot_filled(user_input, board) == False:
                valid = True
            else:
                print('Spot is already filled on the board.')
                valid = False
        elif user_input.lower() =='q':
            valid = True
        else:
            print(f'Invalid input.  Please enter a coordinate like "D1"  You entered: {user_input}.')
            valid = False
    return user_input

def valid_user_guess(user_guess):
    """ This function will make sure the users guess is a number and nothing else. """
    valid_guess = False
    while not valid_guess:
        if user_guess.isnumeric():
            return True
        if user_guess.lower() == 's':
            return True
        else:
            print(f'Error.  Please enter a number from 1 to 9 or s for valid options.  You entered {user_guess}')

def valid_coordinate(text):
    """This function will validate the user's guess and make sure it is in a letter/number format (Like A9) """
    valid_letter = ['A', 'B', 'C','D', 'E', 'F','G', 'H', 'I', 'a','b','c','d','e','f','g','h','i']
    valid_num = [1,2,3,4,5,6,7,8,9]
    split_string = []

    for part in text:
        split_string.append(part)

    part1 = split_string[0]
    part2 = split_string[1]
    if part1.isnumeric():
        part1 = int(part1)
    if part2.isnumeric():
        part2 = int(part2)

    if part1 in valid_letter or part1 in valid_num:
        if part2 in valid_letter or part2 in valid_num:
            return True
    
    elif part2 in valid_letter or part2 in valid_num:
        if part1 in valid_letter or part1 in valid_num:
            return True

    else:
        return False

def parseInput(text):
    """This function will take the users letter and number input and return a coordinate so it can be put on the board """
    A = ord('A')
    Z = ord('Z')
    for letter in text:
        if letter.isnumeric():
            letter = int(letter)
        else:
            letter = letter.upper()
            letter = ord(letter)

        if A <= letter and letter <= Z:
            column = letter - A
        if 1 <= letter <= 9:
            row = letter - 1
            
    return row, column

def display_board(board):
    """THis function will display the Suduko board """
    count = 1
    print('  A B C   D E F   G H I')
    for row in range(0,9):
        if row == 3 or row == 6:
            print('------+------+------')
        print(row + 1, end=" ")
        for column in range(0,9):
            if column == 3 or column == 6:
                print("|", end=' ')
            print(board[row][column] or ' ', end=' ')

            if column == 8:
                print('')

def update_board(board, row, column, user_guess):
    """This function will update the board with the user's guess. """
    board[row][column] = user_guess
    return board

def guess_in_board(board, row, column, user_input):
    """This function will get the user's guess and make sure it is correct. """
    avaliable = False
    user_guess = ''
    while not avaliable:
        # ADD WHILE LOOP TO CHECK FOR s
        user_guess = input(f'What number goes in {user_input}? ')
        user_guess_valid = valid_user_guess(user_guess)

        if user_guess == 's':
            num_options(board, row, column)
            avaliable = False
        else:
            user_guess = int(user_guess)
            if 1 <= user_guess and user_guess <= 9:
                if spot_avaliable(board, row, column, user_guess):
                    avaliable = True
                    return user_guess
                else:
                    avaliable = False
                    print('Invalid guess.  Number is already in the row, column, or square.')
            else:
                print('Please guess a number between 1 and 9.')

def check_row(user_guess, row, board):
    """This function will check the 'board' rows to make sure there are no matching numbers to the user's guess. """
    if user_guess in board[row]:
        return True
    else:
        return False

def check_column(user_guess, row, column, board):
    """This function will check the 'board' columns to make sure there are no matching numbers to the user's guess. """

    for i in range(len(board)):
        if user_guess == board[i][column]:
            return True
    return False

def spot_filled(user_input, board):
    """This function will check if the spot is filled """
    point = parseInput(user_input)
    row = point[0]
    column = point[1]

    if board[row][column] == 0:
        return False
    else:
        return True

def check_box(row, column, board, user_guess):
    begin_row_point = (row // 3) * 3
    begin_column_point = (column // 3) * 3

    for r in range(begin_row_point, begin_row_point + 3):
        for c in range(begin_column_point, begin_column_point + 3):
            if board[r][c] == user_guess:
                return True
    return False

def spot_avaliable(board, row, column, user_guess):
    """This function determines if the spot is avaliable to place the user guess. """
    if check_row(user_guess, row, board) == False:
        return True
    if check_column(user_guess, row, column, board) == False:
        return True
    if check_box(row, column, board, user_guess) == False:
        return True
    return False

def num_options(board, row, column):
    avaliable_num = [True] * 9
    # avaliable_num = []

    for i in range(1, len(avaliable_num) + 1):
        if avaliable_num[i - 1]:
            avaliable_num[i - 1] = not check_row(i, row, board)
        if avaliable_num[i - 1]:
            avaliable_num[i - 1] = not check_column(i, row, column, board)
        if avaliable_num[i - 1]:
            avaliable_num[i - 1] = not check_box(row, column, board, i)
    
    print('The Aviable Numbers are:')
    print([i+1 for i, x in enumerate(avaliable_num) if x])

def choose_board():
    print('\nWelcome to Sudoku! Choose the level difficulty you would like to play!\n ')

    print('[1] Easy\n[2]: Medium\n[3]: Hard')
    valid_board = False

    while not valid_board:
        user_board_choice = input('Enter a number between 1 to 3!: \n>')

        if user_board_choice == 'easy' or user_board_choice == 'Easy' or user_board_choice == '1':
            file = 'easy.json'
            valid_board = True
            return file
        elif user_board_choice == 'Medium' or user_board_choice == 'Medium' or user_board_choice == '2':
            file = 'medium.json'
            valid_board = True
            return file
        elif user_board_choice == 'Hard' or user_board_choice == 'hard' or user_board_choice == '3':
            file = 'hard.json'
            valid_board = True
            return file
        else:
            print(f'Error.  Please enter one of th echoices listed above.  You entered {user_board_choice}.')
            valid_board = False

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        with open(filename, 'r') as file:
            # Put file reading code here.
            return json.load(file)['board']
    except:
        print('Error.  No file found.  Please try again.')

def save_board(filename, board):

    '''Save the current game to a file.'''
    #DUMP SAVES TO FILE. DUMPS you need to use write function
    # Put file writing code here.
    with open(filename, 'w') as file:
        # Put file reading code here.
        json.dump({'board': board},file)

main()