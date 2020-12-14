import players
import os
import time

class TicTacToe():
    def __init__(self):    
        self.current_winner=None
        self.board = self.make_board()

    #Create table
    def make_board(self):
            return [" " for _ in range(9)]

    #Make a move
    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if not self.check_available():
                self.current_winner = True
                return self.current_winner

        letter == "X" if letter == "O" else letter == "X"

    #Print the table
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    #Print the table with their indexes
    @staticmethod        
    def print_board_nums():
        numbers_of_boxes = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numbers_of_boxes:
            print("| " + " | ".join(row) + " |")
    

    def check_available(self):
        return [a for a, nokta in enumerate(self.board) if nokta == " "]
    def available_moves(self):
        return list(self.check_available())


def playthegame(game, o_player, print_game):

    #Start the game, the initialization screen.
    if print_game:
        game.print_board_nums()
        print("Ilk oyun baslatiliyor.")
        game.print_board()


    letter = "O"
    while not game.current_winner:
        if letter == "O":
            t.make_move(o_player.get_move(t), o_player.letter)
            time.sleep(0.5)
            os.system("clear")
            t.print_board()






if __name__ == '__main__':
    #x_player = players.RandomComputerPlayer('X')
    o_player = players.HumanPlayer('O')
    t = TicTacToe()
    playthegame(t,o_player,print_game=True)


