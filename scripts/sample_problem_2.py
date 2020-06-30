def my_func(string1, string2):
    '''
    input: string1(str) and string2(str)
    return:
        function returns True if string1 can be created from the elem in string2
        letters in string2 can only be used once
    '''
    lower_string1 = string1.lower()
    lower_string2 = string2.lower()

    my_dict = {}

    for elem2 in lower_string2:
        my_dict[elem2] = lower_string2.count(elem2)
    for elem1 in lower_string1:
        if elem1 in my_dict.keys():
            my_dict[elem1] -= 1
        elif not elem1 in my_dict.keys():
            my_dict[elem1] = 0
            my_dict[elem1] -= lower_string1.count(elem1)
    
    my_list = sorted(list(my_dict.values()))
    if my_list[0] < 0:
        return False
    elif my_list[0] >= 0:
        return True

print(my_func('helllo','hello'))