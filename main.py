import random
from bracket import Bracket

def create_player(player_list):
    return[Player(p) for p in player_list]

def create_bracket(players):
    plr_len = len(players)
    std = [Bracket('Standard',str(i + 1)) for i in range(0,plr_len - 1)]
    lsr = [Bracket('Loser',str(i + 1)) for i in range(0,plr_len - 2)]
    fnl = [Bracket('Final',str(i + 1)) for i in range(0,2)]
    
    return std,lsr,fnl

def win_match(winner,bracket_list):
    std,lsr,fnl = bracket_list
    loser = 'TBD'
    s_updated = False
    l_updated = False
    f_updated = False
    for s in std:
        if s_updated:
            for g in std:
                if 'TBD' in g.get_players():
                    g.add_player(winner)
                    break
            for l in lsr:
                if 'TBD' in l.get_players():
                    l.add_player(loser)
                    break
            return True
        elif winner in s.get_players() and 'TBD' not in s.get_players() and '-' in s.get_results():
            for player in s.get_players():
                if player != winner:
                    loser = player
            s.win_player(winner)
            s.lose_player(loser)
            s_updated = True
    if s_updated:
        for l in lsr:
            if 'TBD' in l.get_players():
                l.add_player(loser)
                print('added',loser,l.name,l.match)
                break
        final[0].add_player(winner)
        s_updated = False

    for l in lsr:
        if l_updated:
            l.add_player(winner)
            return True
        elif winner in l.get_players() and 'TBD' not in l.get_players() and '-' in l.get_results():
            for player in l.get_players():
                if player != winner:
                    loser = player
            l.win_player(winner)
            l.lose_player(loser)
            l_updated = True
    if l_updated:
        for f in fnl:
            f.add_player(winner)
            break
        final[0].add_player(winner)
        s_updated = False
        return True
        
    for f in fnl:
        if f_updated:
            final[1].add_player(winner)
            final[1].add_player(loser)
            return True
        elif winner in f.get_players() and 'TBD' not in f.get_players() and '-' in f.get_results():
            for player in f.get_players():
                if player != winner:
                    loser = player
            if f.match == '1' and f.get_players()[0] == winner:
                f.win_player(winner)
                f.lose_player(loser)
                print(f'------------Game over {winner} won the whole tournament')
                return False
            elif f.match == '2':
                f.win_player(winner)
                f.lose_player(loser)
                print(f'------------Game over {winner} won the whole tournament')
                return False
            else:
                f.win_player(winner)
                f.lose_player(loser)
                f_updated = True
    return True
                
players = ['Keegan','Mitch','Daryn','William','Felisha','Jordan','Drew','Mark'] # 'William','Felisha','Jordan','Drew','Mark'
#players = ['Keegan','Mitch','Daryn'] # 'William','Felisha','Jordan','Drew','Mark'
#random.shuffle(player_list) #shuffle list of players
'''players = create_player(player_list) # create player object'''

standard,loser,final = create_bracket(players) # create bracket objects

# populate standard bracket with players
for key,p in enumerate(players):
    standard[int(key / 2)].add_player(p)


for i in range(0,3):
    print()

#print brackets
for s in standard:
    print(s.layout)
for l in loser:
    print(l.layout)
for f in final:
    print(f.layout)

#spacing
for i in range(0,3):
    print()
        
test = True
while test:
#spacing

    result = input('Who won?\n')
    if result == 'quit':
        break
    test = win_match(result,[standard,loser,final])
    
    for i in range(0,3):
        print()

    #print brackets
    for s in standard:
        print(s.layout)
    for l in loser:
        print(l.layout)
    for f in final:
        print(f.layout)

    #spacing
    for i in range(0,3):
        print()
#win_match(players[2],[standard,loser,final])
# standard[0].win_player(players[0])
# standard[0].lose_player(players[1])
