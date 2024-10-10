def is_more_than_10_uniques():

    string = input("Enter your text for analysis: ")

    set_string = set(string)
    if len(set_string) > 10:
        print(True)
        return True
    else:
        print(False)
        return False

test = is_more_than_10_uniques()