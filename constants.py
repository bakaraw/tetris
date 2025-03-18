from enum import Enum, pickle_by_global_name

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 900
UNIT = 35
ROWS = 20
COLS = 10
FPS = 60

GRID_COLOR = (200, 200, 200)
BOARD_COLOR = (100, 100, 100)
BG_COLOR = (33, 33, 33)

SHADOW_COLOR = (255, 255, 255, 30)
STROKE_WIDTH = 2


class PieceType(Enum):
    T_PIECE = 0
    I_PIECE = 1
    S_PIECE = 2
    Z_PIECE = 3
    L_PIECE = 4
    J_PIECE = 5
    O_PIECE = 6


PIECE_COLORS = {
    PieceType.T_PIECE.value: (233, 5, 233),
    PieceType.I_PIECE.value: (4, 233, 233),
    PieceType.S_PIECE.value: (4, 233, 6),
    PieceType.Z_PIECE.value: (232, 5, 4),
    PieceType.L_PIECE.value: (233, 154, 4),
    PieceType.J_PIECE.value: (5, 5, 233),
    PieceType.O_PIECE.value: (233, 233, 4)
}

BLOCKS_INITAL_POSITION = {
    PieceType.T_PIECE.value: [(0, 1), (1, 1), (2, 1), (1, 0)],
    PieceType.L_PIECE.value: [(0, 0), (0, 1), (1, 1), (2, 1)],
    PieceType.I_PIECE.value: [(0, 0), (1, 0), (2, 0), (3, 0)],
    PieceType.S_PIECE.value: [(0, 1), (1, 1), (1, 0), (2, 0)],
    PieceType.Z_PIECE.value: [(0, 0), (1, 0), (1, 1), (2, 1)],
    PieceType.O_PIECE.value: [(0, 0), (0, 1), (1, 0), (1, 1)],
    PieceType.J_PIECE.value: [(0, 1), (1, 1), (2, 1), (2, 0)]
}

PIECE_INITIAL_X_OFFSET = {
    PieceType.T_PIECE.value: UNIT * 3,
    PieceType.L_PIECE.value: UNIT * 3,
    PieceType.I_PIECE.value: UNIT * 4,
    PieceType.S_PIECE.value: UNIT * 3,
    PieceType.Z_PIECE.value: UNIT * 3,
    PieceType.O_PIECE.value: UNIT * 5,
    PieceType.J_PIECE.value: UNIT * 3
}

ROTATION_OFFSETS = {
    PieceType.I_PIECE.value: [
        [(-1, -2), (0, -1), (1, 0), (2, 1)],  # 0 degrees
        [(2, -1), (1, 0), (0, 1), (-1, 2)],  # 90 degrees
        [(1, 2), (0, 1), (-1, 0), (-2, -1)],  # 180 degrees
        [(-2, 1), (-1, 0), (0, -1), (1, -2)]  # 270 degrees
    ],
    PieceType.J_PIECE.value: [
        [(-1, -1), (0, 0), (1, 1), (2, 0)],
        [(1, -1), (0, 0), (-1, 1), (0, 2)],
        [(1, 1), (0, 0), (-1, -1), (-2, 0)],
        [(-1, 1), (0, 0), (1, -1), (0, -2)]
    ],
    PieceType.L_PIECE.value: [
        [(0, -2), (-1, -1), (0, 0), (1, 1)],
        [(2, 0), (1, -1), (0, 0), (-1, 1)],
        [(0, 2), (1, 1), (0, 0), (-1, -1)],
        [(-2, 0), (-1, 1), (0, 0), (1, -1)]
    ],
    PieceType.O_PIECE.value: [
        [(0, 0), (0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0), (0, 0)]
    ],
    PieceType.S_PIECE.value: [
        [(-1, -1), (0, 0), (1, -1), (2, 0)],
        [(1, -1), (0, 0), (1, 1), (0, 2)],
        [(1, 1), (0, 0), (-1, 1), (-2, 0)],
        [(-1, 1), (0, 0), (-1, -1), (0, -2)]
    ],
    PieceType.Z_PIECE.value: [
        [(0, -2), (1, -1), (0, 0), (1, 1)],
        [(2, 0), (1, 1), (0, 0), (-1, 1)],
        [(0, 2), (-1, 1), (0, 0), (-1, -1)],
        [(-2, 0), (-1, -1), (0, 0), (1, -1)]
    ],
    PieceType.T_PIECE.value: [
        [(-1, -1), (0, 0), (1, 1), (1, -1)],
        [(1, -1), (0, 0), (-1, 1), (1, 1)],
        [(1, 1), (0, 0), (-1, -1), (-1, 1)],
        [(-1, 1), (0, 0), (1, -1), (-1, -1)]
    ]
}
