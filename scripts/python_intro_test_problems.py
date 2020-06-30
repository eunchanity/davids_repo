def remove_adjacent(nums):
    '''
    input: list of int
    return: list of int, elem is not the same number as previous elem
    '''
    if not len(nums):
        return []
    
    my_list = [nums[0]]

    for elem in nums:
        if not my_list[-1] == elem:
            my_list.append(elem)
        if my_list[-1] == elem:
            continue

    return my_list


print(remove_adjacent([3,2,3,3,3,1,1]))


#second problem involved sorted(function, key=lambda x:x[-1])