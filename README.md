Ultimate Tic Tac Toe Assignment
===============================

Notes:
Attacking and defending
Branch factor is 16

#add degrees of freedom maybe
#add draw guarantee
#consider time overload on free moves

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

Imp notes:
Change ply and check timings (signal)
timing out in some cases
