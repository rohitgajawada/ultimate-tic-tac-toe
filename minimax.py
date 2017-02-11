def minimaxVal(game, maxdepth, evaluatorFunction = None):
	if maxdepth == 0 or game.isLeafNode():
		if evaluatorFunction:
			return evaluatorFunction(game)
		else:
			return game.score()

def minimax(game, maxdepth, evaluatorFunction = None):

	best = None
	for move in game.find_valid_move_cells():
		temp = game.copy()
		temp.play(move)
		val = -1 * minimaxVal(temp, maxdepth, evaluatorFunction)
		if best is None or val > best[0]:
			best = (val, move)

	return best