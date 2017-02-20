"""team39"""
import copy
import random
import time

# possible combinations for winning:
win_rows = [
    # diagonals
    ((0, 0), (1, 1), (2, 2), (3, 3)),
    ((3, 0), (2, 1), (1, 2), (0, 3)),
    # rows
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((1, 0), (1, 1), (1, 2), (1, 3)),
    ((2, 0), (2, 1), (2, 2), (2, 3)),
    ((3, 0), (3, 1), (3, 2), (3, 3)),
    # columns
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 1), (1, 1), (2, 1), (3, 1)),
    ((0, 2), (1, 2), (2, 2), (3, 2)),
    ((0, 3), (1, 3), (2, 3), (3, 3))
]

block_map = [
    [0, 0, 0, 1, 0, 2, 0, 3, 1, 0, 1, 1, 1, 2, 1, 3, 2, 0, 2, 1, 2, 2, 2, 3, 3, 0, 3, 1, 3, 2, 3, 3],
    [0, 4, 0, 5, 0, 6, 0, 7, 1, 4, 1, 5, 1, 6, 1, 7, 2, 4, 2, 5, 2, 6, 2, 7, 3, 4, 3, 5, 3, 6, 3, 7],
    [0, 8, 0, 9, 0, 10, 0, 11, 1, 8, 1, 9, 1, 10, 1, 11, 2, 8, 2, 9, 2, 10, 2, 11, 3, 8, 3, 9, 3, 10, 3, 11],
    [0, 12, 0, 13, 0, 14, 0, 15, 1, 12, 1, 13, 1, 14, 1, 15, 2, 12, 2, 13, 2, 14, 2, 15, 3, 12, 3, 13, 3, 14, 3, 15],

    [4, 0, 4, 1, 4, 2, 4, 3, 5, 0, 5, 1, 5, 2, 5, 3, 6, 0, 6, 1, 6, 2, 6, 3, 7, 0, 7, 1, 7, 2, 7, 3],
    [4, 4, 4, 5, 4, 6, 4, 7, 5, 4, 5, 5, 5, 6, 5, 7, 6, 4, 6, 5, 6, 6, 6, 7, 7, 4, 7, 5, 7, 6, 7, 7],
    [4, 8, 4, 9, 4, 10, 4, 11, 5, 8, 5, 9, 5, 10, 5, 11, 6, 8, 6, 9, 6, 10, 6, 11, 7, 8, 7, 9, 7, 10, 7, 11],
    [4, 12, 4, 13, 4, 14, 4, 15, 5, 12, 5, 13, 5, 14, 5, 15, 6, 12, 6, 13, 6, 14, 6, 15, 7, 12, 7, 13, 7, 14, 7, 15],

    [8, 0, 8, 1, 8, 2, 8, 3, 9, 0, 9, 1, 9, 2, 9, 3, 10, 0, 10, 1, 10, 2, 10, 3, 11, 0, 11, 1, 11, 2, 11, 3],
    [8, 4, 8, 5, 8, 6, 8, 7, 9, 4, 9, 5, 9, 6, 9, 7, 10, 4, 10, 5, 10, 6, 10, 7, 11, 4, 11, 5, 11, 6, 11, 7],
    [8, 8, 8, 9, 8, 10, 8, 11, 9, 8, 9, 9, 9, 10, 9, 11, 10, 8, 10, 9, 10, 10, 10, 11, 11, 8, 11, 9, 11, 10, 11, 11],
    [8, 12, 8, 13, 8, 14, 8, 15, 9, 12, 9, 13, 9, 14, 9, 15, 10, 12, 10, 13, 10, 14, 10, 15, 11, 12, 11, 13, 11, 14, 11, 15],

    [12, 0, 12, 1, 12, 2, 12, 3, 13, 0, 13, 1, 13, 2, 13, 3, 14, 0, 14, 1, 14, 2, 14, 3, 15, 0, 15, 1, 15, 2, 15, 3],
    [12, 4, 12, 5, 12, 6, 12, 7, 13, 4, 13, 5, 13, 6, 13, 7, 14, 4, 14, 5, 14, 6, 14, 7, 15, 4, 15, 5, 15, 6, 15, 7],
    [12, 8, 12, 9, 12, 10, 12, 11, 13, 8, 13, 9, 13, 10, 13, 11, 14, 8, 14, 9, 14, 10, 14, 11, 15, 8, 15, 9, 15, 10, 15, 11],
    [12, 12, 12, 13, 12, 14, 12, 15, 13, 12, 13, 13, 13, 14, 13, 15, 14, 12, 14, 13, 14, 14, 14, 15, 15, 12, 15, 13, 15, 14, 15, 15]
]

class Player39():
    """AI Bot"""

    def __init__(self):
        "Constructor"
        self.board = []
        self.valid_moves = []
        self.blocks_state = ['-' for i in xrange(16)]

        self.flag = " "
        self.levelincr = 0
        self.moves = 0
        self.maxdepth = 4
        self.good_terminal = False

        self.utility = [0 for i in xrange(16)]

    def move(self, board, old_move, currflag):

        total_start = time.time()
        self.board = copy.deepcopy(board.board_status)
        tempblockstatus = copy.deepcopy(board.block_status)

        for i in xrange(4):
            for j in xrange(4):
                self.blocks_state[4*i + j] = tempblockstatus[i][j]

        self.flag = currflag
        self.moves += 1

        bestmove = self.alphabeta(self.board, self.blocks_state, old_move, self.flag, self.levelincr)

        total_end = time.time()
        print "total move time: ", total_end - total_start

        return bestmove

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
        if blocks[12] == blocks[13] == blocks[14] == blocks[15] == flag:
            self.good_terminal = True
            return True

        if blocks[0] == blocks[4] == blocks[8] == blocks[12] == flag:
            self.good_terminal = True
            return True
        if blocks[1] == blocks[5] == blocks[9] == blocks[13] == flag:
            self.good_terminal = True
            return True
        if blocks[2] == blocks[6] == blocks[10] == blocks[14] == flag:
            self.good_terminal = True
            return True
        if blocks[3] == blocks[7] == blocks[11] == blocks[15] == flag:
            self.good_terminal = True
            return True

        if blocks[0] == blocks[5] == blocks[10] == blocks[15] == flag:
            self.good_terminal = True
            return True
        if blocks[3] == blocks[6] == blocks[9] == blocks[12] == flag:
            self.good_terminal = True
            return True

    def is_bad_terminal(self, blocks):
        """Check if a bad terminal state is reached."""
        flag = 'x' if self.flag == 'o' else 'o'

        if blocks[0] == blocks[1] == blocks[2] == blocks[3] == flag:
            return True
        if blocks[4] == blocks[5] == blocks[6] == blocks[7] == flag:
            return True
        if blocks[8] == blocks[9] == blocks[10] == blocks[11] == flag:
            return True
        if blocks[12] == blocks[13] == blocks[14] == blocks[15] == flag:
            return True

        if blocks[0] == blocks[4] == blocks[8] == blocks[12] == flag:
            return True
        if blocks[1] == blocks[5] == blocks[9] == blocks[13] == flag:
            return True
        if blocks[2] == blocks[6] == blocks[10] == blocks[14] == flag:
            return True
        if blocks[3] == blocks[7] == blocks[11] == blocks[15] == flag:
            return True

        if blocks[0] == blocks[5] == blocks[10] == blocks[15] == flag:
            return True
        if blocks[3] == blocks[6] == blocks[9] == blocks[12] == flag:
            return True


    def blocks_allowed(self, old_move, blocks_state):

        r = int(old_move[0] % 4)
        c = int(old_move[1] % 4)
        blocknum = r*4 + c;

        if old_move[0] == (-1, -1):
            return [x for x in xrange(16)]
        else:
            r = int(old_move[0] % 4)
            c = int(old_move[1] % 4)
            possblock = r * 4 + c

            if blocks_state[possblock] != '-':
                possblocks = []
                for i in xrange(16):
                    if blocks_state[i] == '-':
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

                        if tempboard[i][j] == '-':
                            p_cells.append((i, j))

        return p_cells

    def evolvedblockstate(self, board, old_move, oldblockstate, currflag):

        block_stat = oldblockstate[:]

        if old_move == (-1, -1):
            return block_stat

        blockx = int(old_move[0] / 4)
        blocky = int(old_move[1] / 4)
        block_num = blockx * 4 + blocky
        currblock = block_map[blockx * 4 + blocky]

        #rows
        if board[currblock[0]][currblock[1]] == board[currblock[2]][currblock[3]] == board[currblock[4]][currblock[5]] == board[currblock[6]][currblock[7]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        if board[currblock[8]][currblock[9]] == board[currblock[10]][currblock[11]] == board[currblock[12]][currblock[13]] == board[currblock[14]][currblock[15]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        if board[currblock[16]][currblock[17]] == board[currblock[18]][currblock[19]] == board[currblock[20]][currblock[21]] == board[currblock[22]][currblock[23]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        if board[currblock[24]][currblock[25]] == board[currblock[26]][currblock[27]] == board[currblock[28]][currblock[29]] == board[currblock[30]][currblock[31]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        #columns
        if board[currblock[0]][currblock[1]] == board[currblock[8]][currblock[9]] == board[currblock[16]][currblock[17]] == board[currblock[24]][currblock[25]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        if board[currblock[2]][currblock[3]] == board[currblock[10]][currblock[11]] == board[currblock[18]][currblock[19]] == board[currblock[26]][currblock[27]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        if board[currblock[4]][currblock[5]] == board[currblock[12]][currblock[13]] == board[currblock[20]][currblock[21]] == board[currblock[28]][currblock[29]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        if board[currblock[6]][currblock[7]] == board[currblock[14]][currblock[15]] == board[currblock[22]][currblock[23]] == board[currblock[30]][currblock[31]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        #diagonals
        if board[currblock[0]][currblock[1]] == board[currblock[10]][currblock[11]] == board[currblock[20]][currblock[21]] == board[currblock[30]][currblock[31]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        if board[currblock[6]][currblock[7]] == board[currblock[12]][currblock[13]] == board[currblock[18]][currblock[19]] == board[currblock[24]][currblock[25]] == currflag:
            block_stat[block_num] = currflag
            return block_stat

        for i in range(blockx, blockx + 4):
            for j in range(blocky, blocky + 4):
                if board[i][j] == '-':
                    return block_stat

        block_stat[block_num] = 'D'
        return block_stat

    def alphabeta(self, board, blocks_state, old_move, flag, levelincr):

        if old_move == (-1, -1):
            return (4, 4)

        playable_cells = self.cells_allowed(board, self.blocks_allowed(old_move, blocks_state), blocks_state)

        alpha = best_score = score = float('-inf')
        beta = float('inf')
        best_move = []

        if not playable_cells:
            return self.temp()

        for move in playable_cells:
            tempblockstate = blocks_state[:]

            board[move[0]][move[1]] = flag
            tempblockstate = self.evolvedblockstate(board, move, blocks_state, flag)
            score = self.alpha_max(board, tempblockstate, move, flag, 0, alpha, beta, levelincr)

            board[move[0]][move[1]] = '-'

            if score == best_score:
                best_move.append(move)
            if score > best_score:
                best_score = score
                best_move = [move]

            alpha = max(alpha, best_score)
            if alpha >= beta:
                break

        return best_move[random.randrange(len(best_move))]

    def alpha_max(self, board, blocks_state, old_move, flag, depth, alpha, beta, levelincr):

        alphamaxstart = time.time()
        if self.is_bad_terminal(blocks_state) is True:
            return float('-inf')

        if depth > 4 + levelincr:
            return self.temp()

        playable_cells = self.cells_allowed(board, self.blocks_allowed(old_move, blocks_state), blocks_state)

        if not playable_cells:
            return self.temp()

        best_score = float('-inf')
        for move in playable_cells:
            tempblockst = blocks_state[:]
            board[move[0]][move[1]] = flag
            tempblockst = self.evolvedblockstate(board, move,tempblockst, flag)
            score = self.alpha_min(board, tempblockst, move, flag, depth + 1, alpha, beta, levelincr)

            board[move[0]][move[1]] = '-'

            if score > best_score:
                best_score = score

            alpha = max(alpha, best_score)
            if alpha >= beta:
                break

        alphamaxend = time.time()

        print "alphamax time:", alphamaxend - alphamaxstart

        return best_score

    def alpha_min(self, board, blocks_state, old_move, flag, depth, alpha, beta, levelincr):

        alphaminstart = time.time()
        if self.is_good_terminal(blocks_state) is True:
            return float('inf')

        t_flag = 'o' if flag == 'x' else 'x'

        if depth > 4 + levelincr:
            return self.temp()

        playable_cells = self.cells_allowed(board, self.blocks_allowed(old_move, blocks_state), blocks_state)

        if not playable_cells:
            return self.temp()

        best_score = float('inf')

        for move in playable_cells:
            temp_blocks_st = blocks_state[:]
            board[move[0]][move[1]] = t_flag
            temp_blocks_st = self.evolvedblockstate(board, move, temp_blocks_st, t_flag)

            score = self.alpha_max(board, temp_blocks_st, move, flag,depth + 1, alpha, beta, levelincr)

            board[move[0]][move[1]] = '-'
            if score < best_score:
                best_score = score

            beta = min(beta, best_score)
            if alpha >= beta:
                break

        alphaminend = time.time()

        print "alphamin time:", alphaminend - alphaminstart

        return best_score

    def temp(self):
        return 1
