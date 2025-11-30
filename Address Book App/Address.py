import tkinter as tk

window = tk.Tk()
window.title('Address Book')
window.geometry('800x800')  

heading = tk.Label(window, text='Address Book App', font=('Verdana', 30), fg="#AAFFAA", bg='#003300', width=200, height=2)
heading.pack()

addressBookLabel = tk.Label(window, font=('Verdana', 20), text = 'My Address Book')
addressBookLabel.place(x = 50, y = 125)

openBTN = tk.Button(window, font = ('Verdana', 20), text = 'Open', width = 10)
openBTN.place(x = 500, y = 125)

listbox = tk.Listbox(window, font = ('Verdana', 20), width = 20, height = 15)
listbox.place(x = 50, y = 200)

editBTN = tk.Button(window, text = 'Edit', font = ('Verdana', 20), width = 10)
editBTN.place(x = 50, y = 725)

deleteBTN = tk.Button(window, text = 'Delete', font = ('Verdana', 20), width = 10)
deleteBTN.place(x = 225, y = 725)

window.mainloop()