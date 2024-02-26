from tkinter import Text, Tk
from tkinter.ttk import *

# create a window
window = Tk()

# setting the bg
window.config(bg='pink ')
# setting the geometry of the window
window.geometry('500x500+500+160')
window.iconbitmap('Pellatech.ico')

# creating controls/widget
lb_title = Label(text='Sign In', font=10 )
lb_username = Label(text='Username', font=10, background='Grey')
lb_password = Label(text='Password', font=10, background='Grey')


# title.pack()

# creating Text controls
txt_username = Text(height=2, width=25, background='Grey')
txt_password = Text(height=2, width=25, background='Grey')

# creating Button controls
btn_sign_in = Button(text='Sign in')
btn_sign_in_2 = Button(text='Log In')
# displaying widgets using  Geometry manager
lb_title.pack()
lb_username.place(x=60, y=90)
txt_username.place(y=90, x=150)
lb_password.place(x=60,y=160)
txt_password.place(x=150, y=150)
btn_sign_in_2.place(x=180, y=220)


window.mainloop()