from tkinter import *


def register_user():
    username_info = username.get()
    password_info = password.get()

    file= open(username_info+'.txt', 'w')
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text='registration succesfull', fg='Lightgreen').pack


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title('Register')
    screen1.geometry('300x250')

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text='Bitte geben Sie Ihre daten ein').pack()
    Label(screen1, text='').pack()
    Label(screen1,text='username *').pack()

    username_entry = Entry(screen1,textvariable = username)
    username_entry.pack()
    Label(screen1,text='pasword *').pack()

    password_entry = Entry(screen1,textvariable= password)
    password_entry.pack()
    Label(screen1, text='').pack()
    Button(screen1,text='register',width=10,height=1, command=register_user).pack()

def login():
    print('login session started')
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('First 1.0')
    Label(text = 'first 1.0', bg = 'skyblue', width ='300', height ='2').pack()
    Label(text='').pack()
    Button(text = 'login', width ='30', height ='2', command=login).pack()
    Label(text='').pack()
    Button(text = ' register',width ='30', height ='2', command =register).pack()

    screen.mainloop()

main_screen()