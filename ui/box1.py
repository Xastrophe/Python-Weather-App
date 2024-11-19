from tkinter import Frame, Label, Canvas

class Box1(Frame):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height, bg='lightblue', bd=2, relief='solid')
        self.pack_propagate(False)
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self, width=180, height=100, bg='white')
        self.canvas.create_rectangle(10, 10, 170, 90, outline='black', fill='yellow')