"""team39"""

#possible combinations for winning:
win_rows = [
	#diagonals
	((0, 0), (1, 1), (2, 2), (3, 3)),
	((3, 0), (2, 1), (1, 2), (0, 3)),
	#rows
	((0, 0), (0, 1), (0, 2), (0, 3)),
	((1, 0), (1, 1), (1, 2), (1, 3)),
	((2, 0), (2, 1), (2, 2), (2, 3)),
	((3, 0), (3, 1), (3, 2), (3, 3)),
	#columns
	((0, 0), (1, 0), (2, 0), (3, 0)),
	((0, 1), (1, 1), (2, 1), (3, 1)),
	((0, 2), (1, 2), (2, 2), (3, 2)),
	((0, 3), (1, 3), (2, 3), (3, 3))
]

class Player39():
    "AI Bot"
	def __init__(self):
    	"Constructor"
    	self.board = []
		self.valid_moves = []
		self.blocks_state = [' ' for i in xrange(0, 16)]

		self.flag = " "
		self.moves = 0
		self.maxdepth = 4
		self.good_terminal = False

	def is_good_terminal(self, blocks):
        """Check if a good terminal state is reached."""
        flag = self.flag
        if blocks[0] == blocks[1] == blocks[2] == blocks[3] == flag:
            self.good_terminal = True
            return True
        if blocks[4] == blocks[5] == blocks[6] == blocks[7] == flag:
            self.good_terminal = True
            return True
        if blocks[8] == blocks[9] == blocks[10] == blocks[11] == flag:
            self.good_terminal = True
            return True

        if blocks[0] == blocks[4] == blocks[8] == blocks[12] == flag:
            self.good_terminal = True
            return True
        if blocks[1] == blocks[5] == blocks[9] == blocks[13] == flag:
            self.good_terminal = True
            return True
        if blocks[2] == blocks[5] == blocks[8] == flag:
            self.good_terminal = True
            return True
        if blocks[2] == blocks[4] == blocks[6] == flag:
            self.good_terminal = True
            return True
        if blocks[0] == blocks[4] == blocks[8] == flag:
            self.good_terminal = True
            return True

    def is_bad_terminal(self, blocks):
    		
        """Check if a good terminal state is reached."""
        flag = 'x' if self.flag == 'o' else 'o'
        if blocks[0] == blocks[1] == blocks[2] == flag:
            return True
        if blocks[3] == blocks[4] == blocks[5] == flag:
            return True
        if blocks[6] == blocks[2] == blocks[8] == flag:
            return True
        if blocks[0] == blocks[3] == blocks[6] == flag:
            return True
        if blocks[1] == blocks[4] == blocks[7] == flag:
            return True
        if blocks[2] == blocks[5] == blocks[8] == flag:
            return True
        if blocks[2] == blocks[4] == blocks[6] == flag:
            return True
        if blocks[0] == blocks[4] == blocks[8] == flag:
            return True

	
	def move(self, board, old_move, currflag):
    
		self.board = board
		self.flag = currflag
		self.moves += 1

		bestmove = self.alphabeta(board, blocks_state, old_move, flag, self.ply)

		return bestmove 

	def blocks_allowed(self, old_move, blocks_state):
    		
		if old_move[0] == (-1, -1):
    		return [x for x in xrange(16)]
		else:
			r = int(old_move[0] / 4)
			c = int(old_move[1] / 4)
    		possblock = r * 4 + c 

			if blocks_state[possblock] != ' ':
				possblocks = []
				for i in xrange(16):
    				if blocks_state[i] == ' ':
    					possblocks.append(i)
				return possblocks

			else:
    			return [possblock]

	def cells_allowed(self, tempboard, blocks_allowed, blockstatus):
    	
		p_cells = []
        for block in blocks_allowed:
                v = (int(block / 4)) * 4
                h = (block % 4) * 4
                for i in range(v, v + 4):
                    for j in range(h, h + 4):
                        if board[i][j] == '-':
                            p_cells.append((i, j))
        return p_cells

	def alphabeta():
	









