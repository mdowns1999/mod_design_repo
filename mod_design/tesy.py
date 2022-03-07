# list2 = [31,72,32,10,95,50,25,18]
# list1 = [31,32,41,83,59,57]
# ordered_points = [0,0]
# # destination = ['?'] * len(list2)
# # print(destination)


# for i in range(len(list2)-1):
#     print(list2[i])
#     if list2[i] > list2[i + 1]:
#         start_next_section = list2[i + 1]
#         print(f'Start of section 2: {list2[i + 1]}')
            

# print(ordered_points)

            

# print(ordered_points)
# print(list2)
# for i in range(3,4):
#     if list2[i] > list2[i + 1]:
#         print('Swap')
#         list2[i], list2[i + 1] = list2[i + 1], list2[i]

# print(list2)





#             sort_piece(list2[i + 1])

# def sort_piece(piece):
#     for i in range(len(list2)-1):


list1 = [1,3,2,4]

destination = ['?','?','?','?']

set_1 = [0,1]

set_2 = [2,3]

sort = False
i = 0
count1 = 0
count2 = 0

while not sort:

    print(f'{list1[set_1[count1]]} compared to {list1[set_2[count2]]}')

    if list1[set_1[count1]] < list1[set_2[count2]]:

        destination[i] = list1[set_1[count1]]

        count1 += 1
    elif list1[set_1[count1]] > list1[set_2[count2]]:

        destination[i] = list1[set_2[count2]]

        if len(set_2) != 1:
            count2 += 1

    
    elif i == 3:
        sort = True

    i += 1

