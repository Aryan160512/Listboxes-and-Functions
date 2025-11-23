import tkinter as tk

window = tk.Tk()
window.title('Memoriser App')
window.geometry('800x800')

heading = tk.Label(window, text='Memoriser App', font=('Verdana', 30), fg='#0CCE6B', bg='#363537', width=200, height=2)
heading.pack()

getValueBtn = tk.Button(window, text = 'GET', font = ('Verdana', 20))
getValueBtn.place(x = 50, y = 125, width = 200)

deleteBtn = tk.Button(window, text = 'DELETE', font = ('Verdana', 20))
deleteBtn.place(x = 300, y = 125, width = 200)

clearSelection = tk.Button(window, text = 'CLEAR', font = ('Verdana', 20))
clearSelection.place(x = 550, y = 125, width = 200)

addBtn = tk.Button(window, text = 'ADD', font = ('Verdana', 20))
addBtn.place(x = 550, y = 225, width = 200)

entryBox = tk.Entry(window, font = ('Verdana', 30))
entryBox.place(x = 50, y = 225, width = 450)

listbox = tk.Listbox(window, font = ('Verdana', 20), width = 41, height = 13)
listbox.place(x = 50, y = 325)


window.mainloop()