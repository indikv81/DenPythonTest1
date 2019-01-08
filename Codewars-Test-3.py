def namelist(names):
    string = ''
    num = len(names)
    for name in names:
        num -= 1
        string = string + name.get('name') + ', ' * (num > 1) + ' & ' * (num == 1)
    return string
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))

def namelist2(names2):
    string2 = ''
    num2 = len(names2)
    for name2 in names2:
        num2 -= 1
        string2 = string2 + name2.get('name') + ', ' * (num2 >1) + ' и ' * (num2 == 1)
    return string2
print(namelist2([{'name': 'Денис'},{'name': 'Елисей'},{'name': 'Катя'},{'name': 'Николай'},{'name': 'Анастасия'}]))