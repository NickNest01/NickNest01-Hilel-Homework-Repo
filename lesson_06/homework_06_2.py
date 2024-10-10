def must_have_h():

    contain_h = False

    while contain_h != True:
        text = input('Please, enter text that contains the letter "h": ')

        if 'h' in text.lower():
            return True
        else:
            continue


test = must_have_h()