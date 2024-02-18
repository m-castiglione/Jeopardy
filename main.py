import tkinter as tk

window = tk.Tk()

for i in range(6):
    for x in range(5):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=x)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {x}")
        label.pack()
        
window.mainloop()