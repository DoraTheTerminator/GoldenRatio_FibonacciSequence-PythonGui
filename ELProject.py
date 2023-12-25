import tkinter.messagebox
import customtkinter
import tkinter as tk


# ----- Tkinter Settings -----#
root = tk.Tk()
root.geometry("800x360")
root.configure(background="#3DC1AC")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.resizable(True, True)
tk.Wm.wm_title(root, "Fibonacci Sequence")
entr= tk.StringVar(root)
output = tk.StringVar(root)
inpt = tk.StringVar(root)
output2 = tk.StringVar(root)


def calc():
    n=int(inpt.get())

    fiblist = [0,1]
    for i in range(0, n):
        fiblist.append(fiblist[i]+fiblist[i+1])
        output.set(fiblist)

    gratio = [fiblist[i] / float(fiblist[i - 1]) for i in range(2, len(fiblist))]
    output2.set(gratio)

#----- Function that removes the content of the output and input -----#
def delete():
    output.set("")
    inpt.set("")


#----- Send Button -----#
tk.Button(
    root,
    text="RESULTS",
    font=("Courier", 20, "bold"),
    bg="#50C878",
    command=calc,
).place(x=410,y=100)

#----- Delete Button -----#
tk.Button(
    root,
    text="DELETE",
    font=("Courier", 20, "bold"),
    bg="#E41B17",
    command=delete,
).place(x=600,y=100)

#----- TEXT LABELS -----#
tk.Label(
    root,
    text="ITERATIONS: ",
    font=("Courier", 40, "bold"),
    bg="#3DC1AC",
).place(x=40,y=30)

tk.Label(
    root,
    text="RESULT: ",
    font=("Courier", 40, "bold"),
    bg="#3DC1AC",
).place(x=40,y=150)


#----- Information entry -----#
entr = tk.Entry(
    bg="#008B8B",
    font=("Courier", 30, "bold"),
    width=16,
    border=2,
    relief="solid",
    justify="center",
    textvariable=inpt,
).place(x=235,y=60,height=60)

#----- Information output -----#
out = tk.Label(
    bg="#99ff66",
    fg="Black",
    font=("Courier", 36, "bold"),
    textvariable=output,
    bd=2,
    relief="solid",
    width=24,
).place(x=40, y=230, height=70)

#----- Information output -----#
out = tk.Label(
    bg="#99ff66",
    fg="Black",
    font=("Courier", 36, "bold"),
    textvariable=output2,
    bd=2,
    relief="solid",
    width=24,
).place(x=40, y=390, height=70)


root.mainloop()