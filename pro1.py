from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3


win = Tk()
win.geometry("500x570")
win.title("Geo Pin-Point")

#Title1
Information = Label(win, text="ENTER YOUR INFORMATION",font=("arial",18,"bold"))
Information.grid(row=0, columnspan=3, padx=80, pady=30)

#Name
Label1 = Label(win, text="Enter Location:", fg="black",font=("arial",14))
Label1.grid(row=1, column=0, padx=30, pady=10)
txtfield1 = Entry(win, width=25,background="Lightgrey", font=("Calibri",14))
txtfield1.grid(row=1, column=1, padx=5, pady=10)


# text
text1 = tk.Text(win, height=7, width=40, font=("Calibri",14),padx=5,)
text1.place(x=50,y=350)

#Title2
sentence = Label(win, text="VIEW YOUR INFORMATION", font=("arial",18,"bold")).place(x=90,y=310)

#MainFunc
def process():
    name= str(txtfield1.get())
    check=open('where.data', 'a')
    check.write(f"\n{name}")
    messagebox.showinfo("Info", "Place entered successfully")




#CheckFunc	 				
def checking():
    check= open('where.data','r')
    rest =check.read()
    import geoload
    for a in rest[::-1]:
        text1.insert(0.0,a)
	



def clear():
            print('Deleting Text..')


  
            # create connection to the 
            connection = sqlite3.connect('geodata.sqlite')
            
            # drop table
            connection.execute("DROP TABLE Locations")
            
            connection.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')
            
            # close the connection
            connection.close()

            f = open("where.data", "r+") 
            # absolute file positioning
            f.seek(0) 
            # to erase all data 
            f.truncate() 
            text1.delete(0.0, END)
            print("Data cleared successfully")

	 				
def ExitApp():
    msgbox = messagebox.askquestion('Exit','Do you want to quit the app',icon='warning')
    if msgbox=="yes":
        win.destroy()
    else:
        messagebox.showinfo('Return',' Return ')

	 				

#Buttons
submit=Button(win, text='Insert',width=25,bg='Grey',fg='black',command = process,font=("arial",14,"bold")).place(x=100,y=240)

check = Button(win, text="Check", command=checking, background="Grey", fg="black", font=("arial",14,"bold"))
check.place(x=250, y=520)

clear1 = Button(win, text="Clear", command=clear, background="Grey", fg="black", font=("arial",14,"bold"))
clear1.place(x=330, y=520)

button = Button(win, text="Exit",command=ExitApp, background="Red", fg="black", font=("arial",14,"bold"))
button.place(x=400, y=520)

win.mainloop()