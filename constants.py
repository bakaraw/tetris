from enum import Enum

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 900
UNIT = 40
ROWS = 20
COLS = 10
FPS = 60

GRID_COLOR = (200, 200, 200)
BOARD_COLOR = (100, 100, 100)
BG_COLOR = (33, 33, 33)

class PieceType(Enum):
    T_PIECE = 0
    I_PIECE = 1
    S_PIECE = 2
    Z_PIECE = 3
    L_PIECE = 4
    J_PIECE = 5

T_PIECE_COLOR = (137, 52, 136)
