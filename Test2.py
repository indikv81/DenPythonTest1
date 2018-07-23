class myclass:
    arg1 = 'Я первое свойство класса'
    arg2 = 'Я второе свойство класса'

    def __init__(self, arg0):
        print('Я ' + arg0 + ' класса, я родился')

    def gethello(self, username):
        s = 'Привет, ' + username
        return s

a = myclass('первый экземпляр')
print(a.gethello('Елена'))

print(a.arg1)
a.arg2 = 'Новое значение второго свойства'
print(a.arg2)

c = myclass('второй экземпляр')
print(c.arg2)

class myclass2(myclass):
    arg3 = 'Я третье свойство, меня не было в myclass'

    def getgoodbye(self, username):
        s = 'До свидания, ' + username
        return s

d = myclass2('экземпляр дочернего')
print(d.arg1)
print(d.arg2)
print(d.arg3)
print(d.gethello('Артём'))
print(d.getgoodbye('Артём'))

class myclass3(myclass2):
    def gethello(self, username):
        s = 'Саламалейкум, о уважаемый ' + username
        return s

e = myclass3('класс унаследованный от myclass2')
print(e.gethello('Артём'))

class myclass4(myclass3):
    def gethello(self, username):
        s = 'Привет чувак ' + username
        return s

f = myclass4('класс унаследованный от myclass3')
print(f.gethello('Артём'))