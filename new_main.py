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

# def create_tier(bracket_len):
    # var = 1
    # tier = []
    # for i in range(0,bracket_len):
        # for v in range(0,var):
            # tier.append(var)
        # if var >= 2:
            # var = var * 2
        # else:
            # var += 1
    # tier.reverse()
    # return tier[bracket_len:]
    
# b = [['','Dar','Will'],['','Keeg','Mitch'],['','','Fel'],['','','']]
# tier = create_tier(len(b))



# for key,i in enumerate(b):
    # i[0] = tier[key]

# print(b)
            
player_list = ['Daryn','Keegan','Mitch','William','Danyl']
home,away = player_split(player_list)
matches = [Bracket('Match') for i in range(0,len(player_list) - 1)]

add_players(matches,home,0)
add_players(matches,away,1)
    
for m in matches:
    print(m.match,m.players)