import random
from new_bracket import Bracket

def player_split(player_list):
    half = len(player_list) // 2
    return player_list[half:],player_list[:half]

def add_players(matches,player_list,i):
    for m in matches:
        p = random.choice(player_list)
        m.players[i] = p
        player_list.remove(p)
        if player_list == []:
            break
player_list = ['Daryn','Keegan','Mitch','William','Danyl']
home,away = player_split(player_list)
matches = [Bracket('Match') for i in range(0,len(player_list) - 1)]

add_players(matches,home,0)
add_players(matches,away,1)
    
for m in matches:
    print(m.match,m.players)