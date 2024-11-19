from tkinter import Frame, Label

class Box2(Frame):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height, bg='lightgreen')
        self.pack_propagate(False)
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text="Box 2", bg='lightgreen')
        self.label.pack(expand=True)