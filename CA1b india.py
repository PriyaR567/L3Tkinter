import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, height=50, bg="orange")
frame1.pack(fill=tk.BOTH)

frame2 = tk.Frame(master=window, height=50, bg="white")
frame2.pack(fill=tk.BOTH)

frame3 = tk.Frame(master=window, height=50, bg="green")
frame3.pack(fill=tk.BOTH)

window.mainloop()