import tkinter as tk
from tkinter import messagebox
import sqlite3

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "light blue")
        canvas = tk.Canvas(self, bg = "light blue")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg = 'light blue')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


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
        
        self.button = tk.Button(self.entry_frame, text = "Enter", font = ("Arial", 14), command = self.add_task)
        self.button.pack(side=tk.LEFT)
        
        self.list_frame = tk.Frame(self.root, bg='light blue')
        self.list_frame.pack(pady=10, anchor='w')
        
        self.scrollable_frame = ScrollableFrame(self.root, bg='light blue')
        self.scrollable_frame.pack(fill="both", expand=True)
        
        # Dictionary to keep track of row
        self.row_index = 0
        
        self.root.protocol("WM_DELETE_WINDOW",self.on_closing)
        
        self.root.mainloop()
        
        #DataBase
        
        self.conn = sqlite3.connect("tasks.db")
        self.create_table()
        self.load_tasks()
        
    

    # For Adding table  
    def add_task(self):
        task = self.textbox.get()
        if task:
            self.var = tk.IntVar()
            self.checkbox = tk.Checkbutton(self.scrollable_frame.scrollable_frame, text=task, font=("Arial", 20), bg="light blue", fg="Black", variable=self.var)
            self.checkbox.grid(row=self.row_index, column=0, sticky='w', pady=2)
            self.row_index += 1
            self.textbox.delete(0, tk.END)
            self.save_task(task)
            
    
    #For pressing "Enter" Key    
    def shortcut(self, event):
        self.add_task()
        
    #On pressing X button on top right corner
    def on_closing(self):
        message = messagebox.askquestion(title="Exit", message= "Do you want to leave this Application?")
        if message == "yes":
            self.root.quit()
            
    #Create Table
    def create_table(self):
        with self.conn:
            self.conn.execute("""
                              CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL)""")
    
    #SAVE TASK IN THE TABLE
    def save_task(self,task):
        with self.conn:
            self.conn.execute("""INSERT INTO tasks (task) VALUES (?)""", (task,))
            
    #Loading The tasks when Closed
    def load_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT task FROM tasks")
        tasks = cursor.fetchall()
        for task in tasks:
            self.var = tk.IntVar()
            self.checkbox = tk.Checkbutton(self.scrollable_frame.scrollable_frame, text=task[0], font=("Arial", 20), bg="light blue", fg="Black", variable=self.var)
            self.checkbox.grid(row=self.row_index, column=0, sticky='w', pady=2)
            self.row_index += 1
if __name__ == '__main__':
    UI = GUI()
