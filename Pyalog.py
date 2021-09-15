import tkinter


class Pyalog:
    """
    Dialog class to use the tkinter systems
    """
    def __init__(self):
        self.window = tkinter.Tk()
        greeting = tkinter.Label(text="Hello, Tkinter")
        greeting.pack()
        window.mainloop()