import random, os
import game

class Player():
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, game):
        pass



#Human player spesific
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, t):
        valid_move = False
        self.humanMove = None
        while not valid_move:        
            try:
                self.humanMove = int(input(f"{self.letter}'s turn. Make a move [0-8]: "))
                
                if not self.humanMove in t.check_available():
                    raise ValueError
                valid_move=True
            except ValueError:
                print("Invalid square. Try again")
                os.system("clear")
                continue
        return self.humanMove
    def __str__(self):
        return f"{self.letter} object."


#Random computer player spesific
class RandomCompPlayer(Player):
    def __init__(self):
        super().__init__(letter)
    def get_move(self):
        pass