import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('500x300')
l = tk.Label(window,text='welcome to tkinter',bg='green',fg='white',font = ('Arial',12),width=30,height=2)
l.pack()
window.mainloop()