import json
from backpack import Backpack

class Game(object):
    """docstring for Game."""
    def __init__(self,filename):
        self.text = self.load_game_test(filename)
        self.backpack = Backpack()

        self.starting_text()

    def load_game_test(self,filename):
        print('Starting game from: {}'.format(filename))
        with open(filename,'r') as f:
            return json.load(f)

    def starting_text(self):
        # TODO: self.text['Description']
        pass
