import random
import time
class Game():
    WIN_SCORE = 1
    DRAW_SCORE = 0
    LOSS_SCORE = -1

    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2
        self.agent1_score = 0
        self.agent2_score = 0
        self.agent1_moves = 0
        self.agent2_moves = 0
        self.game_durations = []

    def updateMoveCount(self, currentAgent):
        if currentAgent == self.agent1:
            self.agent1_moves += 1
        elif currentAgent == self.agent2:
            self.agent2_moves += 1

    def calculateAverageDuration(self):
        if len(self.game_durations) > 0:
            return sum(self.game_durations) / len(self.game_durations)
        else:
            return 0

    boardvalues = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def board(self):
        count = 0
        for i in range(0, 3):
            print("|", end=" ")
            for j in range(0, 3):
                print(self.boardvalues[i + j + count], "|", end=" "),
            count += 2
            print("\n____________")

    def gameState(self):
        agents = ["Agent1", "Agent2"]
        nextTurn = 'Test'
        start_time = time.time()
        for i in range(0, 9):
            if (i % 2 == 0):
                currentAgent = agent1
                nextTurn = 'X'
            else:
                currentAgent = agent2
                nextTurn = 'O'
            print("Hey " + currentAgent + " Agent! Where do you wanna place " + nextTurn + " at?")
            self.board()
            print("\n")
            if nextTurn == 'X':
                if currentAgent == "QLearning":
                    number = self.trainedMove(game)
                else:
                    number = self.finalMove(currentAgent)
            else:
                if currentAgent == "QLearning":
                    number = self.trainedMove(game)
                else:
                    number = self.finalMove(currentAgent)

            if number is not None and self.boardvalues[number] == " ":
                self.boardvalues[number] = nextTurn
                self.updateMoveCount(currentAgent)
                result = self.isEnd()
                if result:
                    self.board()
                    if result == 'D':
                        self.agent1_score += self.DRAW_SCORE
                        self.agent2_score += self.DRAW_SCORE
                        print("OOPS! Unfortunately, we don't have a winner this time. Better luck next time.")
                    else:
                        if result == 'X':
                            self.agent1_score += self.WIN_SCORE
                            print("OMG! We have a winner. Congratulations " + agent1)
                        elif result == 'O':
                            self.agent2_score += self.WIN_SCORE
                            print("OMG! We have a winner. Congratulations " + agent2)
                    break
                else:
                    continue
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.game_durations.append(elapsed_time)

    def placeAgent(self, position, curAgent):
        player = None
        if (curAgent == " "):
            self.boardvalues[position] = " "
        else:
            if (curAgent == agent1):
                player = 'X'
            else:
                player = 'O'
            self.boardvalues[position] = player

    def tempGameOver(self, node, curAgent):
        if (curAgent == agent1):
            if self.gameOver(node) == 'X':
                return 1
            elif self.gameOver(node) == 'O':
                return -1
            elif self.gameOver(node) == 0:
                return 0
            else:
                return -10
        elif (curAgent == agent2):
            if self.gameOver(node) == 'X':
                return -1
            elif self.gameOver(node) == 'O':
                return 1
            elif self.gameOver(node) == 0:
                return 0
            else:
                return -10

    def gameOver(self, node):
        for i in range(0, 9, 3):
            # Check rows
            if node.boardvalues[i] == node.boardvalues[i + 1] == node.boardvalues[i + 2] != " ":
                return node.boardvalues[i]

        for i in range(3):
            # Check columns
            if node.boardvalues[i] == node.boardvalues[i + 3] == node.boardvalues[i + 6] != " ":
                return node.boardvalues[i]

        # Check diagonals
        if node.boardvalues[0] == node.boardvalues[4] == node.boardvalues[8] != " ":
            return node.boardvalues[0]
        elif node.boardvalues[2] == node.boardvalues[4] == node.boardvalues[6] != " ":
            return node.boardvalues[2]

        for i in range(0, 9):
            if node.boardvalues[i] == " ":
                return None  # Game is not finished

        return 'D'  # Draw

    def isEnd(self):
        if (self.boardvalues[0] == self.boardvalues[1] == self.boardvalues[2] != " "):
            return self.boardvalues[2]
        elif (self.boardvalues[3] == self.boardvalues[4] == self.boardvalues[5] != " "):
            return self.boardvalues[5]
        elif (self.boardvalues[6] == self.boardvalues[7] == self.boardvalues[8] != " "):
            return self.boardvalues[8]
        elif (self.boardvalues[0] == self.boardvalues[3] == self.boardvalues[6] != " "):
            return self.boardvalues[6]
        elif (self.boardvalues[1] == self.boardvalues[4] == self.boardvalues[7] != " "):
            return self.boardvalues[7]
        elif (self.boardvalues[2] == self.boardvalues[5] == self.boardvalues[8] != " "):
            return self.boardvalues[8]
        elif (self.boardvalues[0] == self.boardvalues[4] == self.boardvalues[8] != " "):
            return self.boardvalues[8]
        elif (self.boardvalues[2] == self.boardvalues[4] == self.boardvalues[6] != " "):
            return self.boardvalues[6]
        else:
            for i in range(0, 9):
                if (self.boardvalues[i] == " "):
                    return None  # Game is not finished
            return 'D'  # Draw

    def positionsLeft(self):
        pl = []
        for i in range(len(self.boardvalues)):
            if self.boardvalues[i] == " ":
                pl.append(int(i))
        return pl

    def gameOverValue(self, agent):
        if (agent == 'X'):
            return -1
        elif (agent == 'O'):
            return 1
        else:
            return 0

    def minimax(self, node, curAgent):
        '''
        Minimax algorithm for choosing the best possible move towards
        winning the game
        '''
        if node.tempGameOver(node, curAgent) == -1 or node.tempGameOver(node, curAgent) == 1 or node.tempGameOver(node,curAgent) == 0:
            return node.tempGameOver(node, curAgent)
        else:
            # maxValue = 0
            maxValue = float('-inf')
            if curAgent == "Minimax":
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.minimax(node, self.getOtherAgent(curAgent))
                    node.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                return maxValue
            else:
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.minimax(node, self.getOtherAgent(curAgent))
                    node.placeAgent(move, " ")
                    if (newValue < maxValue):
                        maxValue = newValue
                return maxValue

    def alphabeta(self, node, curAgent, alpha, beta):
        '''
        Alphabeta pruning minimax algorithm for choosing the best possible move towards
        winning the game
        '''
        if node.tempGameOver(node, curAgent) == -1 or node.tempGameOver(node, curAgent) == 1 or node.tempGameOver(node,
                                                                                                                  curAgent) == 0:
            return node.tempGameOver(node, curAgent)
        else:
            maxValue = float('-inf')
            if curAgent == "Alphabeta_Minimax":
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.alphabeta(node, self.getOtherAgent(curAgent), alpha, beta)
                    node.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                    if (maxValue > beta):
                        return maxValue
                    else:
                        alpha = max(alpha, maxValue)
                return maxValue
            else:
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.alphabeta(node, self.getOtherAgent(curAgent), alpha, beta)
                    node.placeAgent(move, " ")
                    if (newValue < maxValue):
                        maxValue = newValue
                    if (maxValue < alpha):
                        return maxValue
                    else:
                        beta = min(beta, maxValue)
                return maxValue

    def expectimax(self, node, curAgent):
        '''
        Minimax algorithm for choosing the best possible move towards
        winning the game
        '''
        if node.tempGameOver(node, curAgent) == -1 or node.tempGameOver(node, curAgent) == 1 or node.tempGameOver(node,
                                                                                                                  curAgent) == 0:
            return node.tempGameOver(node, curAgent)
        else:
            maxValue = float('-inf')
            if curAgent == "Expectimax":
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.expectimax(node, self.getOtherAgent(curAgent))
                    node.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                return maxValue
            else:
                NoofPossibilities = len(node.positionsLeft())
                probability = 1 / NoofPossibilities
                expectiValue = 0
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.expectimax(node, self.getOtherAgent(curAgent))
                    node.placeAgent(move, " ")
                    expectiValue = expectiValue + (newValue * probability)
                return expectiValue

    def QLwin(self, board, Ql_key):
        """ If we have two in a row and the 3rd is available, take it. """
        # Check for diagonal wins
        diag1 = [self.boardvalues[0], self.boardvalues[4], self.boardvalues[8]]
        diag2 = [self.boardvalues[2], self.boardvalues[4], self.boardvalues[6]]
        if diag1.count(" ") == 1 and diag1.count(Ql_key) == 2:
            ind = diag1.index(" ")
            if ind == 0:
                return 0
            elif ind == 1:
                return 4
            else:
                return 8
        elif diag2.count(" ") == 1 and diag2.count(Ql_key) == 2:
            ind = diag2.index(" ")
            if ind == 0:
                return 2
            elif ind == 1:
                return 4
            else:
                return 6
        for i in range(3):
            count = 0
            rows = [self.boardvalues[count], self.boardvalues[count + 1], self.boardvalues[count + 2]]
            if rows.count(" ") == 1 and rows.count(Ql_key) == 2:
                ind = rows.index(" ")
                if ind == 0:
                    return count
                elif ind == 1:
                    return count + 1
                else:
                    return count + 2
            count = count + 3

        for j in range(3):
            count = 0
            cols = [self.boardvalues[count], self.boardvalues[count + 3], self.boardvalues[count + 6]]
            if cols.count(" ") == 1 and cols.count(Ql_key) == 2:
                ind = cols.index(" ")
                if ind == 0:
                    return count
                elif ind == 1:
                    return count + 3
                else:
                    return count + 6
            count = count + 1
        return None

    def blockWin(self, board, enemyKey):
        """ Block the opponent if she has a win available. """
        return self.QLwin(board, enemyKey)

    def pickcenter(self, board):
        """ Pick the center if it is available. """
        if self.boardvalues[4] == " ":
            return 4
        return None

    def pickcorner(self, board, enemyKey):

        corner = [self.boardvalues[0], self.boardvalues[2], self.boardvalues[6], self.boardvalues[8]]
        if corner.count(" ") == 4:
            return corner.index(random.choice(corner))
        else:
            if self.boardvalues[0] == enemyKey and self.boardvalues[8] == " ":
                return 8
            elif self.boardvalues[2] == enemyKey and self.boardvalues[6] == " ":
                return 6
            elif self.boardvalues[8] == enemyKey and self.boardvalues[0] == " ":
                return 0
            elif self.boardvalues[6] == enemyKey and self.boardvalues[2] == " ":
                return 2
        return None

    def diamondside(self, board):
        """ Pick an empty side. """
        diamond = [self.boardvalues[1], self.boardvalues[3], self.boardvalues[5], self.boardvalues[7]]
        if diamond.count(" ") == 4:
            return diamond.index(random.choice(diamond))
        else:
            count = 1
            for i in range(0, 3):
                if (diamond[i] == " "):
                    return count
                count = count + 2
        return None

    def trainedMove(self, board):
        """
        Trained move for Q-Learning Agent
        """
        if self.agent1 == "QLearning":
            Ql_key = 'X'
            enemyKey = 'O'
        elif self.agent2 == "QLearning":
            Ql_key = 'O'
            enemyKey = 'X'

        # Check if there are any available positions
        available_positions = self.positionsLeft()
        if not available_positions:
            return None

        # Adjust the exploration-exploitation trade-off
        exploration_threshold = 0.9

        # Explore with a probability threshold
        if random.random() > exploration_threshold:
            return random.choice(available_positions)

        # Follow optimal strategy
        if (winning_move := self.QLwin(board, Ql_key)) is not None and winning_move != ' ':
            return winning_move
        elif (blocking_move := self.blockWin(board, enemyKey)) is not None and blocking_move != ' ':
            return blocking_move
        elif (center_move := self.pickcenter(board)) is not None and center_move != ' ':
            return center_move
        elif (corner_move := self.pickcorner(board, enemyKey)) is not None and corner_move != ' ':
            return corner_move
        elif (side_move := self.diamondside(board)) is not None and side_move != ' ':
            return side_move
        else:
            # If no specific strategy, choose a random available position
            return random.choice(available_positions)


    def evaluate_agents(self, num_games=100):
        agent1_wins = 0
        agent2_wins = 0
        draws = 0
        total_duration = 0
        agent1_score = 0
        agent2_score = 0
        for game_num in range(num_games):
            self.agent1_score = 0
            self.agent2_score = 0
            # Reset the game for a new round
            self.__init__(self.agent1, self.agent2)
            # Keep track of time for each move
            start_time = time.time()
            # Play the game
            self.gameState()
            # Calculate the time taken for the game
            end_time = time.time()
            elapsed_time = end_time - start_time
            # Determine the winner and update statistics
            winner = self.isEnd()
            if winner == "X":
                agent1_wins += 1
                self.agent1_score += game.WIN_SCORE
                self.agent2_score += game.LOSS_SCORE
            elif winner == "O":
                agent2_wins += 1
                self.agent1_score += game.LOSS_SCORE
                self.agent2_score += game.WIN_SCORE
            else:
                draws += 1
                self.agent1_score += game.DRAW_SCORE
                self.agent2_score += game.DRAW_SCORE

            # Print information about the game and metrics
            print(f"Game {game_num + 1}: {self.agent1} wins : {agent1_wins}, {self.agent2} wins : {agent2_wins},Draws : {draws}")
            print(f"Time taken for the game: {elapsed_time:.2f} seconds")
            print(f"{self.agent1} moves: {self.agent1_moves}, {self.agent2} moves: {self.agent2_moves}")
            print(f"Average game duration: {self.calculateAverageDuration():.2f} seconds\n")

            total_duration += elapsed_time
            agent1_score += self.agent1_score
            agent2_score += self.agent2_score

        average_duration = total_duration / num_games


        # Print overall performance summary
        print("Overall Performance Summary:")
        print(f"{agent1} wins: {agent1_wins}")
        print(f"{agent2} wins: {agent2_wins}")
        print(f"Draws: {draws}")
        print(f"Average game duration: {average_duration:.2f} seconds/n")
        print(f"{self.agent1} score: {(agent1_wins*1)+((num_games-agent1_wins)*-1)}")
        print(f"{self.agent2} score: {(agent2_wins*1)+((num_games-agent2_wins)*-1)}")

    def getOtherAgent(self, currentAgent):
        if currentAgent == self.agent1:
            return self.agent2
        else:
            return self.agent1

    def finalMove(self, currentAgent):
        bestValue = float('-inf') if currentAgent == "Minimax" or currentAgent == "Expectimax" else float('inf')
        bestMove = []
        newValue = 0
        available_positions = self.positionsLeft()
        if not available_positions:
            return None
        for move in self.positionsLeft():
            self.placeAgent(move, currentAgent)
            if currentAgent == "Minimax":
                newValue = self.minimax(self, self.getOtherAgent(currentAgent))
            elif currentAgent == "Alphabeta_Minimax":
                newValue = self.alphabeta(self, self.getOtherAgent(currentAgent), -1000, 1000)
            elif currentAgent == "Expectimax":
                newValue = self.expectimax(self, self.getOtherAgent(currentAgent))
            self.placeAgent(move, " ")
            if (currentAgent == "Minimax" or currentAgent == "Expectimax") and newValue > bestValue:
                bestValue = newValue
                bestMove = [move]
            elif currentAgent == "Alphabeta_Minimax" and newValue < bestValue:
                bestValue = newValue
                bestMove = [move]
        if not bestMove:
            return random.choice(self.positionsLeft())
        else:
            return random.choice(bestMove)


def select_agent(prompt):
    print(prompt)
    print("1. Minimax\n2. Alphabeta_Minimax\n3. Expectimax\n4. QLearning")
    choice = input("Please enter your choice:")
    agents = ["Minimax", "Alphabeta_Minimax", "Expectimax", "QLearning"]
    if choice.isdigit() and 1 <= int(choice) <= 4:
        return agents[int(choice) - 1]
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        return select_agent(prompt)

if __name__ == "__main__":
    agent1 = select_agent("Please Select Agent1:")
    agent2 = select_agent("Please Select Agent2 (other than what you chose for Agent1):")
    num_games = int(input("Please Enter the number of games to be Played:"))
    game = Game(agent1, agent2)
    game.evaluate_agents(num_games)
