import tkinter

root = tkinter.Tk()

root.title("hello world! :D")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="hewwo!", fg="pink")
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text="its me", fg="purple")
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(text="uwu", fg="blue")
my_label3.grid()

root.mainloop()