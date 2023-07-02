from tkinter import *

window = Tk()

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

scroll = Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=6)

listAll.configure(yscrollcommand=scroll.set)
scroll.configure(command=listAll.yview)

window.mainloop()