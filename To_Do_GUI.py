# To Do List (10/2) - TO DO LIST GUI
# Part 1: Create the GUI elements

# Part 3: Delete All, Sort (ASC), Sort (DES), Choose Random, Number
# Part 4: Add one, delete one


import tkinter
from tkinter import *
# tkinter is the standard GUI library for Python
# it provides a robust and platform independent windowinf toolkit
import random

#Creating root window
root = Tk()

# this Changes the root window background color
root.configure(bg = "white")

# This Changes the title of root Window..
root.title("To Do Application")

# Change the window size
root.geometry("325x325")

#window can not be resized..
root.resizable(False, False)

# Create an empty list for tasks .
tasks = []


# For testing purposes, use a default list
# tasks = ["look into Smooch.io specifications", "listen to podcasts", "do hackerrank challenges"]

def sample():
    print("hello user")
    print("your task: %s " % (txt_input.get()))


lbl_title = Label(root, text = "Manage Your Task Here", bg = "white", fg = "blue", font = "Times",  justify =CENTER,  compound = CENTER)
lbl_title.grid(row = 0, column = 0)

lbl_display = Label(root, text = "Write Task Below.", bg="white" , fg = "red", font = "Helvetica 12 bold italic")
lbl_display.grid(row = 0, column = 1)

#         Label(root,
# 		 text="Blue Text in Verdana bold",
# 		 fg = "blue",
# 		 bg = "yellow",
# 		 font = "Verdana 10 bold").pack()

txt_input = Entry(root, width = 20)
txt_input.grid(row = 1, column = 1)

btn_add_task = Button(root, text = "Add to-do item", bg = "white", command = sample)
btn_add_task.grid(row = 1, column = 0)
# go create the add_task function (can create an empty function)

btn_del_all = Button(root, text = "Clear all tasks", bg = "white", command = sample)
btn_del_all.grid(row = 2, column = 0)

btn_del_one = Button(root, text = "Remove", bg = "white", command = sample)
btn_del_one.grid(row = 3, column = 0)

btn_sort_asc = Button(root, text = "Ascending \nSort", bg = "white", command = sample)
btn_sort_asc.grid(row = 4, column = 0)

btn_sort_desc = Button(root, text = "Sort (DESC)", bg = "white", command = sample)
btn_sort_desc.grid(row = 5, column = 0)

btn_choose_random = Button(root, text = "Choose Random", bg = "white", command = sample)
btn_choose_random.grid(row = 6, column = 0)

btn_number_of_tasks = Button(root, text = "Number of Tasks", bg = "white", command = sample )
btn_number_of_tasks.grid(row = 7, column = 0)

btn_exit = Button(root, text = "Exit", bg = "white", command = exit)
btn_exit .grid(row = 8, column = 0)

lb_tasks = Listbox(root)
lb_tasks.grid(row = 2, column = 1, rowspan = 7)
# lb for listbox

# Start the main events loop
root.mainloop()
