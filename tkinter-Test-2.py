from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry('700x400')

def button_clicked1():
    print("Hello World 1 !")

def button_clicked2():
    print("Hello World 2 !")

def close():
    root.destroy()
    root.quit()

button1 = Button(root, text='Кнопка 1', command=button_clicked1)
button1.grid(row=0,column=0)
button2 = Button(root, text="Кнопка 2", command=button_clicked2)
button2.grid(row=0,column=1)

listbox1=Listbox(root, height=5, width=15, selectmode=EXTENDED)
listbox2=Listbox(root, height=5, width=15, selectmode=SINGLE)
list1=["Москва", "Санкт-Петербург", "Саратов", "Омск"]
list2=["Канберра", "Сидней", "Мельбурн", "Аделаида"]
for i in list1:
    listbox1.insert(END,i)
for i in list2:
    listbox2.insert(END,i)
listbox1.grid(row=1, column=0)
listbox2.grid(row=1, column=1)

frame1=Frame(root, bg='green', bd=5)
frame2=Frame(root, bg='red', bd=5)
button3=Button(frame1, text='Первая кнопка')
button4=Button(frame2, text='Вторая кнопка')
frame1.grid(row=2, column=0)
frame2.grid(row=2, column=1)
button3.pack()
button4.pack()

var1=IntVar()
var2=IntVar()
check1=Checkbutton(root, text='1 пункт', variable=var1, onvalue=1, offvalue=0)
check2=Checkbutton(root, text='2 пункт', variable=var2, onvalue=1, offvalue=0)
check1.grid(row=3, column=0)
check2.grid(row=3, column=1)

var=IntVar()
rbutton1=Radiobutton(root, text='1', variable=var, value=1)
rbutton2=Radiobutton(root, text='2', variable=var, value=2)
rbutton3=Radiobutton(root, text='3', variable=var, value=3)
rbutton1.grid(row=4, column=0)
rbutton2.grid(row=4, column=1)
rbutton3.grid(row=4, column=2)

def getV(root):
    a = scale1.get()
    print("Значение: " + str(a))
    text.delete('1.0', END)
    text.insert('1.0', "Значение: " + str(a))
scale1 = Scale(root, orient=HORIZONTAL, length=300, from_=50, to=80, tickinterval=5, resolution=5)
button5 = Button(root, text="Получить значение")
scale1.grid(row=5, column=0)
button5.grid(row=5, column=1)
button5.bind("<Button-1>", getV)

text = Text(root, height=3, width=60)
text.grid(row=6, column=0)
scrollbar = Scrollbar(root)
scrollbar.grid(row=6, column=1)
# первая привязка
scrollbar['command'] = text.yview
# вторая привязка
text['yscrollcommand'] = scrollbar.set

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()