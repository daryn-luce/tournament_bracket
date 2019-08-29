import random

def create_bracket(players):
    standard = {}
    loser = {}
    final = {}
    for i in range(0,players -1):
        standard.update({f'Game{i + 1}':{'name':['TBD','TBD'],'result':['-','-']}})
    
    for i in range(players,(players * 2) - 2):
        loser.update({f'Loser{(i + 1) - players}':{'name':['TBD','TBD'],'result':['-','-']}})
    
    final.update({f'Final{i - players}':{'name':['TBD','TBD'],'result':['-','-']}})
    final.update({f'Final{i - players + 1}':{'name':['TBD','TBD'],'result':['-','-']}})
    
    return [standard,loser,final]

def add_player_list(bracket,player_list):
    temp_list = list(player_list)
    for game in bracket:
        for i in range(1,-1,-1):
            if bracket[game]['name'][i] == 'TBD':
                player = random.choice(temp_list)
                temp_list.remove(player)
                bracket[game]['name'][i] = player
            if len(temp_list) < 1:
                return

def add_player(bracket,plr):
    if isinstance(plr,list):
        temp_list = list(player_list)
    elif isinstance(plr,str):
        player = plr
    for game in bracket:
        for i in range(1,-1,-1):
            if bracket[game]['name'][i] == 'TBD':
                if isinstance(plr,list):
                    player = random.choice(temp_list)
                    temp_list.remove(player)
                    bracket[game]['name'][i] = player
                    if len(temp_list) < 1:
                        return
                elif isinstance(plr,str):
                    bracket[game]['name'][i] = player
                    return



def win(bracket,player):
    # last_game = 'Game' + str(len(bracket.keys()))
    # print(last_game)
    for game in bracket:
        if bracket[game]['result'][0] == '-':
            if bracket[game]['name'][0] == player and bracket[game]['name'][1] != 'TBD':
                bracket[game]['result'][0] = 1
                bracket[game]['result'][1] = 0
                return bracket[game]['name'][1]
            elif bracket[game]['name'][1] == player and bracket[game]['name'][0] != 'TBD':
                bracket[game]['result'][1] = 1
                bracket[game]['result'][0] = 0
                return bracket[game]['name'][0]
    
def player_win(bracket,player):
    standard,loser,final = bracket
    result = win(standard,player)
    std_game = 'Game' + str(len(standard))
    lsr_game = 'Loser' + str(len(loser))
    s_final = False
    l_final = False
    
    for game in standard:
        if game == std_game:
            if standard[game]['result'][0] != '-' and standard[game]['result'][1] != '-':
                s_final = True

    if result != None:
        if not s_final:
            add_player(standard,player)
            add_player(loser,result)
        else:
            add_player(final,player)
            add_player(loser,result)
        return
    else:
        result = win(loser,player)
        for game in loser:
            if game == lsr_game:
                if loser[game]['result'][0] != '-' and loser[game]['result'][1] != '-':
                    l_final = True
        if not l_final:
            add_player(loser,player)
        else:
            add_player(final,player)
        return
 


player_list = ['Keegan','Mitch','William','Daryn','Felisha','Jordan','Drew','Mark'] #

standard,loser,final = create_bracket(len(player_list))
add_player(standard,player_list)

test = True
while test:
    print('-----------------')
    for game in standard:
        print(game,standard[game]['name'],standard[game]['result'])
    for game in loser:
        print(game,loser[game]['name'],loser[game]['result'])
    for game in final:
        print(game,final[game]['name'],final[game]['result'])        
    print('-----------------')
    
    winner = input('Who won?\n')
    if winner == 'quit':
        test = False
    player_win([standard,loser,final],winner)
    


# add_player(bracket,player_list)
# player_win(bracket,player_list[3])

# for b in bracket:
    # print(b)

# # bracket = {
        # # 'Game1':{
            # # 'name':['Daryn','Mitch'],
            # # 'result':['1','0']
            # # },
        # # 'Game2':{
            # # 'name':['William','Keegan'],
            # # 'result':['-','-']
            # # },
        # # 'Game3':{
            # # 'name':['Felisha',''],
            # # 'result':['-','-']
            # # }
        
        # # }
# # bracket.update({f'Game{0 + 4}':{'name':['tba','tba'],'result':['-','-']}})

# # print(bracket['Game4']['name'][0])