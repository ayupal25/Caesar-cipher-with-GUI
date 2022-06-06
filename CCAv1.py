from tkinter import *

def cipher():
    mess = message.get()
    sh = int(s.get())
    result = ""
    for i in range(len(mess)):
        char = mess[i]
        if (char.isupper()):
            result += chr((ord(char) + sh - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + sh - 97) % 26 + 97)
        else:
        	result += char
    ans_label.delete('1.0', END)
    ans_label.insert(END, result)

def decipher():
    mess = message.get()
    sh = int(s.get())
    sh = 26-sh
    result = ""
    for i in range(len(mess)):
        char = mess[i]
        if (char.isupper()):
            result += chr((ord(char) + sh - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + sh - 97) % 26 + 97)
        else:
        	result += char
    ans_label.delete('1.0', END)
    ans_label.insert(END, result)

enc = Tk()
enc.title("Caesar Cypher Encryptor")

enc.geometry("400x400")

head=Label(enc, text="Caesar Cypher Encryptor", font=("Times New Roman", 20))
head.place(relx = 0.5, rely = 0.03, anchor = CENTER)

Label(enc, text="Enter the message").place(relx = 0.35, rely = 0.1)
message=Entry(enc)
message.place(relx = 0.33, rely = 0.15)

Label(enc, text="Enter the shift value").place(relx = 0.35, rely = 0.2)
s=Entry(enc)
s.place(relx = 0.33, rely = 0.25)

addbutton = Button(enc, text = "ENCRYPT", command=cipher)
addbutton.place(relx = 0.32, rely = 0.32)

addbutton = Button(enc, text = "DECRYPT", command=decipher)
addbutton.place(relx = 0.5, rely = 0.32)

answer_box=Label(enc, text="Result", font=(10)).place(relx = 0.43, rely= 0.4 )
ans_label= Text(enc, height=10, width=48)
ans_label.place(relx = 0.01, rely = 0.5)

enc.mainloop()