def calc_row_value(input_string):
    """
    input: input_string (str)
    return: value of row of numbers (int)
    """
    if not type(input_string) == str:
        raise ValueError ('input_string must be a string')
    
    total = 0
    for idx, elem in enumerate(input_string):
        index = idx +1
        if index % 2 == 1:
            total += index * int(elem)
        elif index % 2 == 0:
            total -= 5 * int(elem)

    return total


print(calc_row_value('8915715'))

