import random
import math
import game as game

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
                self.humanMove = int(input("Bir hamle yapınız [0-8]: "))
                
                if not self.humanMove in t.check_available():
                    raise ValueError
                valid_move=True
            except ValueError:
                print("Invalid square. Try again")
                continue
        return self.humanMove



#Random computer player spesific
class RandomCompPlayer(Player):
    def __init__(self):
        super().__init__(letter)
    def get_move(self):
        pass