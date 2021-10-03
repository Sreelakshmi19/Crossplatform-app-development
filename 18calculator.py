from tkinter import*
from functools import partial

root=Tk()
root.geometry("350x350")

root.title("CALCULATOR")

def add(X,Y):
    A=X.get()
    B=Y.get()
    C=int(A)+int(B)
    print("Sum=",C)
    return
    

X=StringVar()
Y=StringVar()

    
label1=Label(root,text="Enter first no=").pack()
entry1=Entry(root,textvariable=X).pack()

label2=Label(root,text="Enter second no=").pack()
entry2=Entry(root,textvariable=Y).pack()

add=partial(add,X,Y)

bt1=Button(root,text="ADD",command=add).pack()

root.mainloop()
