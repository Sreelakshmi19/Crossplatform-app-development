from tkinter import *
Screen1 = Tk()
Screen1.geometry('7500x7000')

Label1 = Label(Screen1, text = "HELLO WORLD", fg="#0939EB", bg="white", font=("Lato",50))
Label1.pack()

def function1():
    Label1 = Label(Screen1, text = "HELLO GUYS", fg="#0939EB", bg="white", font=("Lato",50))
    Label1.pack()
    
    

Button=Button(Screen1,text="On",command=function1,bg="red")
Button.pack()

Screen1.mainloop()

  

