## Sorteer een lijst met divide and conquer

def divide_and_conquer(my_list):
    ##if list is bigger than 1
    if len(my_list) > 1:
        print('split', my_list)
        mid = len(my_list) // 2
        Split_A = my_list[:mid]
        Split_B = my_list[mid:]

        ##call function itself to sort split halfs
        divide_and_conquer(Split_A)
        divide_and_conquer(Split_B)

        # integers for index purposes
        x = 0  # Split A index
        y = 0  # Split_B index
        z = 0  # my_list index

        # while index kleiner dan Split A & B
        while x < len(Split_A) and y < len(Split_B):

            if Split_A[x] <= Split_B[y]:
                my_list[z] = Split_A[x]
                x += 1
            else:
                my_list[z] = Split_B[y]
                y += 1
            z += 1

        while x < len(Split_A):
            my_list[z] = Split_A[x]
            x += 1
            z += 1

        while y < len(Split_B):
            my_list[z] = Split_B[y]
            y += 1
            z += 1

    print('merg', my_list)


my_list = [12, 3, 76, 23, 9, 53, 44, 38, 99, 11, 5, 39]
divide_and_conquer(my_list)
print('my list: ', my_list)
