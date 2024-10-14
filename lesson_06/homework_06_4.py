lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def sum_all_even(lst):
    _sum = 0

    for i in lst:
        if i % 2 == 0:
            _sum = _sum + i

    print(_sum)
    return _sum

test = sum_all_even(lst)