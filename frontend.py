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

window.mainloop()