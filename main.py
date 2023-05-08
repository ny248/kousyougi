import tkinter as tk

size = 40
padding = 50
lines = 19

class board:
    def __init__(self, root):
        self.canvas =tk.Canvas(root, bg = "#eecc99")
        self.canvas.pack(fill = tk.BOTH, expand = True)
        for i in range(lines):
            self.canvas.create_line(padding + size * i, padding, padding + size * i, padding + size * (lines - 1), fill = "#000000", width = 1)
            self.canvas.create_line(padding, padding + size * i,  padding + size * (lines - 1), padding + size * i, fill = "#000000", width = 1)
        self.pieces = [[None for i in range(lines)] for j in range(lines)]
    def draw(self):
        for i in range(lines):
            for j in range(lines):
                if self.pieces[i][j] is None:
                    continue
                if not self.pieces[i][j].image_id is None:
                    self.canvas.delete(self.pieces[i][j].image_id)
                if not self.pieces[i][j].text_id is None:
                    self.canvas.delete(self.pieces[i][j].text_id)
                center = (padding + size * i, padding + size * j)
                color = "#000000" if self.pieces[i][j].owner == 1 else "#ffffff"
                self.pieces[i][j].image_id = self.canvas.create_oval(center[0] - size * 0.45, center[1] - size * 0.45, center[0] + size * 0.45, center[1] + size * 0.45, fill = color)
                if self.pieces[i][j].is_promoted:
                    name_color = "#ff0000"
                elif self.pieces[i][j].owner:
                    name_color = "#ffffff"
                else:
                    name_color = "#000000"
                ang = 180 * self.pieces[i][j].owner
                if len(self.pieces[i][j].name) == 1:
                    font_size = 20
                elif len(self.pieces[i][j].name) == 2:
                    font_size = 13
                else:
                    font_size = 9
                self.pieces[i][j].text_id = self.canvas.create_text(center[0], center[1], text = "\n".join(self.pieces[i][j].name), fill = name_color, angle = ang, font=("Times", font_size))


class piece:
    def __init__(self, name, position, board, owner):
        self.name = name
        self.position = position
        self.owner = owner
        self.is_promoted = 0
        self.image_id = None
        self.text_id = None
        board.pieces[position[0]][position[1]] = self
    



def place_pieces(board):
    piece("先鋒", (9, 12), board, 0)
    piece("仏狼機", (9, 16), board, 0)
    piece("鼓", (8, 17), board, 0)
    piece("中軍", (9, 17), board, 0)
    piece("旗", (10, 17), board, 0)
    piece("記室", (8, 18), board, 0)
    piece("将", (9, 18), board, 0)
    piece("参謀", (10, 18), board, 0)
    piece("神僧", (1, 18), board, 0)
    piece("高道", (17, 18), board, 0)
    for x in [0, 18]:
        piece("車総", (x, 13), board, 0)
        piece("騎総", (x, 15), board, 0)
        piece("後衛", (x, 17), board, 0)
        piece("前衛", (x, 18), board, 0)
    for x in [1, 17]:
        piece("百総", (x, 17), board, 0)
    for x in [2, 16]:
        piece("軍匠", (x, 18), board, 0)
    for x in [3, 15]:
        piece("把総", (x, 17), board, 0)
        piece("軍吏", (x, 18), board, 0)
    for x in [4, 14]:
        piece("舎餘", (x, 18), board, 0)
    for x in [5, 13]:
        piece("千総", (x, 17), board, 0)
        piece("舎人", (x, 18), board, 0)
    for x in [6, 12]:
        piece("力士", (x, 18), board, 0)
    for x in [7, 11]:
        piece("護兵", (x, 17), board, 0)
        piece("親兵", (x, 18), board, 0)
    for x in [1, 9, 17]:
        piece("牌総", (x, 13), board, 0)
        piece("歩総", (x, 14), board, 0)
    for x in range(2, 18, 2):
        piece("車", (x, 13), board, 0)
        piece("馬兵", (x, 15), board, 0)
    for x in range(3, 17, 2):
        if x != 9:
            piece("牌", (x, 13), board, 0)
            piece("歩兵", (x, 14), board, 0)
    for x in [0, 4, 8, 10, 14, 18]:
        piece("象", (x, 16), board, 0)
    for x in [1, 5, 13, 17]:
        piece("砲", (x, 16), board, 0)
    for x in [2, 6, 12, 16]:
        piece("弩", (x, 16), board, 0)
    for x in [3, 7, 11, 15]:
        piece("弓", (x, 16), board, 0)
    for i in range(lines):
        for j in range(lines):
            if not board.pieces[i][j] is None and board.pieces[i][j].owner == 0:
                name = board.pieces[i][j].name
                piece(name, (lines - 1 - i, lines - 1 - j), board, 1)
root = tk.Tk()
root.geometry('800x1000')
game_board = board(root)
place_pieces(game_board)
game_board.draw()
root.mainloop()