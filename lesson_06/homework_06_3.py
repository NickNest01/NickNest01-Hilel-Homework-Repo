lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

def get_strings_from_list(lst):
    lst2 = []

    for k in lst:
        if isinstance(k, str):
            lst2.append(k)
    print(lst2)

    return lst2

test = get_strings_from_list(lst1)