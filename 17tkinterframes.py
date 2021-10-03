from tkinter import*
root=Tk()
root.geometry("350x350")


lf1=LabelFrame(root,text="Frame1").pack(expand="yes",fill="both")
lab1=Label(lf1,text="India is my country").pack()
bt1=Button(lf1,text="button1").pack()


lf2=LabelFrame(root,text="Frame2").pack(expand="yes",fill="both")
lab1=Label(lf2,text="India is my country").pack()
bt1=Button(lf1,text="button2").pack()


lf3=LabelFrame(root,text="Frame3").pack(expand="yes",fill="both")
lab1=Label(lf3,text="India is my country").pack()
bt1=Button(lf1,text="button3").pack()


root.mainloop()