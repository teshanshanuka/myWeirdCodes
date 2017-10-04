from tkinter import *

def add_entry_fields():
    valSet = []
    for textField in e:
        try:
            valSet.append(float(textField.get()))
        except ValueError:
            pass
        textField.delete(0,END)
    if len(valSet) == noOfEntries:
        values.append(valSet)
        # print(valSet)
        print(values)
    else:
        pass
        # Display message



def create_entries():
    global e
    for i in range(noOfEntries):
        Label(master, text = "terminal "+str(i+1)).grid(row=i)
        e.append(Entry(master))
        e[i].grid(row=i,column=1)

master = Tk()

e = []
values = []
noOfEntries = 2

create_entries()
message = Label(master, text = "-")
message.grid(row=noOfEntries, columnspan=2,pady = 5)

Button(master, text='Quit', command=master.quit).grid(row=noOfEntries+1, column=0, sticky=W, pady=4)
Button(master, text='Add', command=add_entry_fields).grid(row=noOfEntries+1, column=1, sticky=W, pady=4)

mainloop( )
