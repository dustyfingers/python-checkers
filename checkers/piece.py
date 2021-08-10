import pygame

from .constants import RED, WHITE, GREY, SQUARE_SIDE_LENGTH

class Piece:
    BORDER = 1

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        elif self.color == WHITE:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIDE_LENGTH * self.col + SQUARE_SIDE_LENGTH // 2
        self.y = SQUARE_SIDE_LENGTH * self.row + SQUARE_SIDE_LENGTH // 2
    
    def make_king(self):
        self.king = True

    def draw(self, window):
        RADIUS = (SQUARE_SIDE_LENGTH // 2) * 0.9
        pygame.draw.circle(window, GREY, (self.x, self.y, RADIUS + self.OUTLINE))
        pygame.draw.circle(window, self.color, (self.x, self.y, RADIUS))
     
    def __repr__(self):
        return str(self.color)


