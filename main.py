import tkinter as tk
from tkinter import messagebox
from flashcards import flashcards_data  

class Base_GUI:
    def __init__(self):
        self.root = tk.Tk()
         #Main app screen
        #size and name
        self.root.geometry("800x400")
        self.root.title("Franklin Flash")
        self.root.config(bg= "tan", highlightbackground="red4", highlightcolor='red4')
        self.root.withdraw()

#starter screen
        self.splash_root = tk.Toplevel()
        self.splash_root.title('Franklin Flash starting screen')
        self.splash_root.label = tk.Label(self.splash_root, text="Welcome to the Franklin Flash! Where learning about computers gets better with computers!", font = ('Arial',18))
        self.splash_root.geometry("400x200")
        self.splash_root.config(bg= "tan", highlightbackground="red4", highlightcolor='red4')
        self.startbtn = tk.Button(self.splash_root, text= 'Get Started', font= ('Arial',18), command=self.handle_startclick)
        self.startbtn.config(bg= "red4", fg= "linen")
        self.startbtn.pack(fill='both')
        self.check_startrandomizerbutn = tk.BooleanVar()
        self.startrandomizerbtn = tk.Checkbutton(self.splash_root, text = "Randomize \n cards", variable=self.check_startrandomizerbutn, selectcolor='red')
        self.startrandomizerbtn.bind("<Button-1>", self.check_startrandomization)
        self.startrandomizerbtn.config(bg= "red4", fg= "linen")
        self.startrandomizerbtn.pack(fill='both')
       

        self.cards = flashcards_data
        self.card_place = 0
        self.current_card = self.cards[self.card_place]["question"]
        self.showing_question = True
        self.score = 0
        self.card_amount=0
      
        #button Checks
        self.check_startbutn =  tk.BooleanVar()
        self.check_scorebutn = tk.BooleanVar()
        self.check_yesbutn = tk.BooleanVar()
        self.check_nobutn = tk.BooleanVar()
        self.check_flipbutn = tk.BooleanVar()
        self.check_randomizerbutn = tk.BooleanVar()
        
        
        

        #texts within
        self.label = tk.Label(self.root,text = "Look at the card and mark yes if you know answer and no if you do not.\nCheck the boxes to show the score or randomize.Happy Learning!!\nPress the x in the corner when ready to leave.\n BEWARE: Randomizing to switch cards counts as shown cards against you.", font = ('Arial', 18))
        self.label.config(bg='tan')
        self.label.pack(padx=20, pady =20)

        self.textbox = tk.Text(self.root, height = 3, font = ('Arial', 16))
        self.textbox.insert("1.0", f"{self.current_card}")
        self.textbox.bind("<Key>", lambda e: "break")
        self.textbox.bind("<Button-1>", lambda e: self.textbox.focus_set())
        self.textbox.pack()

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.config(bg="linen")
        self.buttonframe.columnconfigure(0 , weight =1) 
        self.buttonframe.columnconfigure(1 , weight =1) 

        self.flipbutn = tk.Button(self.buttonframe, text="Flip", font = ('Arial', 18), command=self.handle_flipclick)
        self.flipbutn.config(bg= "red4" , fg= "linen")
        self.flipbutn.grid(row=0 ,column =0, sticky = tk.W + tk.E ,columnspan=2 , padx=10 ,pady=5)

        self.yesbutn = tk.Button(self.buttonframe, text="Yes", font = ('Arial', 18), command=self.handle_yesclick)
        self.yesbutn.config(bg= "red4", fg= "linen")
        self.yesbutn.grid(row=1 , column =0 ,sticky = tk.W + tk.E, padx=10 ,pady=5)

        self.nobutn = tk.Button(self.buttonframe, text="No", font = ('Arial', 18), command=self.handle_noclick)
        self.nobutn.config(bg= "red4", fg= "linen")
        self.nobutn.grid(row=1 , column =1, sticky= tk.W + tk.E, padx=10 ,pady=5)
        
        self.buttonframe.pack(fill = 'x')

#checkbox funtionality/buttons
        self.scorebtn = tk.Checkbutton(self.root, text = "Show Score!", variable=self.check_scorebutn, selectcolor='red')
        self.scorebtn.bind("<Button-1>", self.check_show_score)
        self.scorebtn.place(x=200 , y=300, heigh=100, width = 100)
        self.scorebtn.config(bg= "red4", fg= "linen")
        self.score_label = tk.Label(self.root, text = self.score , font=('Arial', 12))
        self.score_label.config(text=f'{self.score}/{self.card_amount}',bg= 'tan')
        
        self.randomizerbtn = tk.Checkbutton(self.root, text = "Randomize \n cards", variable=self.check_randomizerbutn, selectcolor='red')
        self.randomizerbtn.bind("<Button-1>", self.check_randomization)
        self.randomizerbtn.config(bg= "red4", fg= "linen")
        self.randomizerbtn.place(x=600 , y=300, heigh=100, width = 100)


        self.splash_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.splash_root.mainloop()
        self.root.mainloop()       
#Helper functions
    def update_textbox(self,text):
        self.textbox.delete('1.0', tk.END)
        self.textbox.insert('1.0', text)
        self.score_label.config(text=f'{self.score}/{self.card_amount}',bg= 'tan', fg= "linen")


#Checkbox functions
    def check_show_score(self, event=None):
        if self.check_scorebutn.get() == 0:
            self.score_label.place(x=350,y=375)
        elif self.check_scorebutn.get() == 1:
             self.score_label.place_forget()
             print(self.textbox.get('1.0', tk.END))
    
    def check_startrandomization(self, event=None):
        if  self.check_startrandomizerbutn.get() == 0:
            import random
            random.shuffle(self.cards)
            self.card_place = 0
            self.showing_question = True
            self.update_textbox(self.cards[self.card_place]["question"])
            self.check_randomizerbutn.set(1)
            
        
        else:
            self.card_place +=1
            if self.card_place >= len(self.cards):
                self.card_place = 0 
            self.showing_question = True
            self.update_textbox(self.cards[self.card_place]["question"])
            self.randomizerbtn.toggle()
            self.check_randomizerbutn.set(0)


    def check_randomization(self, event=None):
        if  self.check_randomizerbutn.get() == 0:
            import random
            random.shuffle(self.cards)
            self.card_place = 0
            self.showing_question = True
            self.card_amount +=1
            self.update_textbox(self.cards[self.card_place]["question"])
        
        else:
            self.card_place +=1
            if self.card_place >= len(self.cards):
                self.card_place = 0 
            self.showing_question = True
            self.card_amount +=1
            self.update_textbox(self.cards[self.card_place]["question"])

#click functionalities:        
    def handle_yesclick(self,event=None):
        if self.check_yesbutn.get() == 0: 
                self.score += 1
                self.score_label.config(text=self.score)
        self.card_place +=1
        if self.card_place >= len(self.cards):
             self.card_place = 0 
        self.showing_question = True
        self.card_amount +=1
        self.update_textbox(self.cards[self.card_place]["question"]) 

    def handle_noclick(self,event=None):
        self.card_place +=1
        if self.card_place >= len(self.cards):
            self.card_place = 0
        self.showing_question = True 
        self.card_amount +=1
        self.update_textbox(self.cards[self.card_place]["question"])
    
    def handle_startclick(self, event=None):
        self.splash_root.destroy()
        if self.check_startrandomizerbutn.get() == 1:
            self.check_randomizerbutn.set(1)
        else:
            self.check_randomizerbutn.set(0)
        self.root.deiconify()

    def handle_flipclick(self,event=None):
        if  self.showing_question:
            self.update_textbox(self.cards[self.card_place]["answer"])
            self.showing_question = False 

        else:
            self.update_textbox(self.cards[self.card_place]["question"])
            self.showing_question= True

    def on_closing(self):
        dialog = tk.Toplevel()
        dialog.title("Done Studying?")
        dialog.geometry("350x120")
        dialog.config(bg="tan")
        dialog.resizable(False, False)
    
    # Center on parent window
        try:
            if self.splash_root.winfo_exists() and self.splash_root.winfo_viewable():
                dialog.transient(self.splash_root)
            else:
                dialog.transient(self.root)
        except tk.TclError:
            dialog.transient(self.root)

        dialog.grab_set()
    
    # Message
        tk.Label(dialog, text="Franklin thinks you need to keep studying,\nare you sure?", 
             bg="tan", font=('Arial', 12)).pack(pady=15)
    
    # Buttons
        btn_frame = tk.Frame(dialog, bg="tan")
        btn_frame.pack()
    
        def close_app():
            dialog.destroy()  # Close dialog first
            self.root.destroy()
            self.splash_root.destroy()
    
        def cancel_close():
            dialog.destroy()  # Just close the dialog
    
        tk.Button(btn_frame, text="Yes", command=close_app, 
                  bg="red4", fg="linen", width=8).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="No", command=cancel_close, 
                  bg="red4", fg="linen", width=8).pack(side=tk.LEFT, padx=10)
    
Base_GUI()
