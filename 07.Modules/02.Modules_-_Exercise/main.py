import tkinter as tk
from helpers import clear_screen


def render_main_screen(screen: tk.Tk):
    tk.Button(window, text="Login", background="green", foreground="white", command=lambda: print("Clicked")).grid(
        row=0, column=0)
    tk.Button(window, text="Register", background="black", foreground="yellow", command=lambda: print("Clicked")).grid(
        row=0, column=1)



if __name__ == "__main__":
    window = tk.Tk()
    window.title = "My App"
    window.geometry("600x600")


    render_main_screen(window)

    tk.Button(window, text="Clear screen", background="orange", foreground="black",
              command=lambda: clear_screen(window)).grid(row=1, column=1)

    window.mainloop()
