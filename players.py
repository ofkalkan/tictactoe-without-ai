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
                print(f"Invalid square. Try again. (Available moves: {t.available_moves()}")
                continue
        return self.humanMove

    #Print object's name.    
    def __str__(self):
        return f"{self.letter} player."


#Random computer player spesific
class RandomCompPlayer(Player):
    def __init__(self):
        #super().__init__(letter)
        pass
    def get_move(self):
        pass