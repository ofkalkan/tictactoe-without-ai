import players
import os
import time

class TicTacToe():
    def __init__(self):    
        self.current_winner=None
        self.tie = None
        self.board = self.make_board()

    #Create table
    def make_board(self):
            return [" " for _ in range(9)]

    #Make a move
    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if not self.check_available():
                self.tie = True
                return self.tie
                

    #Will return the letter/new letter
    @staticmethod
    def change_letter(letter_turn):
            if letter_turn == x_player:
                letter_turn = o_player
            else:
                letter_turn = x_player
            return letter_turn
        

        
    #Check the table staus, if there is a winner, return current_winner = 1
    def check_status(self):
        situ = [self.board[2:7:2],self.board[-9::4],self.board[::3],self.board[1::3],self.board[2::3],self.board[0:3],self.board[3:6],self.board[6:9]]
        for i in range(len(situ)):
            if situ[i].count("X") == 3 or situ[i].count("O") == 3:
                self.current_winner = True
                return self.current_winner
            
            

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


#Start the game, the initialization screen.
def playthegame(game, print_game):
    if print_game:
        game.print_board_nums()
        print("Game initialization... Remember, X plays first.")

    current_letter = game.change_letter("ilk")
    while True:
        game.make_move(current_letter.get_move(t), current_letter.letter)
        time.sleep(0.3)
        os.system("clear")
        if game.check_status() or game.tie == True:
            if game.current_winner == True:
                game.print_board()
                print(f"There is a winner! {current_letter}wins!")
                break
            else:
                game.print_board()
                print("It's a tie!")
                break
        current_letter = game.change_letter(current_letter)
        game.print_board()

    

if __name__ == '__main__':
    #x_player = players.RandomComputerPlayer('X')
    o_player = players.HumanPlayer("O")
    x_player = players.HumanPlayer("X")
    t = TicTacToe()
    playthegame(t,print_game=True)


