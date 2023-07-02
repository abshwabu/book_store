from tkinter import *

window = Tk()

title = lable(window,text='title')
title.grid(row=0,column=0)

author = lable(window,text='author')
author.grid(row=0,column=0)

year = lable(window,text='year')
year.grid(row=0,column=0)

isbn = lable(window,text='isbn')
isbn.grid(row=0,column=0)

window.mainloop()