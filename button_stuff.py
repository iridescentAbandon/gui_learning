import tkinter

def print_uwu():
    print("uwu")

root = tkinter.Tk()

root.geometry("3000x1000")

button1 = tkinter.Button(root)
button1.config(text="owo!", command=print_uwu, fg='#ff3498', font=("times", "200"))
button1.grid()

root.mainloop()