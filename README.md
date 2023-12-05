# AITermProject
#Implementation Of Multiple Tic Tac Toe Agents In A Tournament Setting

# Introduction:

Tic Tac Toe is a classic two-player game played on a square grid. Each player, represented by X or O, aims to achieve their symbol in an entire row, column, or diagonal to win. This implementation introduces a tournament setting where various intelligent agents compete against each other in the game.

# Implemented Agents:

The project features four distinct agents, each employing a different strategy to play Tic Tac Toe effectively:

# Minimax Agent:

Utilizes a backtracking algorithm for optimal decision-making in a two-player zero-sum game.
Analyzes potential moves through recursive layers of maximizing and minimizing nodes.

# Alpha-Beta Pruning Minimax Agent:

Builds on the Minimax algorithm, incorporating alpha-beta pruning to optimize the search for the best moves.
Alpha and beta values determine the range of nodes to explore, enhancing efficiency.

# Expectimax Agent:

Similar to Minimax but includes a chance node, assuming the opponent's moves are based on probability rather than optimal play.
Considers the average utility of all possible nodes, providing a more realistic model for opponent behavior.

# Q-Learning Agent:
A reinforcement learning algorithm that learns optimal moves through trial and error.
Requires training with the game environment to develop strategies based on received rewards.

# How to Run the Code:

Execute the multiAgentTicTacToe.py file.
Enter the names of Agent 1 and Agent 2 as prompted in the console, ensuring they are different.
Specify the number of games to be played in the tournament.
Observe and compare how different agents perform against each other in multiple game scenarios.

# Instructions for Running the Tournament:

Select two different agents for the Tic Tac Toe game.
Run the tournament multiple times to assess and compare the performance of various agents.
Analyze the outcomes to identify which agent demonstrates superior gameplay.

# Additional Notes:
Make sure to choose diverse agent combinations to explore different matchups.
The Q-Learning Agent requires prior training in the game environment before participating in the tournament.

# Specify the required version of Python
python_version >= 3.6
