import tkinter as tk



def on_button_click():

    label.config(text="Hello, Tkinter!")



app = tk.Tk()

app.title("Tkinter Example")



button = tk.Button(app, text="Click Me!", command=on_button_click)

button.pack(pady=20)



label = tk.Label(app, text="Welcome to Tkinter!")

label.pack(pady=20)



app.mainloop()
