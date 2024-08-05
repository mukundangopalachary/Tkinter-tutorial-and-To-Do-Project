import tkinter as tk
from tkinter import messagebox
class GUI:
    
    def __init__(self):
        # Main Frame Setup
        self.root = tk.Tk()
        self.root.title("To Do")
        self.root.geometry("500x500")
        self.root.configure(bg = "light blue")
        
        self.label = tk.Label(self.root, text = "To Do List", font = ("Arial", 26), bg='light blue', fg='Black')
        self.label.pack(padx = 100, pady = 10)
        
        # Entry Frame
        self.entry_frame = tk.Frame(self.root, bg='light blue')
        self.entry_frame.pack(side=tk.BOTTOM, pady=10)
        
        self.textbox = tk.Entry(self.entry_frame, font = ("Arial", 14))
        self.textbox.bind("<Return>",self.shortcut)
        self.textbox.pack(side=tk.LEFT, padx=10)
        
        self.button = tk.Button(self.entry_frame, text = "Enter", font = ("Arial", 14), command = self.entry)
        self.button.pack(side=tk.LEFT)
        
        self.list_frame = tk.Frame(self.root, bg='light blue')
        self.list_frame.pack(pady=10, anchor='w')
        
        # Dictionary to keep track of row
        self.row_index = 0
        
        self.root.protocol("WM_DELETE_WINDOW",self.on_closing)
        
        self.root.mainloop()
        
    def entry(self):
        task = self.textbox.get()
        
        if task:
            self.var = tk.IntVar()
            self.checkbox = tk.Checkbutton(self.list_frame, text = task, font = ("Arial", 20), bg = "light blue", fg = "Black", variable = self.var)   
            self.checkbox.grid(row=self.row_index, column=0, sticky='w', pady=2)
            self.row_index += 1
            self.textbox.delete(0, tk.END)
        
    def shortcut(self, event):
        self.entry()
        
    def on_closing(self):
        message = messagebox.askquestion(title="Exit", message= "Do you want to leave this Application?")
        if message == "yes":
            self.root.quit()
    
if __name__ == '__main__':
    UI = GUI()
