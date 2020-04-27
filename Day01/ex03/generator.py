def shuffle(lst):
    '''default of this methode is that the elem with 
    the same name will always be together'''
    hash_lst = []
    if isinstance(lst, list):
        for x in lst:
            hash_lst.append((hash(x), x))
        hash_lst.sort()
        for x, y in hash_lst:
            print(x, y)
        return [y for x, y in hash_lst]

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory.
    random module is forbidden for shuffle option'''

    if not isinstance(text, str):
        return "Error"
    lst = text.split()
    if option == "ordered":
        lst = sorted(lst, key=str.casefold)
    elif option == "unique":
        lst = list(dict.fromkeys(lst))
        # set() works too, but will change the order 
    elif option == "shuffle":
        lst = shuffle(lst)
    elif option is None:
        pass
    else:
        return "Error"

    for x in lst:
        yield x



text = "Le Lorem Ipsum est simplement du faux texte. Le Lorem Ipsum est simplement du faux texte."
print('------test option shuffle----')
for word in generator(text, option="shuffle"):
    print(word)
print('------test option unique----')
for word in generator(text, option="unique"):
    print(word)
print('------test option ordered----')
for word in generator(text, option="ordered"):
    print(word)