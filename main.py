import customtkinter as ctk

class App (ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bing go!")
        self.geometry("350x350")
        self.resizable(False, False)

app = App()
app.mainloop()

