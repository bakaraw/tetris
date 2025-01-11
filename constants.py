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
    O_PIECE = 6

T_PIECE_COLOR = (233, 5, 233)
I_PIECE_COLOR = (4, 233, 233)
S_PIECE_COLOR = (4, 233, 6)
Z_PIECE_COLOR = (232, 5, 4)
L_PIECE_COLOR = (233, 153, 4)
J_PIECE_COLOR = (5, 5, 233)
O_PIECE_COLOR = (233, 233, 4)

ROTATION_OFFSETS = {
    PieceType.I_PIECE.value: [
        [(1, -2), (0, -1), (-1, 0), (-2, 1)],  # 0 degrees
        [(-1, 1), (0, 0), (1, -1), (2, -2)],  # 90 degrees
        [(2, -1), (1, 0), (0, 1), (-1, 2)],  # 180 degrees
        [(-2, 2), (-1, 1), (0, 0), (1, -1)]  # 270 degrees
    ],
    PieceType.J_PIECE.value: [
        [(-2, 0), (-1, 1), (0, 0), (1, -1)],
        [(0, -2), (-1, -1), (0, 0), (1, 1)],
        [(2, 0), (1, -1), (0, 0), (-1, 1)],
        [(0, 2), (1, 1), (0, 0), (-1, -1)]
    ],
    PieceType.L_PIECE.value: [
        [(1, -1), (0, 0), (-1, 1), (0, 2)],
        [(1, 1), (0, 0), (-1, -1), (-2, 0)],
        [(-1, 1), (0, 0), (1, -1), (0, -2)],
        [(-1, -1), (0, 0), (1, 1), (2, 0)]
    ]
}
