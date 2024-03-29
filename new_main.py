import random
from new_bracket import Bracket

# Method to add players to the match 
def add_players(matches,player_list,max_tier):
    for m in matches:
        if m.tier == max_tier:
            t = random.choice(player_list)
            m.players[0] = t
            player_list.remove(t)
            t = random.choice(player_list)
            m.players[1] = t
            player_list.remove(t)

    for m in matches:
        if m.tier != max_tier:
            try:
                t = random.choice(player_list)
                m.players[0] = t
                player_list.remove(t)
            except IndexError:
                break

def move_player(matches,player):
    for m in matches:
        if m.winner == player and not m.moved:
            for j in matches:
                if j.tier < m.tier:
                    if j.players[0] == 'TBD':
                        print(f'**************Moving {player} to {j.match}')
                        j.players[0] = m.winner
                        m.moved = True
                        return True
                    elif j.players[1] == 'TBD':
                        print(f'**************Moving {player} to {j.match}')
                        j.players[1] = m.winner
                        m.moved = True
                        return True
            return False
def win_player(matches,player):
    print()
    print(f'**************Looking for {player}')
    for m in matches:
        
        if m.players[0] == player and not m.moved:
            print(f'**************Found {player}')
            m.result = [1,0]
            m.winner,m.loser = m.players[0],m.players[1]
            break
        elif m.players[1] == player and not m.moved:
            print(f'**************Found {player}')
            m.result = [0,1]
            m.winner,m.loser = m.players[1],m.players[0]
            break
    return move_player(matches,player)
            
def create_tier(bracket_len):
    var = 1
    tier = []
    for i in range(0,bracket_len):
        for v in range(0,var):
            tier.append(var)
        if var >= 2:
            var = var * 2
        else:
            var += 1
    tier = tier[:bracket_len - 1]
    tier.reverse()
    return tier
    

player_list = ['Daryn','Keegan','Mitch','William','Danyl','Felisha'] #,'Ryan','Mark','Jesse','Julio'
tier = create_tier(len(player_list))
matches = [Bracket('Match') for i in range(0,len(player_list) - 1)]

for key,m in enumerate(matches):
    m.tier = tier[key]
    

add_players(matches,player_list,max(tier))
    
for key,m in enumerate(matches):
    m.tier = tier[key]
    print(m.match,m.players,f'Tier: {m.tier}')



while True:
    temp = input('Who won?\n')
    if temp == 'quit':
        break
    win_player(matches,temp)
    for m in matches:
        print(m.match,m.players,m.result)