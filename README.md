Ultimate Tic Tac Toe Assignment

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

Beginning: Center is the best tile to target.
Force opponent on edge tiles for best effect.
Corner at mini block is attacking the block itself but giving the opponent a corner block in next turn
Edge at mini block is defending the block itself but giving opponent a relatively worse position in the next turn
Dont let opponent gain a block (big) when possible unless it guarantees you winning one next
Fix stalemates when no move gives a clear advantage

