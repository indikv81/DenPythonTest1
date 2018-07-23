def namelist(names):
    string = ''
    num = len(names)
    for name in names:
        num -= 1
        string = string + name.get('name') + ', ' * (num > 1) + ' & ' * (num == 1)
    return string
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))