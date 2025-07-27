import tkinter as tk
from tkinter import messagebox
from flashcards import flashcards_data  

class Base_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

        self.cards = flashcards_data
        self.card_place = 0
        self.current_card = self.cards[self.card_place]["question"]
        self.showing_question = True
        self.score = 0
        
        #button Checks
        self.check_startbutn =  tk.BooleanVar()
        self.check_scorebutn = tk.BooleanVar()
        self.check_yesbutn = tk.BooleanVar()
        self.check_nobutn = tk.BooleanVar()
        self.check_flipbutn = tk.BooleanVar()
        
        #starter screen
        self.splash_root = tk.Toplevel()
        self.splash_root.title('Franklin Flash starting screen')
        self.splash_root.label = tk.Label(self.splash_root, text="Welcome to the Franklin Flash! Where learning about computers gets better with computers!", font = ('Arial',18))
        self.splash_root.geometry("800x400")
        self.startbtn = tk.Button(self.splash_root, text= 'Get Started', font= ('Arial',18), command=self.handle_startclick)
        self.startbtn.place(x=400 , y=200, height=100, width = 100)
        
        #Main app screen
        #size and name
        self.root.geometry("800x400")
        self.root.title("Franklin Flash")

        #texts within
        self.label = tk.Label(self.root,text = "Look at the the card and mark yes if you know answer and no if you do not.", font = ('Arial', 18))

        self.label.pack(padx=20, pady =20)

        self.textbox = tk.Text(self.root, height = 3, font = ('Arial', 16))
        self.textbox.insert("1.0", f"{self.current_card} ")
        self.textbox.pack()

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0 , weight =1) 
        self.buttonframe.columnconfigure(1 , weight =1) 

        self.flipbutn = tk.Button(self.buttonframe, text="Flip", font = ('Arial', 18), command=self.handle_flipclick)
        self.flipbutn.grid(row=0 ,column =0,sticky = tk.W + tk.E)

        self.flipbutn = tk.Button(self.buttonframe, text="Flip", font = ('Arial', 18), command=self.handle_flipclick)
        self.flipbutn.grid(row=0 ,column =0,sticky = tk.W + tk.E)

        self.yesbutn = tk.Button(self.buttonframe, text="Yes", font = ('Arial', 18), command=self.handle_yesclick)
        self.yesbutn.grid(row=1 , column =0 ,sticky = tk.W + tk.E)

        self.nobutn = tk.Button(self.buttonframe, text="No", font = ('Arial', 18), command=self.handle_noclick)
        self.nobutn.grid(row=1 , column =1, sticky= tk.W + tk.E)
        
        self.buttonframe.pack(fill = 'x')

#scoring funtionality/buttons
        self.scorebtn = tk.Checkbutton(self.root, text = "Show Score!", variable=self.check_scorebutn)
        self.scorebtn.bind("<Button-1>", self.check_show_score)
        self.scorebtn.place(x=350 , y=300, heigh=100, width = 100)
        
        self.score_label = tk.Label(self.root, text = self.score , font=('Arial', 12))
        self.score_label.config(text=self.score)
        

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.splash_root.mainloop()
        self.root.mainloop()       

    def check_show_score(self, event=None):
        if self.check_scorebutn.get() == 0:
            self.score_label.place(x=350,y=375)
        elif self.check_scorebutn.get() == 1:
             self.score_label.place_forget()
             print(self.textbox.get('1.0', tk.END))

#click functionalities:        
    def handle_yesclick(self,event=None):
        if self.check_yesbutn.get() == 0: 
                self.score += 1
                self.score_label.config(text=self.score)
        self.card_place +=1
        if self.card_place >= len(self.cards):
             self.card_place = 0 
        self.showing_question = True
        self.textbox.delete('1.0', tk.END)  
        self.textbox.insert('1.0', self.cards[self.card_place]["question"]) 

    def handle_noclick(self,event=None):
        self.card_place +=1
        if self.card_place >= len(self.cards):
            self.card_place = 0
        self.showing_question = True 
        self.textbox.delete('1.0', tk.END)  
        self.textbox.insert('1.0', self.cards[self.card_place]["question"]) 
    
    def handle_startclick(self, event=None):
         self.splash_root.destroy()
         self.root.deiconify()

    def handle_flipclick(self,event=None):
        if  self.showing_question:
            self.textbox.delete('1.0', tk.END)  
            self.textbox.insert('1.0', self.cards[self.card_place]["answer"])
            self.showing_question = False 

        else:
            self.textbox.delete('1.0', tk.END)  
            self.textbox.insert('1.0', self.cards[self.card_place]["question"]) 
            self.showing_question= True

    def on_closing(self):
        if messagebox.askyesno(title = "Done Studying?", message="Franklin thinks you need to keep studying, are you sure?" ):
             self.root.destroy()

        

Base_GUI()
