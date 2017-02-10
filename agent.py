class minimax_agent():
    def __init__(self):
        pass

    def move(self, board, old_move, flag):
        cells = board.find_valid_move_cells(old_move)