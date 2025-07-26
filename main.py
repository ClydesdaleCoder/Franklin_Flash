import tkinter as tk
from tkinter import ttk

class Base_GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("800x400")
        self.root.title("Franklin Flash")

        self.label = tk.Label(self.root,text = "Welcome to the Franklin Flash! Where learning about computers gets better with computer!", font = ('Arial', 18))

        self.label.pack(padx=20, pady =20)

        self.textbox = tk.Text(self.root, height = 3, font = ('Arial', 16))
        self.textbox.pack()

        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(0 , weight =1) 
        buttonframe.columnconfigure(1 , weight =1) 

        btn1 = tk.Button(buttonframe, text="Yes", font = ('Arial', 18))
        btn1.grid(row=0 , column =0 ,sticky = tk.W + tk.E)


        btn2 = tk.Button(buttonframe, text="No", font = ('Arial', 18))
        btn2.grid(row=0 , column =1, sticky= tk.W + tk.E)
        
        buttonframe.pack(fill = 'x')

        scorebtn = tk.Button(self.root, text = "Show Score!")
        scorebtn.place(x=350 , y=300, heigh=100, width = 100)
        
        self.score = 0
        
        self.root.mainloop()

    def modify_score():
        if btn1.checkbutton == 1: 
            self.score += 1
    



Base_GUI()
