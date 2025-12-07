import tkinter as tk
from tkinter.filedialog import *
from tkinter import messagebox

window = tk.Tk()
window.title('Address Book')
window.geometry('950x900')  

contacts = {}

def updateContacts():
    nameVal = nameEntry.get()
    addressVal = addressEntry.get()
    mobileVal = mobileEntry.get()
    emailVal = emailEntry.get()
    birthdayVal = birthdayEntry.get()

    if nameVal: 
        contacts[nameVal] = {
            'Address': addressVal,
            'Mobile': mobileVal,
            'Email': emailVal,
            'Birthday': birthdayVal
        }

    listbox.delete(0, tk.END)

    for contact in contacts.keys():
        listbox.insert(tk.END, contact)

    nameEntry.delete(0, tk.END)
    addressEntry.delete(0, tk.END)
    mobileEntry.delete(0, tk.END)
    emailEntry.delete(0, tk.END)
    birthdayEntry.delete(0, tk.END)

def deleteContacts():
    selected = listbox.curselection()

    # for i in selected[:: -1]:
    #     name = listbox.get(i)

    for i in selected:
        name = listbox.get(i)

        if name in contacts:
            del contacts[name]

        listbox.delete(i)
        

    if not selected:
        messagebox.showerror('Deletion', 'No items to delete')
    else:
        messagebox.showinfo('Deletion', 'You have successfully deleted selected contacts')

def editContacts():
    pass

def saveContacts():
    filePath = asksaveasfile(defaultextension = ".txt")
    
    # for name, details in contacts.items():
    #     print(f"Name: {name}", file = filePath)
    #     print(f"Address: {details['Address']}", file = filePath)
    #     print(f"Mobile: {details['Mobile']}", file = filePath)
    #     print(f"Email: {details['Email']}", file = filePath)
    #     print(f"Birthday: {details['Birthday']}", file = filePath)
    #     print(f'', file = filePath)

    if filePath:
        print(contacts, file = filePath)
        listbox.delete(0, tk.END)
        contacts.clear()
    

def openContacts():
    global contacts, listbox

    fileObject = askopenfile(title = 'Open File')

    # if fileObject:
    #     listbox.delete(0, tk.END)
    #     fileData = fileObject.readlines()

    #     for line in fileData:
    #         listbox.insert(tk.END, line)
    if fileObject:
        listbox.delete(0, tk.END)
        contacts.clear()
        contacts = eval(fileObject.read())

        for contact in contacts.keys():
            listbox.insert(tk.END, contact)

def showContacts(event):
    selected = listbox.curselection()
    selectedItems = []
    for i in selected:
        selectedItems.append(listbox.get(i))

    print(selectedItems)
#     messagebox.showinfo(f'Name: {contacts[name]}', f'''Address: {contacts[address]}
# Mobile: {contacts[mobile]}
# Email: {contacts[email]}
# Birthday: {contacts[birthday]}''')

heading = tk.Label(window, text='Address Book App', font=('Verdana', 30), fg="#AAFFAA", bg='#003300', width=200, height=2)
heading.pack()

openBTN = tk.Button(window, font = ('Verdana', 20), text = 'Open Contacts', width = 25, command = openContacts)
openBTN.place(x = 25, y = 125)

editBTN = tk.Button(window, text = 'Edit', font = ('Verdana', 20), width = 10, command = editContacts)
editBTN.place(x = 25, y = 825)

deleteBTN = tk.Button(window, text = 'Delete', font = ('Verdana', 20), width = 10, command = deleteContacts)
deleteBTN.place(x = 275, y = 825)

listbox = tk.Listbox(window, font = ('Verdana', 20), width = 25, height = 18, selectmode = 'multiple')
listbox.place(x = 25, y = 200)
listbox.bind('<<ListboxSelect>>', showContacts)

saveBTN = tk.Button(window, font = ('Verdana', 20), text = 'Save Contacts', width = 25, command = saveContacts)
saveBTN.place(x = 500, y = 125)

updateBTN = tk.Button(window, font = ('Verdana', 20), text = 'Update/Add Contacts', width = 25, command = updateContacts)
updateBTN.place(x = 500, y = 825)

name = tk.Label(window, text = 'Name: ', font = ('Verdana', 15))
name.place(x = 500, y = 200)
nameEntry = tk.Entry(window, font = ('Verdana', 15), width = 25)
nameEntry.place(x = 600, y = 200)

address = tk.Label(window, text = 'Address: ', font = ('Verdana', 15))
address.place(x = 500, y = 325)
addressEntry = tk.Entry(window, font = ('Verdana', 15), width = 25)
addressEntry.place(x = 600, y = 325)

mobile = tk.Label(window, text = 'Mobile: ', font = ('Verdana', 15))
mobile.place(x = 500, y = 450)
mobileEntry = tk.Entry(window, font = ('Verdana', 15), width = 25)
mobileEntry.place(x = 600, y = 450)

email = tk.Label(window, text = 'Email: ', font = ('Verdana', 15))
email.place(x = 500, y = 575)
emailEntry = tk.Entry(window, font = ('Verdana', 15), width = 25)
emailEntry.place(x = 600, y = 575)

birthday = tk.Label(window, text = 'Birthday: ', font = ('Verdana', 15))
birthday.place(x = 500, y = 700)
birthdayEntry = tk.Entry(window, font = ('Verdana', 15), width = 25)
birthdayEntry.place(x = 600, y = 700)


window.mainloop()