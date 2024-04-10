import tkinter as tk  # package import


root = tk.Tk()

root.geometry("800x500")  # the size
root.title("Compound Calculator")  # the name

label = tk.Label(root,text = "COMPOUND TO GET RICH",font = ("arial",18))  # the front character
label.pack(padx=20,pady=20)

textbox  = tk.Text(root,height =10, font=("arial",16)) # dark background size
textbox.pack(padx=10)

button = tk.Button(root,text = "Calculate Now",font  = ("arial",18))  # the button
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)  # do with 3 columns
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

# for multiple buttons, and frame

btn1 = tk.Button(buttonframe, text="1",font=("arial",18))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)  # row and column

btn2 = tk.Button(buttonframe, text="2",font=("arial",18))
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3",font=("arial",18))
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4",font=("arial",18))
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5",font=("arial",18))
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6",font=("arial",18))
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


root.mainloop()  # basic windows in python