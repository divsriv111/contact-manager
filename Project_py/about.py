from Tkinter import *
p=Tk()
p.iconbitmap(default='about.ico')
p.title("About Software..")
a=PhotoImage(file='contacts_logo.gif')
label = Label(image=a).pack()
Label(p,text='Contact Manager v1.0.',font='Comic 20 bold underline',fg='Red').pack()
Label(p,text='Developed in Python\nMade By- Divyanshu Ranjan Srivastava\n151457 CSE',font='Arial 15 bold').pack()
Label(p,text='Contact- greatdrs@gmail.com, +91-7247368486',font='Arial 15 bold').pack()
Label(p,text='Jaypee University of Engineering And Technology Guna, M.P',font='Arial 15 bold').pack()
p.mainloop()
