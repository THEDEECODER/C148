# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 17:35:01 2022

@author: admin
"""

from tkinter import*
import random
root = Tk()
root.geometry("500x500")
root.title("PicNic")

randomlist = ["Sheets, Notebook, Pencil, Food, Friends, Family, Water"]
sortedlist = Label(root)
     
def rlist():
    items = random.sample(range(0,6),1)
    randomlist["text"] = " List: " + str(items)
    rnumb.sort()
    sortedlist["text"] = " Put item no " + str(items) + "In Bag"

btn = Button(root, text = "Generate Random List", command= rlist)
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)
randomlist.place(relx = 0.5, rely = 0.5, anchor=CENTER)
sortedlist.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()