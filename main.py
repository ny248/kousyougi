import tkinter as tk

size = 40
padding = 50
lines = 20

class piece:
    def __init__(self, name, position, board, owner):
        self.name = name
        self.position = position
        self.owner = owner
        self.is_promoted = 0
        self.image_id = None
        self.place(board, position)
    def place(self, board, position):
        if not self.image_id is None:
            board.delete(self.image_id)
        center = (padding + size * position[0], padding + size * position[1])
        color = "#000000" if self.owner == 1 else "#ffffff"
        self.image_id = board.create_oval(center[0] - size * 0.45, center[1] - size * 0.45, center[0] + size * 0.45, center[1] + size * 0.45, fill = color)
        if self.is_promoted:
            name_color = "#ff0000"
        elif self.owner:
            name_color = "#ffffff"
        else:
            name_color = "#000000"
        ang = 180 * self.owner
        board.create_text(center[0], center[1], text = "\n".join(self.name), fill = name_color, angle = ang)

def create_board(root):
    board = tk.Canvas(root, bg = "#eecc99")
    board.pack(fill = tk.BOTH, expand = True)
    for i in range(lines):
        board.create_line(padding + size * i, padding, padding + size * i, padding + size * (lines - 1), fill = "#000000", width = 1)
        board.create_line(padding, padding + size * i,  padding + size * (lines - 1), padding + size * i, fill = "#000000", width = 1)
    return board
root = tk.Tk()
root.geometry('800x1000')
board = create_board(root)
A = piece("天狗", (1, 3), board, 1)
root.mainloop()