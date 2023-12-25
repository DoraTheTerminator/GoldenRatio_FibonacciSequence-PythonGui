import customtkinter
import tkinterDnD
import tkinter.messagebox

# customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("800x600")  # Adjusted the window size
app.title("Golden Ratio")

print(type(app), isinstance(app, tkinterDnD.Tk))


def is_valid_input(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False


def calc():
    input_value = entry_1.get()

    if not is_valid_input(input_value):
        tkinter.messagebox.showerror("Error", "Please enter a valid number.")
        return

    n = int(input_value)

    fiblist = [0, 1]
    for i in range(0, n):
        fiblist.append(fiblist[i] + fiblist[i + 1])

    output.set("\n".join(map(str, fiblist)))
    text_1.configure(state="normal")  # Enable writing to the textbox
    text_1.delete(1.0, "end")  # Clear existing content
    text_1.insert("insert", "Fibonacci Series: \n\n" + "\n".join(map(str, fiblist)))
    text_1.configure(state="disabled")  # Make the textbox read-only

    gratio = [fiblist[i] / float(fiblist[i - 1]) for i in range(2, len(fiblist))]
    output2.set("\n".join(map(str, gratio)))
    text_2.configure(state="normal")  # Enable writing to the textbox
    text_2.delete(1.0, "end")  # Clear existing content
    text_2.insert("insert", "Golden Ratio: \n\n" + "\n".join(map(str, gratio)))
    text_2.configure(state="disabled")  # Make the textbox read-only


def clear():
    entry_1.delete(0, 'end')
    text_1.configure(state="normal")
    text_1.delete(1.0, "end")
    text_1.configure(state="disabled")
    text_2.configure(state="normal")
    text_2.delete(1.0, "end")
    text_2.configure(state="disabled")


def button_callback():
    print("Button click", combobox_1.get())


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter Number of Iterations")
entry_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Calculate", command=calc)
button_1.pack(pady=10, padx=10)

button_clear = customtkinter.CTkButton(master=frame_1, text="Clear", command=clear)
button_clear.pack(pady=10, padx=10)

output = customtkinter.StringVar()  # Use standard tkinter StringVar
output2 = customtkinter.StringVar()  # Use standard tkinter StringVar

# Set the width and height of the textboxes
textbox_width = 500
textbox_height = 300

text_1 = customtkinter.CTkTextbox(master=frame_1, width=textbox_width, height=textbox_height)
text_1.pack(side="left", pady=10, padx=10)
text_1.insert("insert", "Fibonacci Series: \n\n")
text_1.configure(state="disabled")  # Make the textbox read-only

text_2 = customtkinter.CTkTextbox(master=frame_1, width=textbox_width, height=textbox_height)
text_2.pack(side="right", pady=10, padx=10)
text_2.insert("insert", "Golden Ratio: \n\n")
text_2.configure(state="disabled")  # Make the textbox read-only

app.mainloop()
