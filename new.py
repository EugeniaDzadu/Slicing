from tkinter import Text, Tk
from tkinter.ttk import Button, Entry, Label

window = Tk()

window.config( bg='pink')
window.geometry('500x500+500+160')

def btn_events():
    first = first_number.get()
    first.config(text=f'First Number {first_number}')
    
    two = second_number.get()
    two.config(text=f'Second Number {second_number}')
    
    
def add():
    first_value = first_number.get()
    second_value = second_number.get()
    res_values = int(first_value)+int(second_value)
    result = Label(text=f'the result is {res_values}')
    result.place(x=180, y=120)
    
def product():
    first_value = first_number.get()
    second_value = second_number.get()
    res_values = int(first_value)*int(second_value)
    result = Label(text=f'the result is {res_values}')
    result.place(x=180, y=120)
    
def substraction():
    first_value = first_number.get()
    second_value = second_number.get()
    res_values = int(first_value)-int(second_value)
    result = Label(text=f'the result is {res_values}')
    result.place(x=180, y=120)
    
def division():
    first_value = first_number.get()
    second_value = second_number.get()
    res_values = int(first_value)/int(second_value)
    result = Label(text=f'the result is {res_values}')
    result.place(x=180, y=120)
    
def remainder():
    first_value = first_number.get()
    second_value = second_number.get()
    res_values = int(first_value)%int(second_value)
    result = Label(text=f'the result is {res_values}')
    result.place(x=180, y=120)
    
def Exponent():
    first_value = first_number.get()
    second_value = second_number.get()
    res_values = int(first_value)**int(second_value)
    result = Label(text=f'the result is {res_values}')
    result.place(x=180, y=120)
    
first_number = Entry(width=40)
second_number = Entry(width=40)
# lb_click = Button(text='Click me', command=btn_events)
first = Label(text='First Number', font=2, width=10)
two = Label(text='Second Number', font=2, width=10)
add_up = Button(text='Add', command=add, width=4)
product_show = Button(text='Prod', command=product, width=4)
substract = Button(text='Sub', command=substraction, width=4)
divide = Button(text='Div', command=division, width=4)
remain = Button(text='Rem', command=remainder, width=4)
power = Button(text='Expo', command=Exponent, width=4)


first_number.place(x=150, y=20)
second_number.place(x=150, y=50)
# lb_click.place(x=180, y=120)
first.place(x=30, y=20)
two.place(x=30, y=50)
add_up.place(x=150, y=80)
product_show.place(x=190, y=80)
substract.place(x=230, y=80)
divide.place(x=270, y=80)
remain.place(x=310, y=80)
power.place(x=350, y=80)
# def btn_label():
#     fst = first.g
    
    
# first = Label(text='First Number')




window.mainloop()