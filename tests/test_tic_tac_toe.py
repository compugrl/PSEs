import pytest
from app.tic_tac_toe import tic_tac_toe_winner

def test_tie(self):
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'Tie'

def test_incomplete(self):
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', '', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == None

def test_col_win(self):
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'O', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'O'

def test_row_win(self):
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'O'],
        ['X', 'X', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'O'

def test_diag_win(self):
    # Arrange
    board =[
        ['O', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'O'
