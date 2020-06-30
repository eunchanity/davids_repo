def my_func(divisors, lower, upper):
    '''
    input: 
        divisors: list of numbers
        lower: int
        upper: int
    return:
        function returns a dictionary -
            key: elements in the list of divisors
            value: list of numbers in range from lower to upper that are divisible by key 
    '''

    my_dict = dict()

    for elem in divisors:
        my_dict[elem] = []

        for num in range(lower,upper+1):
            if num % elem == 0:
                my_dict[elem] += [num]
    
    return my_dict

print(my_func([1,2,5],2,4))