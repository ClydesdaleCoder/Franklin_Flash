import tkinter as tk
from tkinter import messagebox

class Base_GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.score = 0
        self.check_scorebutn = tk.BooleanVar()
        self.check_yesbutn = tk.BooleanVar()
        self.check_nobutn = tk.BooleanVar()
        
        #size and name
        self.root.geometry("800x400")
        self.root.title("Franklin Flash")

        #texts within
        self.label = tk.Label(self.root,text = "Welcome to the Franklin Flash! Where learning about computers gets better with computer!", font = ('Arial', 18))

        self.label.pack(padx=20, pady =20)

        self.textbox = tk.Text(self.root, height = 3, font = ('Arial', 16))
        self.textbox.pack()

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0 , weight =1) 
        self.buttonframe.columnconfigure(1 , weight =1) 

        self.yesbutn = tk.Button(self.buttonframe, text="Yes", font = ('Arial', 18), command=self.handle_yesclick)
        self.yesbutn.grid(row=0 , column =0 ,sticky = tk.W + tk.E)


        self.nobutn = tk.Button(self.buttonframe, text="No", font = ('Arial', 18), command=self.check_nobutn)
        self.nobutn.bind("<Button-1>", self.check_show_score)
        self.nobutn.grid(row=0 , column =1, sticky= tk.W + tk.E)
        
        self.buttonframe.pack(fill = 'x')

#scoring funtionality/buttons
        self.scorebtn = tk.Checkbutton(self.root, text = "Show Score!", variable=self.check_scorebutn)
        self.scorebtn.bind("<Button-1>", self.check_show_score)
        self.scorebtn.place(x=350 , y=300, heigh=100, width = 100)
        
        self.score_label = tk.Label(self.root, text = self.score , font=('Arial', 12))
        self.score_label.config(text=self.score)
        
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def check_show_score(self, event=None):
        if self.check_scorebutn.get() == 0:
            self.score_label.place(x=350,y=375)
        elif self.check_scorebutn.get() == 1:
             self.score_label.place_forget()
             print(self.textbox.get('1.0', tk.END))

        
    def handle_yesclick(self,event=None):
        if self.check_yesbutn.get() == 0: 
                self.score += 1
                self.score_label.config(text=self.score)

    def handle_noclick(self,event=None):
         pass

    def on_closing(self):
        if messagebox.askyesno(title = "Done Studying?", message="Franklin thinks you need to keep studying, are you sure?" ):
             self.root.destroy()

        

Base_GUI()
