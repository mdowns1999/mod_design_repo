# def read_board(filename):
#     '''Read the previously existing board from the file if it exists.'''
#     # accepted_file = False
#     # while accepted_file != True:
#     try:
#         with open(filename, 'r') as file:
#             # Put file reading code here.
#             return json.load(file)['board']
#     except:
#         print('Error.  No file found.')


# # def save_board(filename, board):
# #     '''Save the current game to a file.'''
# #     #DUMP SAVES TO FILE. DUMPS you need to use write function
# #     # Put file writing code here.
# #     with open(filename, 'w') as file:
# #         # Put file reading code here.
# #         json.dump({'board': board},file)


# def display_board(board):
#     print(' A B C D E F G H I')
#     for row in range(0,9):
#         print(count)
#         if row == 3 or row == 6:
#             print('------+------+------')
#         for column in range(0,9):
#             print(board[row][column] or ' ', end=' ')
#             # if column == 3:
#             #     seperator = "|"
#             #     print(seperator[column])
#             if column == 8:
#                 print('')
#             #     seperator = "\n"
#             #     print('\n')
#                 # print(seperator[column])
            


# def valid_coordinate(text):
#     valid_letter = ['A', 'B', 'C','D', 'E', 'F','G', 'H', 'I']
#     valid_num = [1,2,3,4,5,6,7,8,9]
#     for letter in text:
#         if letter in valid_letter:
#             return True
#         elif letter.isnumeric in valid_num:
#             return True
#         else:
#             return False

# file = input('Filename: ')

# opened_file = read_board(file)

# # print(opened_file)

# display_board(opened_file)

# def parseInput(text):
#     A = ord('A')
#     Z = ord('Z')
#     for letter in text:
#         if letter.isnumeric():
#             letter = int(letter)
#         else:
#             letter = ord(letter)

#         if A <= letter and letter <= Z:
#             column = letter - A
#         if 1 <= letter <= 9:
#             row = letter - 1
            
#     return row, column

# text = input('Input: ')

# result = parseInput(text)

# print(result)

# file = input('File:')

# board = read_board(file)

# display_board(board)

# text = input('Input: ')

# if valid_input(text):
#     print('Valid!')
# else:
#     print('Invalid')
# text = "A9"
# split = []
# for i in text:
#     split.append(i)

# print(split)

# print('Welcome to Sudoku! Choose the level difficulty you would like to play!\n ')

# print('[1] Easy\n[1]: Medium\n[1]: Hard')

# user_board_choice = input('Enter a number between 1 to 3!: \n>')
# valid_board = False

# while not valid_board:
#     if user_board_choice == 'easy' or user_board_choice == 'Easy' or user_board_choice == '1':
#         file = 'easy.json'
#         valid_board = True
#         return file
#     elif user_board_choice == 'Medium' or user_board_choice == 'Medium' or user_board_choice == '2':
#         file = 'easy.json'
#         valid_board = True
#         return file
#     elif user_board_choice == 'Hard' or user_board_choice == 'hard' or user_board_choice == '2':
#         file = 'easy.json'
#         valid_board = True
#         return file
#     else:
#         print(f'Error.  Please enter one of th echoices listed above.  You entered {user_board_choice}.')

# row = 2
# column = 6

# point = (3,2)

# print(row%column)

avaliable_num = [1,2,3,4,5,6,7,8,9]

for i in range(1,10):
    if i in avaliable_num:
        avaliable_num.remove(i)
print(list1)
