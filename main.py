import tkinter as tk


class piece:
    pass

def create_board(root):
    size = 30
    padding = 50
    lines = 20
    board = tk.Canvas(root, bg = "#eecc99")
    board.pack(fill = tk.BOTH, expand = True)
    for i in range(lines):
        board.create_line(padding + size * i, padding, padding + size * i, padding + size * (lines - 1), fill = "#000000", width = 1)
        board.create_line(padding, padding + size * i,  padding + size * (lines - 1), padding + size * i, fill = "#000000", width = 1)
root = tk.Tk()
root.geometry('800x1000')
create_board(root)
root.mainloop()