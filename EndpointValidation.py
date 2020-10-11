#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:02:48 2020

@author: ram
"""
import mysql.connector as msqlc
import os
import filecmp as fc
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
bad_chars = ["'", '(', ')', ","]
bchars = ["'", '(', ')', '[', ']']
mydb = msqlc.connect(
    host="localhost",
    user="XXX",
    passwd="XXX",
    database="XXX",
    auth_plugin='mysql_native_password'
)
mc = mydb.cursor(buffered=True)
# ***********************************************************************************


def new_window():
    win1 = Tk()
    win1.configure(bg="#edebeb")
    win1.geometry("400x400")
    tframe = LabelFrame(win1, text="ENTER THE VALUES", bg="#edebeb")
    label1 = Label(tframe, text="Enter Code id", bg="#edebeb", justify=LEFT)
    label3 = Label(tframe, text="Enter Test file path",
                   bg="#edebeb", justify=LEFT)
    label2 = Label(tframe, text="Enter Test case path",
                   bg="#edebeb", justify=LEFT)
    entry1 = Entry(tframe)
    entry2 = Entry(tframe)
    entry3 = Entry(tframe)

    def browsefunc():
        filename = fd.askopenfilename()
        entry2.insert(END, filename)

    def browsefunc1():
        filename = fd.askopenfilename()
        entry3.insert(END, filename)

    def validate():
        try:
            id = entry1.get()
            mc.execute("select paths from details where moid= '{}'".format(id))
            x = str(mc.fetchone())
            for i in bad_chars:
                x = x.replace(i, '')
            path = entry2.get()
            try:
                os.system("python3 '{}' > file.txt".format(x))
                if(fc.cmp("file.txt", path, shallow=False)):
                    messagebox.showinfo("Validation", "Successful validation")
                    mc.execute(
                        "update scode set valid='y' where soid='{}'".format(id))
                    mydb.commit()
                else:
                    messagebox.showerror("Validation", "Test case Failed")
            except:
                messagebox.showerror("Validation", "Error in program")
        except:
            path = entry2.get()
            x = entry3.get()
            try:
                os.system("python3 '{}' > file.txt".format(x))
                if(fc.cmp("file.txt", path, shallow=False)):
                    messagebox.showinfo("Validation", "Successful validation")
                    mc.execute(
                        "update scode set valid='y' where soid='{}'".format(id))
                    mydb.commit()
                else:
                    messagebox.showerror("Validation", "Test case Failed")
            except:
                messagebox.showerror("Validation", "Error in program")

    b = Button(win1, text="test", command=validate,
               bg="#edebeb", height=2, width=6, relief=RAISED)
    b1 = Button(tframe, text="choose", command=browsefunc,
                bg="#edebeb", height=2, width=6, relief=RAISED)
    b2 = Button(tframe, text="choose", command=browsefunc1,
                bg="#edebeb", height=2, width=6, relief=RAISED)
    tframe.pack(fill=X)
    label1.grid(row=0)
    entry1.grid(row=0, column=1)
    label2.grid(row=2)
    entry2.grid(row=2, column=1)
    label3.grid(row=1)
    entry3.grid(row=1, column=1)
    b1.grid(row=2, column=10)
    b2.grid(row=1, column=10)
    b.pack()
    win1.mainloop()
# ***********************************************************************************


def new_window1():
    win1 = Tk()
    win1.configure(bg="#edebeb")
    win1.geometry("400x400")
    tframe = LabelFrame(win1, text="MODULE CHECK", bg="#edebeb")
    label1 = Label(tframe, text="module name", bg="#edebeb")
    entry1 = Entry(tframe)

    def reqcheck():
        id = entry1.get()
        mc.execute(
            "select fmat from details d, scode s where d.moid=s.soid and s.mname='{}'".format(id))
        y = str(mc.fetchone())
        for i in bad_chars:
            y = y.replace(i, '')
        mc.execute(
            "select moid from details d, scode s where d.moid=s.soid and s.mname='{}'".format(id))
        x = str(mc.fetchone())
        for i in bad_chars:
            x = x.replace(i, '')
        mc.execute("select version from details where moid= '{}'".format(x))
        z = str(mc.fetchone())
        for i in bad_chars:
            z = z.replace(i, '')
        mc.execute("select vers from requirements where reqname= '{}'".format(y))
        vers = str(mc.fetchone())
        for i in bad_chars:
            vers = vers.replace(i, '')
        if z == vers:
            messagebox.showinfo("Verifiction", "Successful")
        else:
            messagebox.showerror("Verification", "Version error")
    b = Button(win1, text="test", command=reqcheck,
               height=2, width=6, relief=RAISED)
    tframe.grid(row=0)
    label1.grid(row=0)
    entry1.grid(row=0, column=1)
    b.grid(row=1)
    win1.mainloop()
# ***********************************************************************************


def new_window2():
    win1 = Tk()
    tframe = LabelFrame(win1, text="ENTER THE MODULE", bg="#edebeb")
    bframe = LabelFrame(win1, text="DETAILS OF MODULE", bg="#edebeb")
    messagebox.showwarning("Warning", "Careful while entering values")
    win1.geometry("400x400")
    l1 = Label(tframe, text="module id", bg="#edebeb")
    e1 = Entry(tframe)
    l2 = Label(tframe, text="module name", bg="#edebeb")
    e2 = Entry(tframe)
    l3 = Label(bframe, text="path", bg="#edebeb")
    e3 = Entry(bframe)
    l4 = Label(bframe, text="format", bg="#edebeb")
    e4 = Entry(bframe)
    l5 = Label(bframe, text="version", bg="#edebeb")
    e5 = Entry(bframe)
    l6 = Label(tframe, text="stage id", bg="#edebeb")
    e6 = Entry(tframe)

    def browsefunc():
        filename = fd.askopenfilename()
        e3.insert(END, filename)
    mc.execute("select soid from scode order by soid desc")
    x = str(mc.fetchone())
    print(x)
    for i in bad_chars:
        x = x.replace(i, '')
    mc.execute("select sid,sname from stage")
    y = str(mc.fetchall())
    for i in bchars:
        y = y.replace(i, '')
    print(y)
    l7 = Label(win1, text="last module id = {}".format(x), bg="#d6bb1e")
    l8 = Label(win1, text="stages: {}".format(y), bg="#d6bb1e")

    def insertval():
        id1 = e1.get()
        nam = e2.get()
        path = e3.get()
        fmt = e4.get()
        vers = e5.get()
        st = e6.get()
        mc.execute(
            "insert into scode values('{}','{}','{}','n')".format(id1, nam, st))
        mydb.commit()
        mc.execute("insert into details values('{}','{}','{}','{}')".format(
            path, id1, vers, fmt))
        mydb.commit()
        messagebox.showinfo("Entry", "Successful")
    b = Button(win1, text="Insert", command=insertval,
               height=2, width=6, relief=RAISED)
    b1 = Button(win1, text="Exit", command=win1.quit,
                height=2, width=6, relief=RAISED)
    b3 = Button(win1, text="Refersh", command=lambda: [
                win1.quit, new_window2()], height=2, width=6, relief=RAISED)
    b2 = Button(bframe, text="choose", command=browsefunc,
                bg="#edebeb", height=2, width=6, relief=RAISED)
    l1.grid(row=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1)
    e2.grid(row=1, column=1)
    l3.grid(row=0)
    e3.grid(row=0, column=1)
    b2.grid(row=0, column=10)
    l4.grid(row=1)
    e4.grid(row=1, column=1)
    l5.grid(row=2)
    e5.grid(row=2, column=1)
    l6.grid(row=2)
    e6.grid(row=2, column=1)
    tframe.pack(fill=X)
    bframe.pack(fill=X)
    b.pack()
    b1.pack()
    b3.pack()
    l7.pack(fill=X)
    l8.pack(fill=X)
    win1.mainloop()


# ***********************************************************************************
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)
root.geometry("800x600")
# ***********************************************************************************
tframe = LabelFrame(root, text="VALIDATE", bg="#fcfcfc")
b = Button(tframe, text="validation", command=new_window,
           height=2, width=6, relief=RAISED)
l = Label(
    tframe, text="This helps in check your program with test constrains", bg="#d4c253")
tframe.pack(side=TOP, fill=BOTH, expand=True)
l.pack(side=TOP, fill=X, expand=True)
b.pack()
# ***********************************************************************************
frame2 = LabelFrame(root, text="VERIFICATION", bg="#f0f0f0")
b1 = Button(frame2, text="Proceed", command=new_window1,
            height=2, width=6, relief=RAISED)
l1 = Label(frame2, text="Requirement Check helps in identifying the compatability of your program terms", bg="#ccba4e")
frame2.pack(fill=BOTH, expand=True)
l1.pack(side=TOP, fill=X, expand=True)
b1.pack()
# ***********************************************************************************
frame3 = LabelFrame(root, text="NEW VALUES", bg="#e6e6e6")
b2 = Button(frame3, text="Insert", command=new_window2,
            height=2, width=6, relief=RAISED)
l2 = Label(
    frame3, text="Enter Values into Database to proceed further verification", bg="#c9b74f")
frame3.pack(side=BOTTOM, fill=BOTH, expand=True)
l2.pack(side=TOP, fill=X, expand=True)
b2.pack()
root.mainloop()
