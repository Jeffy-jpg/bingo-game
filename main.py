import customtkinter as ctk
import tkinter as tk
import random
from tkinter import messagebox 


class App (ctk.CTk):
    def __init__(self):
        super().__init__()

        #Window Appearance
        self.title("Bingo!")
        self.geometry("450x200")
        self.resizable(True, True)
        self._set_appearance_mode("light")


        #Widgets
        self.num_frame = ctk.CTkFrame(self, fg_color="white", corner_radius= 0)
        self.num_frame.pack(padx=20, pady=20, fill = "both", expand = True,
                             side ="left")

        self.list_frame = ctk.CTkFrame(self, fg_color="white", corner_radius= 0)
        self.list_frame.pack(padx=(0, 20), pady = 20, fill = "both", expand = True,
                            side = "right")

        self.columns = []

        #Outloop makes the 5 list boxes
        for i in range(5):
            self.listbox = tk.Listbox(self.num_frame, selectmode= "multiple", selectforeground= "white",
                                       height=5, width=5, exportselection= False, bg="white", fg= "black",
                                        font=('Arial', 16), justify= "center")
            self.listbox.pack(side="left", fill= "both", expand=True, padx=2)
            self.columns.append(self.listbox) 
            self.listbox.bind("<<ListboxSelect>>", self.check_bingo)

            #Add rand numbers for the inner loop
            for j in range(5):
                self.listbox.insert("end", random.randint(0, 100))

        self.bingo_frame = ctk.CTkFrame(self.list_frame, fg_color="transparent")
        self.bingo_frame.pack(side = "top", fill = "x", expand = False)

        self.history_frame= ctk.CTkFrame(self.list_frame, fg_color="transparent")
        self.history_frame.pack(side="bottom", fill = "both", expand = True)

        self.bingo = ctk.CTkLabel(self.bingo_frame, text="##", fg_color="green", corner_radius= 8,
                                  font=("arial", 16))
        self.bingo.pack(pady = 5, padx = 5, fill = "both", expand = True)

        self.history_list = tk.Listbox(self.history_frame,
                                       selectforeground="white",
                                       height= 5, width= 5, exportselection= False, bg = "#2b6cb0", fg="black",
                                       font=('arial', 16), justify= "center")
        self.history_list.pack(pady =5, padx = 5, fill = "both", expand = True, side="left")
        self.list_scrollbar = ctk.CTkScrollbar(self.history_frame, command=self.history_list.yview)
        self.list_scrollbar.pack(side="right", fill="y")
        self.history_list.configure(yscrollcommand = self.list_scrollbar.set)

        self.bingo_timer()


    def bingo_timer(self): # chooses bingo number and updates list frame accordingly
        self.ran_num = random.randint(0, 100)
        self.bingo.configure(text = self.ran_num)
        self.history_list.insert("end", self.ran_num, )
        self.timer_id = self.after(10000, self.bingo_timer)
        self.check_bingo(None)

    def check_bingo(self, event):
        won = False
        called_numbers = self.history_list.get(0, "end")

        def is_valid(col_idex, row_index):
            listbox = self.columns[col_idex]
            is_selected = row_index in listbox.curselection()
            number_val = listbox.get(row_index)
            return is_selected and (number_val in called_numbers)
    
        #check horizontal and vertical
        for i in range (5):
            if all(is_valid(i, row) for row in range(5)):
                won = True
            if all (is_valid(col, i) for col in range(5)):
                won = True

        #check diagonal
        if all(is_valid(i, i) for i in range(5)):
            won = True
        if all(is_valid(i, 4-i) for i in range(5)):
            won = True


        if won == True:
            messagebox.showinfo("Message", "BINGO! You Have Won!")

            for listbox in self.columns:
                listbox.delete(0, "end")
                for j in range(5):
                    listbox.insert("end", random.randint(0,100))

            self.history_list.delete(0, "end")
            self.after_cancel(self.timer_id)
            self.bingo_timer

      
app = App()
app.mainloop()

