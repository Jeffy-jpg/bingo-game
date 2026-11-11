import customtkinter as ctk
import tkinter as tk
import random

class App (ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bingo!")
        self.geometry("400x200")
        self.resizable(True, True)
        self._set_appearance_mode("light")

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

            #Add rand numbers for the inner loop
            for j in range(5):
                ran_num = random.randint(0,100)
                self.listbox.insert("end", ran_num)

        self.bingo_frame = ctk.CTkFrame(self.list_frame, fg_color="green")
        self.bingo_frame.pack(side = "top", fill = "x", expand = False)

        self.history_frame= ctk.CTkFrame(self.list_frame, fg_color="#2b6cb0")
        self.history_frame.pack(side="bottom", fill = "both", expand = True)

        self.bingo = ctk.CTkLabel(self.bingo_frame, text="00", fg_color="green",
                                  font=("arial", 16))
        self.bingo.pack(pady = 5, padx = 5, fill = "both", expand = True)

        self.history_list = tk.Listbox(self.history_frame,
                                       selectmode="multiple", selectforeground="white",
                                       height= 5, width= 5, exportselection= False, bg = "white", fg="black",
                                       font=('arial', 16), justify= "center")
           
app = App()
app.mainloop()

