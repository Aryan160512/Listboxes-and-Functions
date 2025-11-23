import tkinter as tk
from tkinter import messagebox

def showMessagebox(event):
    data = listbox1.curselection()
    print(data)
    selected_item = []

    for i in data:
        value = listbox1.get(i)
        selected_item.append(value)
    messagebox.showinfo('Selected Items', f'Your selected items are {selected_item}')

def addElement():
    listbox1.insert(tk.END, entryBox.get())
    entryBox.delete(0, tk.END)

def deleteElement():
    selected_indices = listbox1.curselection()

    for i in selected_indices[:: -1]:
        listbox1.delete(i)

    messagebox.showinfo('Deletion', 'Items Successfully Deleted')


window = tk.Tk()
window.geometry('800x800')

listbox1 = tk.Listbox(window, font = ('Verdana', 20), width = 30, height = 10, selectmode = tk.MULTIPLE)
listbox1.pack(pady = 20)

for fruit in ['Apple', 'Banana', 'Orange', 'Strawberry']:
    listbox1.insert(tk.END, fruit)

#Adding Click Event to a Listbox
#listbox1.bind('<<ListboxSelect>>', showMessagebox)

entryBox = tk.Entry(window, font = ('Verdana', 30))
entryBox.pack(pady = 20)

addBtn = tk.Button(window, font = ('Verdana', 20), text = 'ADD', width = 30, command = addElement)
addBtn.pack(pady = 20)

deleteBtn = tk.Button(window, font = ('Verdana', 20), text = 'DELETE', width = 30, command = deleteElement)
deleteBtn.pack(pady = 20)

#listbox1.selection_clear(0, tk.END)

window.mainloop()