def find_first_names(students_input):
    """
    input: list of a class roster
    return: sorted list of first names in roster
    """

    first_name = []
    for name in students_input:
        first_name.append(name.split()[0].capitalize())
    return sorted(first_name)

print(
    find_first_names([
        'nicholas Jones', 'Ashley Rowland', 'Stephanie Jackson',
        'Donald Hicks', 'evan Johnson'
    ]))