from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('mydbms')
cur=con.cursor()
p=Tk()
p.title('Edit Contact')
p.iconbitmap(default='edit.ico')        #for changing the icon in the titlebar
p.resizable(width='False',height='False')   #ti disablt the maximize button in titlebar
v=IntVar()          #for checkbutton

def clear():        #function to clear all the entries
    e1_fname.delete(0,END)
    e2_fname.delete(0,END)
    e1_lname.delete(0,END)
    e2_lname.delete(0,END)
    e1_phone.delete(0,END)
    e2_phone.delete(0,END)
    e1_address.delete(0,END)
    e2_address.delete(0,END)
    e1_dob.delete(0,END)
    e2_dob.delete(0,END)
    e1_note.delete(0,END)
    e2_note.delete(0,END)

def delete_one():           #function to delete single contact
    def go():
        if askquestion('Confirm?','Are you Sure to Delete This Contact?')=='yes':
            if a_fname.get()=='' or a_phone.get()=='':
                showerror('ERROR','Enter Details to delete the contact')
            else:
                cur.execute("delete from contact_db where fname='"+a_fname.get()+"' and phone1='"+a_phone.get()+"'")
                cur.execute("delete from contact_db where fname='"+a_fname.get()+"' and phone2='"+a_phone.get()+"'")
                cur.execute("delete from contact_db where fname='"+a_fname.get()+"' and phone3='"+a_phone.get()+"'")
                con.commit()
                showinfo('Success','Contact Deleted.')
                a_fname.delete(0,END)
                a_phone.delete(0,END)
                a.destroy() #windows destroys itself after function
    a=Tk()
    a.title('Delete')
    a.resizable(width='False',height='False')
    Label(a,text='First Name*',font='bold').grid(row=0,column=0)
    a_fname=Entry(a)
    a_fname.grid(row=0,column=1)
    Label(a,text='Phone*',font='bold').grid(row=1,column=0)
    a_phone=Entry(a)
    a_phone.grid(row=1,column=1)
    Button(a,text='Delete',font='bold',command=lambda:go()).grid(row=2,column=1,sticky=E+W+N+S)
        
def check_save():
    str1=str()
    if v.get()==0:
        str1='Male'
    elif v.get()==1:
        str1='Female'
            
    if e1_fname.get()=='' and e1_lname.get()=='':       #condition to check wheather user is making blank search request
        showerror('ERROR','Field marked with (*) cannot be Empty.')
        if e2_lname!='':
            cur.execute("update contact_db set fname='"+e2_fname.get()+"',lname='"+e2_lname.get()+"' where fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"'")
            cur.execute("update contact_db set lname='"+e2_lname.get()+"' where fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"'")
            cur.execute("update contact_db set address='"+e2_address.get()+"' where (fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"')")
            cur.execute("update contact_db set gender='"+str1+"' where (fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"')")
            cur.execute("update contact_db set dob='"+e2_dob.get()+"' where (fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"')")
            cur.execute("update contact_db set note='"+e2_note.get()+"' where (fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"')")  
            cur.execute("update contact_db set phone3='"+e2_phone.get()+"' where phone3='"+e1_phone.get()+"'")
            cur.execute("update contact_db set phone2='"+e2_phone.get()+"' where phone2='"+e1_phone.get()+"'")
            cur.execute("update contact_db set phone1='"+e2_phone.get()+"' where phone1='"+e1_phone.get()+"'")
            cur.execute("select * from contact_db where fname='"+e2_fname.get()+"' and lname='"+e2_lname.get()+"'")
            con.commit()        #to save changes
            clear() 
            r=cur.fetchone()
            showinfo('New Edited contact',r)
        else:
            cur.execute("update contact_db set fname='"+e2_fname.get()+"',lname='"+e2_lname.get()+"' where fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"'")
            cur.execute("update contact_db set address='"+e2_address.get()+"' where (fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"')")
            cur.execute("update contact_db set gender='"+str1+"' where (fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"')")
            cur.execute("update contact_db set dob='"+e2_dob.get()+"' where (fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"')")
            cur.execute("update contact_db set note='"+e2_note.get()+"' where (fname='"+e1_fname.get()+"' and lname='"+e1_lname.get()+"')")  
            cur.execute("update contact_db set phone3='"+e2_phone.get()+"' where phone3='"+e1_phone.get()+"'")
            cur.execute("update contact_db set phone2='"+e2_phone.get()+"' where phone2='"+e1_phone.get()+"'")
            cur.execute("update contact_db set phone1='"+e2_phone.get()+"' where phone1='"+e1_phone.get()+"'")
            cur.execute("select * from contact_db where fname='"+e2_fname.get()+"' and lname='"+e2_lname.get()+"'")
            con.commit()        #to save changes
            clear()
            r=cur.fetchone()
            showinfo('New Edited contact',r)

a=PhotoImage(file='edit_main.gif')
label = Label(image=a,bd=10,relief='ridge').grid(row=0,columnspan=4)

Label(p,text='First Name*:',font='bold').grid(row=1,column=0)
Label(p,text='From*:',font='bold').grid(row=2,column=0)
e1_fname=Entry(p)
e1_fname.grid(row=2,column=1)
Label(p,text='To:',font='bold').grid(row=2,column=2)
e2_fname=Entry(p)
e2_fname.grid(row=2,column=3)
    
Label(p,text='Last Name*:',font='bold').grid(row=3,column=0)
Label(p,text='From*:',font='bold').grid(row=4,column=0)
e1_lname=Entry(p)
e1_lname.grid(row=4,column=1)
Label(p,text='To:',font='bold').grid(row=4,column=2)
e2_lname=Entry(p)
e2_lname.grid(row=4,column=3)

Label(p,text='Phone:',font='bold').grid(row=5,column=0)
Label(p,text='From:',font='bold').grid(row=6,column=0)
e1_phone=Entry(p)
e1_phone.grid(row=6,column=1)
Label(p,text='To:',font='bold').grid(row=6,column=2)
e2_phone=Entry(p)
e2_phone.grid(row=6,column=3)

Label(p,text='Address:',font='bold').grid(row=7,column=0)
Label(p,text='From:',font='bold').grid(row=8,column=0)
e1_address=Entry(p)
e1_address.grid(row=8,column=1)
Label(p,text='To:',font='bold').grid(row=8,column=2)
e2_address=Entry(p)
e2_address.grid(row=8,column=3)

Label(p,text='Gender:',font='bold').grid(row=9,column=0)
Checkbutton(p,text='Male',font='bold',variable=v,onvalue=0).grid(row=10,column=0)
Checkbutton(p,text='Female',font='bold',variable=v,onvalue=1).grid(row=10,column=3)
    
Label(p,text='DoB(DD/MM/YY):',font='bold').grid(row=11,column=0)
Label(p,text='From:',font='bold').grid(row=12,column=0)
e1_dob=Entry(p)
e1_dob.grid(row=12,column=1)
Label(p,text='To:',font='bold').grid(row=12,column=2)
e2_dob=Entry(p)
e2_dob.grid(row=12,column=3)

Label(p,text='Note:',font='bold').grid(row=13,column=0)
Label(p,text='From:',font='bold').grid(row=14,column=0)
e1_note=Entry(p)
e1_note.grid(row=14,column=1)
Label(p,text='To:',font='bold').grid(row=14,column=2)
e2_note=Entry(p)
e2_note.grid(row=14,column=3)

'''photos above buttons'''

a1=PhotoImage(file='check_save2.gif')
label = Label(image=a1).grid(row=15,column=0)
Button(p,text='Check/Save',font='bold',command=lambda:check_save()).grid(row=16,column=0)
a2=PhotoImage(file='delete.gif')
label = Label(image=a2).grid(row=15,column=1)
Button(p,text='Delete',font='bold',command=lambda:delete_one()).grid(row=16,column=1)
a3=PhotoImage(file='clear.gif')
label = Label(image=a3).grid(row=15,column=2)
Button(p,text='Clear Fields',font='bold',command=lambda:clear()).grid(row=16,column=2)


Label(p,text='(Field marked with * cannot be empty)',font='Comic 7').grid(row=17,column=1)
p.mainloop()
