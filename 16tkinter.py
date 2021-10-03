from tkinter import*
root=Tk()
root.geometry("350x350")

X= StringVar(root,value="Enter a value")
entr=Entry(root,textvariable=X).pack()

root.mainloop()

