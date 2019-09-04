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
    
    def win_player(self,player):
        if self.players[0] == player:
            self.result = [1,0]
            self.winner,self.loser = players[0],players[1]
        elif self.players[1] == player:
            self.result = [0,1]
            self.winner,self.loser = players[1],players[0]
