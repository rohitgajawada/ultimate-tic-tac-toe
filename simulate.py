import game as *

class Simulator:
    __init__(self, Agent1, Agent2):
        self.agent1 = Agent1;
        self.agent2 = Agent2;

    # play a single game and return the winner
    def playGame(self):
        state = startState();
        while not endState(state):
            if player(state) == 1:
                action = Agent1.getAction(state);
            elif player(state) == 2:
                action = Agent2.getAction(state);
            state = succ(state, action);

        if utility(state) > 0:
            return 1
        else
            return 2

    def playGames(self, n): # n is the number of games to be played
        wins = 0.0;
        for i in range(n):
            if self.playGame() == 1:
                wins += 1
        return wins / n;
