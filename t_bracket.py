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


player_list = ['Keegan','Mitch','William','Daryn','Felisha']

bracket = create_bracket(len(player_list))

add_player(bracket,player_list)

for b in bracket:
    print(b)