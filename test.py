import tkinter as tk

window = tk.Tk()

'''label = tk.Label(
    foreground="white",
    background="black",
    width=10,
    height=10
)

entry = tk.Entry(fg="orange", bg="green", width=50)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow"
)'''


#label = tk.Label(text="Name:")
#entry = tk.Entry()

#name = entry.get()
#name


#label.pack()
#button.pack()
#entry.pack()

#frame = tk.Frame()
#frame.pack()

frameA = tk.Frame()
labelA = tk.Label(master=frameA, text="Text A")
labelA.pack()

frameB = tk.Frame()
labelB = tk.Label(master=frameB, text="Text B")
labelB.pack()

frameA.pack()
frameB.pack()

window.mainloop()