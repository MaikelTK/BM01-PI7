##Opdracht 1 Decrease and conquer

def decrease_and_conquer(list):
    index = 0

    #while index < list size
    while index < len(list):
        index_value = list[index]

        while index > 0 and list[index - 1] > index_value:
            list[index] = list[index - 1]
            index -= 1
        print(list)
        list[index] = index_value
        index += 1

my_list = [12, 3, 76, 23, 9, 53, 44, 38, 99, 11, 5, 39]
decrease_and_conquer(my_list)
print('my list: ', my_list)

