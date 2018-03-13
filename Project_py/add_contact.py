from Tkinter import *
from tkMessageBox import *
import sqlite3
import os
con=sqlite3.Connection('mydbms')
cur=con.cursor()
p=Tk()
p.title('Add contact')
p.iconbitmap(default='edit.ico')
p.resizable(width='False',height='False')
v=IntVar()          #FOR Check BUTTONS
temp_phone=[]       #TO SAVE THE PHONE NUMBERS

cur.execute('create table if not exists contact_db(fname varchar(10),lname varchar(10),phone1 number,phone2 number,phone3 number,address varchar(15),gender char(2),dob varchar(10),note varchar(20))')

'''====================CONTACT ADD AND SAVE FUNCTIONS AND THEIR SUBFUNCTIONS==============================='''

def initialize(a1,a2,a3,a4,a5,a6):      #function to delete all the entries
    a1.delete(0,END)
    a2.delete(0,END)
    a3.delete(0,END)
    a4.delete(0,END)
    a5.delete(0,END)
    a6.delete(0,END)
    Label(p,text='Phone:',font='bold').grid(row=4,column=0)
    while temp_phone!=[]:
        temp_phone.pop()
        
def add_field(x):           #stores more than one phone number
    global temp_phone
    if len(temp_phone)<3:
        if x.get().isalpha():
            showerror('ERROR','Invalid number!!')
        elif x.get()=='':
            showerror('ERROR','Number field is Empty!!')
        else:
            temp_phone.append(x.get())
            x.delete(0,END)
            Label(p,text='(Saved!)Phone',font='bold').grid(row=4,column=0)
    else:
        showinfo('Failed!','Cannot add more than 3 numbers.')
            
def add_clear():            #button function to clear entries
    if (askquestion('Confirm?','Are you sure want to discart changes?\nYou will lose the current data!'))=='yes':
        initialize(e_fname,e_lname,e_phone,e_address,e_dob,e_note)
    
def add_save():
    global temp_phone
    phone1=int()
    phone2=int()
    phone3=int()
    if e_fname.get().isdigit() or (e_fname.get()=='' and e_lname.get()==''):
        showerror('ERROR','Invalid Name!')
    elif e_phone.get().isalpha() or e_phone.get()=='':
        showerror('ERROR','Invalid Number!')
    else:
        gender=str()
        if len(temp_phone)==3:
            phone3=int(temp_phone.pop())
            phone2=int(temp_phone.pop())
            phone1=int(temp_phone.pop())
        elif len(temp_phone)==2:
            phone3=''
            phone2=int(temp_phone.pop())
            phone1=int(temp_phone.pop())
        elif len(temp_phone)==1:
            phone3=''
            phone2=''
            phone1=int(temp_phone.pop())
        elif len(temp_phone)==0:
            phone1=e_phone.get()
            phone2=''
            phone3=''
        if v.get()==0:
            gender='MALE'
        elif v.get()==1:
            gender='FEMALE'
        cur.execute('insert into contact_db values(?,?,?,?,?,?,?,?,?)',(e_fname.get(),e_lname.get(),phone1,phone2,phone3,e_address.get(),gender,e_dob.get(),e_note.get()))
        con.commit()
        showinfo('Success','Contact saved successfully')
        initialize(e_fname,e_lname,e_phone,e_address,e_dob,e_note)


a=PhotoImage(file='male.gif')
label = Label(image=a,bd=5,relief='ridge').grid(row=0,column=0)
b=PhotoImage(file='female.gif')
label2 = Label(image=b,bd=5,relief='ridge')
label2.grid(row=0,column=2)
Checkbutton(p,text='Male',font='bold',variable=v,onvalue=0).grid(row=1,column=0)
Checkbutton(p,text='Female',font='bold',variable=v,onvalue=1).grid(row=1,column=2)
Label(p,text='First Name*:',font='bold').grid(row=2,column=0)
e_fname=Entry(p)
e_fname.grid(row=2,column=1,columnspan=2)
Label(p,text='Last Name*:',font='bold').grid(row=3,column=0)
e_lname=Entry(p)
e_lname.grid(row=3,column=1,columnspan=2)
Label(p,text='Phone:',font='bold').grid(row=4,column=0)
e_phone=Entry(p)
e_phone.grid(row=4,column=1,columnspan=2)
Label(p,text='Address:',font='bold').grid(row=5,column=0)
e_address=Entry(p)
e_address.grid(row=5,column=1,columnspan=2)
    
Label(p,text='DoB(DD/MM/YY):',font='bold').grid(row=6,column=0)
e_dob=Entry(p)
e_dob.grid(row=6,column=1,columnspan=2)
Label(p,text='Note',font='bold').grid(row=7,column=0)
e_note=Entry(p)
e_note.grid(row=7,column=1,columnspan=2)

a1=PhotoImage(file='add_number.gif')
label = Label(image=a1).grid(row=8,column=0)
a2=PhotoImage(file='clear.gif')
label = Label(image=a2).grid(row=8,column=1)
a3=PhotoImage(file='save.gif')
label = Label(image=a3).grid(row=8,column=2)

Button(p,text='New Number',font='bold',command=lambda:add_field(e_phone)).grid(row=9,column=0)
Button(p,text='Clear',font='bold',command=lambda:add_clear()).grid(row=9,column=1)
Button(p,text='Save',font='bold',command=lambda:add_save()).grid(row=9,column=2)
Label(p,text='(Field with * are madatory)',font='Comic 7 bold').grid(row=10,column=1)    
p.mainloop()
