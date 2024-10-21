test_array = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']

def list_items_total(lst):
    total1 = []

    for k in lst:
        total2 = 0

        split_lst= k.split(',')
        try:
            for i in split_lst:
                total2 += int(i)
            total1.append(total2)
        except ValueError:
            total1.append('Can\'t do this!')
        except TypeError:
            total1.append('Can\'t do this!')

    print(total1)

list_items_total(test_array)