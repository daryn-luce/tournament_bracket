# class Player():
    # def __init__(self,name):
        # self.name = name
        # self.match = None
        # self.win = 0
        # self.loss = 0
        
    # def add_win(self):
        # self.win += 1
        
    # def add_loss(self):
        # self.loss += 1
        
    # def set_match(self,match):
        # self.match = match

class Bracket():
    def __init__(self,name,match):
        self.name = name
        self.match = match
        self.p1 = 'TBD'
        self.p2 = 'TBD'
        self.p1r = '-'
        self.p2r = '-'
        self.layout = {}
        self.update_layout()
        
    def update_layout(self):
        self.layout.update({self.name + self.match:{'name':[self.p1,self.p2],'result':[self.p1r,self.p2r]}})

    def add_player(self,player):
        if self.p1 == 'TBD':
            self.p1 = player
        elif self.p2 == 'TBD':
            self.p2 = player
        self.update_layout()
    
    def win_player(self,player):
        if self.p1 == player:
            self.p1r = 1
        elif self.p2 == player:
            self.p2r = 1
        self.update_layout()

    def lose_player(self,player):
        if self.p1 == player:
            self.p1r = 0
        elif self.p2 == player:
            self.p2r = 0
        self.update_layout()
        
    def get_players(self):
        return self.p1,self.p2
        
    def get_results(self):
        return self.p1r,self.p2r