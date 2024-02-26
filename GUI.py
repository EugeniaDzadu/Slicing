import tkinter as tk
from tkinter.ttk import Button

window = tk.Tk(className='Pellatech')
window.config(width=500, height=500, bg='Grey')
window.geometry('500x500+500+160')
window.iconbitmap('Pellatech.ico')

# adding controls/widgets
btn_click = Button(text='Click me')
btn_click_2 = Button(text='Second Click me')

# btn_click.pack(ipadx=90, ipady=10, pady=10)
btn_click.place(x=40, y=40)
btn_click_2.pack()


window.mainloop()