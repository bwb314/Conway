from board import board
def test_board_sizing_square():

    rows = 8
    test_board = board(rows)
    
    assert test_board.board == [[0] * rows for _ in range(rows)]

def test_board_sizing_rectangle():

    rows = 8
    cols = 4
    test_board = board(rows, cols)
    
    assert test_board.board == [[0] * cols for _ in range(rows)]
