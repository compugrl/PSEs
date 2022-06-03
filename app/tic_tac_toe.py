'''
Create a function named tic_tac_toe_winner that is responsible for determing the state of a Tic Tac Toe board - Either there's no winner, it's a tie, 'X' won, or 'O' won. This function should take in 3x3 matrix as a parameter. Each element is either an 'X', 'O', or empty string ''. This function should have a return value of the winner 'X' or 'O', 'Tie' (for a full board with no winner), or None (for a game that is still in progress).

'''
winning_combos = [[ (0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [ (0, 0), (1, 0), (2, 0)], [ (0, 1), (1, 1), (2, 1)], [ (0, 2), (1, 2), (2, 2)], [ (0, 0), (1, 1), (2, 2)], [ (0, 2), (1, 1), (2, 0)]]

def tic_tac_toe_winner(board):
    winning_char = ''
    blank_cell = False

    for i in range(len(winning_combos)):
        cells = []
        combo = winning_combos[i]
        
        for coords in combo:
            coord1 = coords[0]
            coord2 = coords[1]
            cell = board[coord1][coord2]
            if cell == '':
                blank_cell = True
            cells.append(cell)
        
        if cells[0] == cells[1] == cells[2]:
            winning_char += cells[0]
    
    if winning_char == 'XO' or winning_char == 'OX':
        winning_char = 'Tie'
    elif winning_char == '' and not blank_cell:
        winning_char = 'Tie'
    elif winning_char == '' and blank_cell:
        winning_char = None

    return winning_char

board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', '', 'O']
    ]

print(f"Winner: {tic_tac_toe_winner(board)}")