import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="orange")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="white")
frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="green")
frame3.pack()

window.mainloop()
