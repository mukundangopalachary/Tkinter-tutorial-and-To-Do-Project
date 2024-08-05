import tkinter as tk

#Create the main window
app = tk.Tk()
app.title('Tkinter Tutorial')
app.geometry('900x900')

#MENU-BAR
menubar = tk.Menu(app)
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label="close", command= exit)
menubar.add_cascade(menu = filemenu, label= "File")
app.config(menu = menubar)
#Create a label
tk.Label(app, text='My First Tkinter UI', font = ("Times New Roman", 20)).pack(padx = 10, pady = 10) #For the Programmer's to write the text


#Create a text box
'''tk.Text(app, height = 1, width = 50, font=("Arial", 10)).pack(padx = 10, pady = 10) #For the User to write the text
Better to use Entry instead of Text for the User to write the text
'''

entry = tk.Entry(app, font=("Arial", 10))
entry.pack(padx = 10, pady = 10)


#grid
buttonframe = tk.Frame(app)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='Button 1', font=("Arial", 10), padx=10, pady=10) 
btn1.grid(row=0, column=0, sticky='ew')
btn2 = tk.Button(buttonframe, text='Button 2', font=("Arial", 10), padx=10, pady=10)
btn2.grid(row=0, column=1, sticky='ew')

buttonframe.pack(padx=10, pady=10)

#Place() for absolute positioning
anther_btn = tk.Button(app, text='Another Button', font=("Arial", 10), padx=10, pady=10)
anther_btn.place(relx = "0.99", rely = "00.99", anchor = "se")

#Quit App button
tk.Button(app, text='Quit',command = app.quit, height= 2, width= 7).pack(padx = 10, pady = 10)

#Run the main loop
app.mainloop()