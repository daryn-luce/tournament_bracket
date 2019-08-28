import random

def create_bracket(players):
    bracket = []
    for i in range(0,players):
        bracket.append([f'Game{i + 1}',['',''],['','']])
    
    for i in range(players,players + 2):
        bracket.append([f'Loser{(i + 1) - players}',['',''],['','']])
    
    bracket.append([f'LastFinal',['',''],['','']])
    
    return bracket

def add_player(bracket,player_list):
    temp_list = list(player_list)
    for match in bracket:
        if match[1][0] == '':
            player = random.choice(temp_list)
            temp_list.remove(player)
            match[1][0] = player
            if len(temp_list) < 1:
                break
        if match[2][0] == '':
            player = random.choice(temp_list)
            temp_list.remove(player)
            match[2][0] = player
            if len(temp_list) < 1:
                break

def player_win(bracket,player):
    winner = False
    for b in bracket:
        if b[1][0] == player and b[2][0] != '':
            b[1][1] = 1
            b[2][1] = 0
            loser_name = b[2][0]
        elif b[2][0] == player and b[1][0] != '':
            b[1][1] = 0
            b[2][1] = 1
            loser_name = b[1][0]
        if b[0][:-1] == 'Game':
            for i in range(len(b) -1,1,-1):
                if b[i][0] == '':
                    b[i][0] = player
                    winner = True
                    break
        if b[0][:-1] == 'Loser':
            for i in range(len(b) -1,1,-1):
                if b[i][0] == '':
                    b[i][0] = loser_name
                    break
        if winner:
            break

player_list = ['Keegan','Mitch','William','Daryn','Felisha']

bracket = create_bracket(len(player_list))

add_player(bracket,player_list)
player_win(bracket,player_list[3])

for b in bracket:
    print(b)