from tkinter import *
import csv

def add_entry_fields():
    valSet = []
    for row in entries:
        rowValSet = []
        for textField in row:
            try:
                rowValSet.append(float(textField.get()))
            except ValueError:
                pass
            textField.delete(0,END)
        if len(rowValSet) == rowSize-1:
            valSet.append(rowValSet)
    if len(valSet) == colSize:
        values.append(valSet)
        # print(values)
        with open('data.csv','wb') as csvf:
            w = csv.writer(csvf, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in valSet:
                w.writerow(row)

def create_table(rowLabels, columnLabels, title):
    global entries
    Label(master, text=title).grid(row=0, columnspan=len(columnLabels)+1)
    for i in range(len(columnLabels)):
        Label(master, text = columnLabels[i]).grid(row=1, column=i+1)
    for i in range(len(rowLabels)):
        Label(master, text = rowLabels[i]).grid(row=i+2)
        e=[]
        for j in range(len(columnLabels)):
            e.append(Entry(master)) if i != j else e.append(Entry(master, state = 'disabled'))
            e[j].grid(row=i+2,column=j+1)
        entries.append(e)

master = Tk()

entries = []
values = []

l=['T'+str(i+1) for i in range(3)]
rowSize = colSize = len(l)

create_table(l,l,'MyTable')
message = Label(master, text = "-")
message.grid(row=len(l)+2, columnspan=len(l)+1,pady = 5)

Button(master, text='Quit', command=master.quit).grid(row=len(l)+3, column=0, sticky=W, pady=4)
Button(master, text='Add', command=add_entry_fields).grid(row=len(l)+3, column=1, sticky=W, pady=4)
# Button(master, text='Check', command=check_vals).grid(row=len(l)+3, column=2, sticky=W, pady=4)

mainloop( )
