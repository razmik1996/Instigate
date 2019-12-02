#!/usr/bin/env python
from tkinter import *
from ClassModule import Date

def output(event):
    dateList = getDates()
    dateList[0].diff(dateList[1])
    
def getDates():
    listDates = []
    date1 = entry_1.get()
    listDate1 = map(int, re.findall(r"\d+", date1))
    if(len(listDate1) == 3):
        p1 = Date.Date(listDate1[0], listDate1[1], listDate1[2])
    else:
        label_3 = Label(root, text = "First input is invalid")
        label_3.grid(columnspan = 2)
        return
    listDates.append(p1)
    date2 = entry_2.get()
    listDate2 = map(int, re.findall(r"\d+", date2))
    if(len(listDate2) == 3):
        p2 = Date.Date(listDate2[0], listDate2[1], listDate2[2])
    else:
        label_3 = Label(root, text = "Second input is invalid")
        label_3.grid(columnspan = 2)
        return
    listDates.append(p2)
    return listDates


root = Tk()
root.title("Count Different")

label_1 = Label(root, text = "First Date")
label_2 = Label(root, text = "Second Date")

entry_1 = Entry(root)
entry_2 = Entry(root)


label_1.grid(row = 0, column = 0, sticky = E)
label_2.grid(row = 1, column = 0, sticky = E)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

c = Button(root, text = "Count Different")
c.grid(columnspan = 2)

c.bind("<Button-1>", output)

root.mainloop()
