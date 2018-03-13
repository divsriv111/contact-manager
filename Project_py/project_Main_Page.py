from Tkinter import *                                       #for GUI
from tkMessageBox import *                                  #for dialogboxes
import sqlite3 #for database
import os   #for system commands
con=sqlite3.Connection('mydbms')
cur=con.cursor()
root=Tk()       #main window
root.title('Contact Manager')

def add_contact():              #function for adding contact
    osCommandString = "add_contact.py"              #system command for opoening the another python file persent in the folder
    os.system(osCommandString)

def view_contact():         #function for viewing contact
    osCommandString = "view_contact.py"
    os.system(osCommandString)

def edit_contact():         #function for editing contact
    osCommandString = "edit_contact.py"
    os.system(osCommandString)

def delete_contact():           #function for deleting contact
    if askquestion('Confirm?','Are to sure you want to delete all the contacts? This cannot be undone!')=='yes':
        cur.execute('drop table contact_db')
        con.commit()

def ask_quit():             #function for exit
    if askokcancel("Quit", "You want to quit now?"):
        con.close()
        root.destroy()
def show_about():           #function for showing information
    osCommandString = "about.py"
    os.system(osCommandString)
    
osCommandString = "notepad.exe ReadMe.txt"      #system command for opoening the notepad 'readme' file persent in the folder
os.system(osCommandString)
root.iconbitmap(default='main.ico') #changes the title icon
root.resizable(width='False',height='False')    #disables maximize button in titlebar, as i have used grid so maximizing is of no use
a=PhotoImage(file='welcome2.gif')
label = Label(image=a,bd=10,relief='ridge').grid(row=0,column=0)
Button(root,text=' Click here to Add Contact',width=25,height=2,font='Harrington 15 bold',bd=5,bg='Green',command=lambda:add_contact()).grid(row=2,sticky=E+W+S+N)
Button(root,text='Click here to View Contacts',width=25,height=2,font='Harrington 15 bold',bd=5,bg='yellow',command=lambda:view_contact()).grid(row=3,sticky=E+W+S+N)
Button(root,text='Click here to Edit Contact',width=25,height=2,font='Harrington 15 bold',bd=5,bg='purple',command=lambda:edit_contact()).grid(row=4,sticky=E+W+S+N)
Button(root,text='Click here to Delete All Contact',width=25,height=2,font='Harrington 15 bold',bd=5,bg='red',command=lambda:delete_contact()).grid(row=5,sticky=E+W+S+N)
Button(root,text='Click here to Exit',font='Harrington 15 bold',width=25,height=2,bd=5,bg='light blue',command=lambda:ask_quit()).grid(row=6,sticky=E+W+S+N)
Label(root,text='@made by-151457',font='Comic 7').grid(row=7)
Button(root,text='About',font='Comic 7',command=lambda:show_about()).grid(row=7,sticky=E)
root.mainloop()
