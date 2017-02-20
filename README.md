Ultimate Tic Tac Toe Assignment
===============================

-Rohit Gajawada 201401067
-Anubhab Sen 201501114

Notes:
Attacking and defending
Branch factor is 16

#defence
in 3x3
center stops 4
corner stops 3
side stops 2

in 4x4
any of the centers(4 squares) stop 3
corners stop 3
sides stop 2

#offence
in 3x3
center stops 4
corner stops 3
side stops 2

in 4x4
any of the centers(4 squares) stop 3
corners stop 3
sides stop 2

Cases:


Notes: (3 x 3 x 3 x 3)
======================

Anubhab and Arun
================

* Beginning: Center is the best tile to target.
* Force opponent on edge tiles for best effect.
* Corner at mini block is attacking the block itself but giving the opponent a corner block in next turn
* Edge at mini block is defending the block itself but giving opponent a relatively worse position in the next turn
* Dont let opponent gain a block (big) when possible unless it guarantees you winning one next
* Fix stalemates when no move gives a clear advantage
* A block available doesnt mean we need to block it, just dont let the opponent reach that block again
* If opponent can win by moving a tile which will ensure us to make any move next, do that

eval func:
==========

f = ax1 + bx2 + cx3 + ...

Rohit
=====

Cases:
* If you occupy a center, you can keep sending your opponent over there to waste moves but would lose overall game
* if there is a square which is not practical for opponent to win in it or if winning it would be useless to win the game, then try to push opponent into it
* don't go to win a square blindly
* sacrificing to win one square and obtaining another one which has higher likelihood to win the game
* if you send your opponent to a position that seems like it would be an advantage to him but if you think of your next steps, you can plan your win on that
6* check when winning a block, where it would send opponent and if it would let him win blocks that can give him a game win
* don't focus on a block where your opponent wont send you too
* if your opponent is trying to force you to a square that is already won, get those spaces occupied so that would prevent him from doing so

Features extracted
========

* number of blocks already won by player.
* number of blocks already won by opponent.
* number of blocks which player can win with one move in that block.
* number of blocks which opponent can win with one move in that block.
* block positions occupied beside of same type
* block positions occupied beside of opp type
* won blocks occupied beside of same type
* won blocks occupied beside of opp type

Variables
========
* number of rows that can almost be completed in terms of (4 - required no needed) and can be summed up if more that one row
* number of rows won by taking that state

* if that block is won and then correspond to above

* entropy : O is majority (for offense) or X is majority (for defence i.e to mess up opponents offense) but not tending to equal

* Lets make our array as 1d for simplification
