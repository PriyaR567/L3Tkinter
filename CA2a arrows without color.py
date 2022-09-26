import tkinter as tk
from turtle import bgcolor

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

button1 = tk.Button(text="Top")
button1.place(x=60, y=0)

button2 = tk.Button(text="Bottom")
button2.place(x=52, y=120)

button2 = tk.Button(text="Left")
button2.place(x=0, y=60)

button2 = tk.Button(text="Right")
button2.place(x=110, y=60)

window.mainloop()