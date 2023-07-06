from tkinter import *
import backend


def getSelectedRow(event):
    global selectedRow
    index = listAll.curselection()[0]
    selectedRow = listAll.get(index)
    title_entery.delete(0,END)
    title_entery.insert(END,selectedRow[1])
    author_entery.delete(0,END)
    author_entery.insert(END,selectedRow[2])
    year_entery.delete(0,END)
    year_entery.insert(END,selectedRow[3])
    isbn_entery.delete(0,END)
    isbn_entery.insert(END,selectedRow[4])

    

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

def delete_comands():
    backend.delete(selectedRow[0])

def update_comands():
    backend.update(selectedRow[0],title_text.get(),author_entery.get(),year_text.get(),isbn_text.get())

window = Tk()

window.wm_title('Book Store')

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

update = Button(window,text='Update',width=15,command=update_comands)
update.grid(row=5,column=3)

delete = Button(window,text='Delete',width=15,command=delete_comands)
delete.grid(row=6,column=3)

close = Button(window,text='Close',width=15,command=window.destroy)
close.grid(row=7,column=3)

window.mainloop()