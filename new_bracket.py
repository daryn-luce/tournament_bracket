class Bracket():
    _counter = 0
    def __init__(self,name):
        Bracket._counter += 1
        self.name = name
        self.id = Bracket._counter
        self.match = self.name + str(self.id)
        self.players = ['TBD','TBD']
        self.result = ['-','-']
        self.winner = self.players[0]
        self.loser = self.players[0]
        self.tier = None
        self.moved = False
    
