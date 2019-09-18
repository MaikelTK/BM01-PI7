def reverse_string(string):

    print('Normal string: ', string)
    new_string = ''
    string_index = len(string) - 1

    while string_index > -1:
        new_string += string[string_index]
        print(new_string)
        string_index -= 1
    print('reverse string: ', new_string)

string_a = 'Jim_Vliegen'
reverse_string(string_a)
