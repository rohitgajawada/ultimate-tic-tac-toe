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
"""Bot Class"""

	def __init__(self):
    	"Constructor"
    	self.board = []
		self.valid_moves = [];
		self.flag = " "
		self.moves = 0
		self.good_endstate = False

	def move(self, board, old_move, flag):
    
		best = None
		cells = board.find_valid_move_cells(old_move)

		for move in cells:
    			
			temp = game.copy()
			temp.play(move)
			val = -1 * minimaxVal(temp, maxdepth, evaluatorFunction)
			if best is None or val > best[0]:
				best = (val, move)

		return best

	def minimaxVal(game, maxdepth, evaluatorFunction = None):
		if maxdepth == 0 or game.isLeafNode():
			if evaluatorFunction:
				return evaluatorFunction(game)
			else:
				return game.score()

	def alphabetaVal(game, maxdepth, alpha, beta, evaluatorFunction = None):
		if maxdepth = 0 or game.isLeafNode():
			if evaluatorFunction:
				return evaluatorFunction(game)
			else:
				return game.score()

		for move in game.find_valid_move_cells():
			temp = game.copy()
			temp.play(move)

			if alpha is not None:
				opponentBeta  = -1 * alpha
			else:
				opponentBeta = None

			if beta is not None:
				opponentAlpha = -1 * beta
			else:
				opponentAlpha = None

			val = -1 * alphabetaVal(temp, maxdepth - 1, opponentAlpha, opponentBeta, evaluatorFunction)
			if (alpha is not None) and (beta is not None) and alpha >= beta:
				return beta

		return alpha

	def alphabetapruning(game, maxdepth, evaluatorFunction = None):

		bestVal = None
		bestMove = None

		for move in game.find_valid_move_cells():
			temp = game.copy()
			temp.play(move)

			if bestVal is not None:
				opponentBeta = -1 * bestVal
			else:
				opponentBeta = None

			val = -1 * alphabetaVal(temp, maxdepth, None, opponentBeta, evaluatorFunction)
			if bestVal is None or val > bestVal:
				(bestVal, bestMove) = (val, move)

		return (bestVal, bestMove)










