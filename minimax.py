class minimax_agent():

	def __init__(self):
    	pass

	def minimaxVal(game, maxdepth, evaluatorFunction = None):
		if maxdepth == 0 or game.isLeafNode():
			if evaluatorFunction:
				return evaluatorFunction(game)
			else:
				return game.score()

	def move(game, maxdepth, evaluatorFunction = None):

		best = None
		for move in game.find_valid_move_cells():
			temp = game.copy()
			temp.play(move)
			val = -1 * minimaxVal(temp, maxdepth, evaluatorFunction)
			if best is None or val > best[0]:
				best = (val, move)

		return best

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










