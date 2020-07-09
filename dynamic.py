'''

'''


import DFmodule as df
import tkinter as tk


def dynamicDisplay():
    global message

    display = message


message = input('Enter message:')
message = df.encrypt(message)

top = tk.Tk()
top.title('DYNAMIX')

a1 = tk.Label(top, text='Encrypted Message', fg='blue')

b = tk.Entry(top, text='Encrypt!', command=dynamicDisplay)

a1.pack()
b.pack()
top.mainloop()
