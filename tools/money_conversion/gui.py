from tkinter import *
from money_conversion import Currency


def convert(event=None):
    """
        The main function used to pipe user input through the Currency class and return the values to UI.
    :param event: tkinter event
    :return: None
    """
    entered_value = money_entry.get()
    c = Currency(entered_value)

    # Clear text in `denarius` field and add new text.
    denarius.delete(0.0, END)
    denarius.insert(END, c.in_denarius)

    # Clear text in `£sd` field and add new text.
    lsd.delete(0.0, END)
    lsd.insert(END, c.in_lsd)

    # Clear text in `marks` field and add new text.
    m.delete(0.0, END)
    m.insert(END, c.in_marks)


def close_window():
    root.destroy()
    exit()

# Initialize the tkinter window
root = Tk()
root.title('Convert Money')

# set background color
root.configure(background='#245602')

# Create boundary measurements for tkinter window frame
title_frame = Frame(root, width=450, height=100)
title_frame.grid(row=0, column=0, padx=10, pady=2)
entry_frame = Frame(root, background='#245602', width=450, height=100)
entry_frame.grid(row=1, column=0, columnspan=3, padx=25)
output_frame = Frame(root, background='#245602', width=250, height=250)
output_frame.grid(row=4, column=0, columnspan=2)
output_frame.grid_rowconfigure(3, weight=1)
output_frame.grid_columnconfigure(1, weight=1)

Label(title_frame, text='Convert Monetary Values', bg='#245602', fg='white', font='none 12 bold')\
    .grid(row=1, column=0, sticky=E)

# Monetary entry frame
Label(entry_frame, text='Enter Value', bg='#245602', fg='white', font='none 12 bold')\
    .grid(row=1, column=0, sticky=E)
money_entry = Entry(entry_frame, bg='white')
money_entry.bind('<Return>', convert)
money_entry.grid(row=1, column=1,)
Button(entry_frame, text='Convert', width=7, highlightbackground='#245602', command=convert)\
    .grid(row=2,column=1, sticky=E)

# create another label
Label(output_frame, text='\nConverted Values', bg='#245602', fg='white', font='none 12 bold')\
    .grid(row=1, column=0, sticky=W)

# create box for Denarius
Label(output_frame, text='\nIn Denarius:', bg='#245602', fg='white', font='none 12 bold')\
    .grid(row=2, column=0, sticky=E)
denarius = Text(output_frame, width=10, height=1, background='white')
denarius.grid(row=2, column=1, sticky=SW)

# create box for £sd
Label(output_frame, text='\nIn £sd:', bg='#245602', fg='white', font='none 12 bold')\
    .grid(row=3, column=0, sticky=E)
lsd = Text(output_frame, width=10, height=1, background='white')
lsd.grid(row=3, column=1, sticky=SW)

# create box for Marks
Label(output_frame, text='\nIn Marks:', bg='#245602', fg='white', font='none 12 bold')\
    .grid(row=4, column=0, sticky=E)
m = Text(output_frame, width=10, height=1, background='white')
m.grid(row=4, column=1, sticky=SW)

# create exit button
Button(root, text='Exit', width=4, highlightbackground='#245602', command=close_window)\
    .grid(row=10, column=0, sticky=W)

# run tkinter.
root.mainloop()
