
f = open("example.txt", "w")
for i in range(1,4) :
    f.write("Line %d\n" % i)
f.close()

f = open("example.txt", "a")
alphabet = ["A", "B", "C", "D", "E"]
for c in alphabet :
    f.write(c)
f.close()

f = open("example.txt", "r")
data = f.read()
print(data)
f.close()

f = open("example.txt", "r")
while True :
    line = f.readline()
    if not line : break
    print(line, end = "")
f.close()

f = open("example.txt", "r")
data = f.readlines()
for line in data :
    print(line, end = "")
f.close()

f = open("example.txt", "r")
while True :
    print(f.tell(), end = "")
    line = f.readline()
    print(line.strip())
    if not line : break
f.seek(26)
print("after setting a pointer : %d(%s)" % (f.tell(), f.read()[0]))
f.close()

f = open("profile.txt", "w")
name = input("Name : ")
age = input("Age :")
f.write("Name : %s\n" % name)
f.write("Age : %s\n" % age)
f.close()

f = open("alphabet.txt", "w")
f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(65, 91) :
    f.write(chr(i))
f.close()

from tkinter import *
def get_click() :
    lbl2["text"] = txt_box.get(1.0, END)
def ins_click() :
    txt_box.insert(1.0, lbl1["text"])
def del_click() :
    txt_box.delete(1.0, END)
win = Tk()
txt_box = Text(win, width = 40, height = 5)
lbl1 = Label(win, text = "Click the 'insert' button to insert this string.", width = 40, height = 5, bg = "skyblue")
lbl2 = Label(win, text = "Click the 'get' button to import textbox strings\ninto this label.", width = 40, height = 5, bg = "pink")
btn_get = Button(win, text = "get", width = 10, command = get_click)
btn_ins = Button(win, text = "insert", width = 10, command = ins_click)
btn_del = Button(win, text = "delete", width = 10, command = del_click)
txt_box.grid(row = 0, column = 0, columnspan = 3)
lbl1.grid(row = 1, column = 0, columnspan = 3)
lbl2.grid(row = 2, column = 0, columnspan = 3)
btn_get.grid(row = 3, column = 0)
btn_ins.grid(row = 3, column = 1)
btn_del.grid(row = 3, column = 2)
win.mainloop()

f = open("fruit.txt", "r")
fruits = f.readlines()
for word in fruits :
    word = word.strip()
    if len(word) >= 10 :
        print(word.strip())
f.close()

f = open("anna.txt", "r")
lines = f.readline()
lines = lines.split()
for word in lines :
    if  "b" in word :
        print(word)
f.close()
