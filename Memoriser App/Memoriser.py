import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import *

window = tk.Tk()
window.title('Memoriser App')
window.geometry('800x900')

def add():
    listbox.insert(tk.END, entryBox.get())
    entryBox.delete(0, tk.END)

    #messagebox.showinfo('Addition', 'You have successfully added items')

def delete():
    selected = listbox.curselection()

    for i in selected[:: -1]:
        listbox.delete(i)

    if not selected:
        messagebox.showerror('Deletion', 'No items to delete')
    else:
        messagebox.showinfo('Deletion', 'You have successfully deleted selected items')

def clear():
    listbox.selection_clear(0, tk.END)
    messagebox.showinfo('Unselection', 'You have successfully unselected all items')

def get():
    selected = listbox.curselection()
    print(selected)
    for i in selected:
        messagebox.showinfo('Get Item', listbox.get(i))

def save():
    filePath = asksaveasfile(defaultextension = '.txt')

    if filePath:
        for listItem in listbox.get(0, tk.END):
            print(listItem, file = filePath)

        listbox.delete(0, tk.END)

def open():
    fileObject = askopenfile(title = 'Open File')

    if fileObject:
        listbox.delete(0, tk.END)

        #Reading from a file
        fileData = fileObject.readlines()

        for line in fileData:
            listbox.insert(tk.END, line)

heading = tk.Label(window, text = 'Memoriser App', font = ('Verdana', 30), fg = '#0CCE6B', bg = '#363537', width = 200, height = 2)
heading.pack()

getValueBtn = tk.Button(window, text = 'GET', font = ('Verdana', 20), command = get)
getValueBtn.place(x = 50, y = 125, width = 200)

deleteBtn = tk.Button(window, text = 'DELETE', font = ('Verdana', 20), command = delete)
deleteBtn.place(x = 300, y = 125, width = 200)

clearSelection = tk.Button(window, text = 'CLEAR', font = ('Verdana', 20), command = clear)
clearSelection.place(x = 550, y = 125, width = 200)

addBtn = tk.Button(window, text = 'ADD', font = ('Verdana', 20), command = add)
addBtn.place(x = 550, y = 225, width = 200)

openBtn = tk.Button(window, text = 'OPEN', font = ('Verdana', 20), command = open)
openBtn.place(x = 50, y = 225, width = 200)

saveBtn = tk.Button(window, text = 'SAVE', font = ('Verdana', 20), command = save)
saveBtn.place(x = 300, y = 225, width = 200)

entryBox = tk.Entry(window, font = ('Verdana', 30))
entryBox.place(x = 50, y = 325, width = 700)

listbox = tk.Listbox(window, font = ('Verdana', 20), width = 41, height = 13, selectmode = tk.MULTIPLE)
listbox.place(x = 50, y = 400)

window.mainloop()
