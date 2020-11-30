#Determining Lotto Numbers
import random
from tkinter import *

#Create window object
window=Tk()

#define three labels Title Author Year
l1=Label(window, text="Title")
l1.grid(row=0, column=0)

l1=Label(window, text="Author")
l1.grid(row=0, column=0)

l1=Label(window, text="Year")
l1.grid(row=0, column=0)

l1=Label(window, text="Age")
l1.grid(row=0, column=0)

l1=Label(window, text="Nationality")
l1.grid(row=0, column=0)

#define Entries
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=1,column=1)

author_text=StringVar()
author_text = StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=2,column=1)

year_text=StringVar()
year_text = StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=3,column=1)

age_text=StringVar()
age_text = StringVar
e4=Entry(window,textvariable=age_text)
e4.grid(row=4,column=1)

nationality_text=StringVar()
nationality_text = StringVar()
e5=Entry(window,textvariable=nationality_text)
e5.grid(row=5,column=1)

#define ListBox
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#Attach scrollbar to the list
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(comman=list1.yview)

#Define buttons
b1=Button(window, text="Select", width=12)
b1.grid(row=2, column=3)

b1=Button(window, text="Enter", width=12)
b1.grid(row=6, column=3)


#Initialise six random numbers (between1and49)
lotteryNumbers = []

for i in range (0,6):
  number = random.randint(1,50)

#Check if this number has already been picked and ..
  while number in lotteryNumbers:
    # .. if it has, pick a new number instead
    number = random.randint(1,50)

#Now that we have a unique number, let's append it to our list.
  lotteryNumbers.append(number)

#Sort the list in ascending order
lotteryNumbers.sort()

#Display the list on screen:
print("Today's lottery numbers are: ")
print(lotteryNumbers)
#Sort the list in ascending order
lotteryNumbers.sort()

#Display the list on screen:
print("Today's lottery numbers are: ")
print(lotteryNumbers)

window.mainloop()
