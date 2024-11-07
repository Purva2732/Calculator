import tkinter as tk

# Function to update the display
def click(event):
    global expression
    expression += str(event.widget.cget("text"))
    equation.set(expression)

# Function to evaluate the final expression
def equal():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("error")
        expression = ""

# Function to clear the display
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window setup
window = tk.Tk()
window.title("Calculator")
window.geometry("400x400")
window.configure(bg="#17161b")

# Global variables
expression = ""
equation = tk.StringVar()

# Display result
result = tk.Label(window, width=55, height=2, textvariable=equation, bg="white")
result.pack()

# Creating buttons and attaching commands
tk.Button(window, text="C", width=10, height=1, fg="#fff", bg="#3697f5", command=clear).place(x=10, y=100)
tk.Button(window, text="%", width=10, height=1, fg="#fff", bg="grey").place(x=100, y=100)
tk.Button(window, text="/", width=10, height=1, fg="#fff", bg="grey").place(x=190, y=100)
tk.Button(window, text="*", width=10, height=1, fg="#fff", bg="grey").place(x=280, y=100)

tk.Button(window, text="1", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=10, y=150)
tk.Button(window, text="2", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=100, y=150)
tk.Button(window, text="3", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=190, y=150)
tk.Button(window, text="+", width=10, height=2, fg="#fff", bg="grey").place(x=280, y=150)

tk.Button(window, text="4", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=10, y=200)
tk.Button(window, text="5", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=100, y=200)
tk.Button(window, text="6", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=190, y=200)
tk.Button(window, text="-", width=10, height=2, fg="#fff", bg="grey").place(x=280, y=200)

tk.Button(window, text="7", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=10, y=250)
tk.Button(window, text="8", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=100, y=250)
tk.Button(window, text="9", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=190, y=250)
tk.Button(window, text="+", width=10, height=2, fg="#fff", bg="grey").place(x=280, y=250)

tk.Button(window, text="0", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=10, y=300)
tk.Button(window, text=".", width=10, height=2, fg="#fff", bg="#2a2d36").place(x=100, y=300)
tk.Button(window, text="=", width=10, height=2, fg="#fff", bg="grey", command=equal).place(x=190, y=300)

# Bind click event to buttons that don't have a command
for widget in window.winfo_children():
    if isinstance(widget, tk.Button) and not widget.cget('command'):
        widget.bind("<Button-1>", click)

window.mainloop()
