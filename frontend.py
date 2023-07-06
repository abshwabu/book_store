from tkinter import *
import backend
window = Tk()

def getSelectedRow(event):
    index = listAll.curselection()[0]
    selectedRow = listAll.get(index)
    print(selectedRow)

def view_all():
    listAll.delete(0,END)
    for row in backend.viewAll():
        listAll.insert(END, row)

def search_comands():
    listAll.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        listAll.insert(END, row)


def add_comands():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

title = Label(window,text='title')
title.grid(row=0,column=0)

author = Label(window,text='author')
author.grid(row=0,column=2)

year = Label(window,text='year')
year.grid(row=1,column=0)

isbn = Label(window,text='isbn')
isbn.grid(row=1,column=2)

title_text = StringVar()
title_entery = Entry(window,textvariable=title_text)
title_entery.grid(row=0,column=1)

year_text = StringVar()
year_entery = Entry(window,textvariable=year_text)
year_entery.grid(row=1,column=1)

author_text = StringVar()
author_entery = Entry(window,textvariable=author_text)
author_entery.grid(row=0,column=3)

isbn_text = StringVar()
isbn_entery = Entry(window,textvariable=isbn_text)
isbn_entery.grid(row=1,column=3)

listAll = Listbox(window,height=6,width=35)
listAll.grid(row=2,column=0,rowspan=6,columnspan=2)

listAll.bind('<<ListboxSelect>>',getSelectedRow)

scroll = Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=6)

listAll.configure(yscrollcommand=scroll.set)
scroll.configure(command=listAll.yview)

viewAll = Button(window,text='View All',width=15,command=view_all)
viewAll.grid(row=2,column=3)

search = Button(window,text='Search',width=15,command=search_comands)
search.grid(row=3,column=3)

add = Button(window,text='Add',width=15,command=add_comands)
add.grid(row=4,column=3)

update = Button(window,text='Update',width=15)
update.grid(row=5,column=3)

delete = Button(window,text='Delete',width=15)
delete.grid(row=6,column=3)

close = Button(window,text='Close',width=15)
close.grid(row=7,column=3)

window.mainloop()