'''
    self.movetypes = {'Tackle': 0, 'Water Gun': 10, 'Thunder Shock': 12}


    #player1 base stats
    #Add something to find level later
    self.player1level = [100, 100, 100, 100, 100, 100]
    self.computerpokemonlevel = 100

    
    #get base stats
    player1basehp = []
    player1baseattack = []
    player1basedefense = []
    player1basespAtk = []
    player1basespDef = []
    player1basespeed = []
    for i in player1data:
      self.player1basehp.append(i['stats'][1]['base_stat'])
      self.player1baseattack.append(i['stats'][2]['base_stat'])
      self.player1basedefense.append(i['stats'][3]['base_stat'])
      self.player1basespAtk.append(i['stats'][4]['base_stat'])
      self.player1basespDef.append(i['stats'][5]['base_stat'])
      self.player1basespeed.append(i['stats'][6]['base_stat'])

      #add something to find type
    for i in mudkipdata1['types']:
      self.mudkiptype.append(i['type']['name'])
      
    #player 2 base stats

    self.computerpokemonbaseattack = computerpokemondata['stats'][4]['base_stat']
    self.computerpokemonbasedefense = computerpokemondata['stats'][3]['base_stat']
    self.computerpokemonbasehp = computerpokemondata['stats'][5]['base_stat']
    self.computerpokemontype = []
    for i in computerpokemondata['types']:
      self.computerpokemontype.append(i['type']['name'])


    #player 2 active stats
    self.computerpokemonname = str(computerpokemondata['name'])
    self.computerpokemonname1 = self.computerpokemonname[0].upper()
    self.computerpokemonname2 = self.computerpokemonname[1:len(self.computerpokemonname)]
    self.computerpokemonname = self.computerpokemonname1 + self.computerpokemonname2
    self.computerpokemonattack = (2 * self.computerpokemonbaseattack * self.computerpokemonlevel) / 100 + self.computerpokemonlevel + 5
    self.computerpokemondefense = (2* self.computerpokemonbasedefense * self.computerpokemonlevel) / 100 + self.computerpokemonlevel + 5
    self.computerpokemonhp = ((2 * self.computerpokemonbasehp * self.computerpokemonlevel) / 100) + self.computerpokemonlevel + 10
    self.fullcomputerpokemonhp = ((2 * self.computerpokemonbasehp * self.computerpokemonlevel) / 100) + self.computerpokemonlevel + 10

    self.computerpokemonmoves = []
    self.computerpokemonmoves2 = {}
    self.computerpokemonmultipler = 1

    #player 1 active stats
    for i in player1pokemon:
      player1pokemon.setBaseStats(i, self.level, self.hpIV, self.AttackIV, self.defenseIV, self.specialAttackIV, self.specialDefIV, self.speedIV, self.hpEV, self.AttackEV, self.defenseEV, self.specialAttackEV, self.specialDefEV, self.speedEV)
    
    self.player1pokemon1evs = extractEVdata(player1data[0])
    print(self.player1pokemon1evs)
    self.mudkipattack = (2 * self.mudkipbaseattack * self.mudkiplevel) / 100 + self.mudkiplevel + 5
    self.mudkipdefense = (2 * self.mudkipbasedefense * self.mudkipbasedefense) / 100 + self.mudkiplevel + 5
    self.mudkiphp = (2 * self.mudkipbasehp * self.mudkiplevel) / 100 + self.mudkiplevel + 10
    self.mudkipfullhp = (2 * self.mudkipbasehp * self.mudkiplevel) / 100 + self.mudkiplevel + 10
    self.mudkipmoves = ['Tackle: 40 Power, 100% Accuracy', 'Water Gun: 40 Power']
    self.mudkipmoves2 = {'Tackle': 40, 'Water Gun': 40}
    self.mudkipmultiplier = 1

    self.mudkipitem = 'Life Orb'

    self.a = 1
'''

  ''' for i in range(len(computerpokemondata['abilities'])):
      self.computerpokemonability = computerpokemondata['abilities'][i]['ability']['name']
      self.computerpokemonabilities.append(pokemonstats.computerpokemonability)
    print(pokemonstats.computerpokemonabilities)
    for i in range(len(mudkipdata1['abilities'])):
      self.mudkipability = mudkipdata1['abilities'][i]['ability']['name']
      self.mudkipabilities.append(pokemonstats.mudkipability)
    print(self.mudkipabilities)

    self.mudkipmoves = ['Tackle: 40 Power, 100% Accuracy', 'Water Gun: 80 Power']
    self.mudkipmoves2 = {'Tackle': 40, 'Water Gun': 80}


    self.mudkipability2 = random.choice(mudkipabilities)
    print(self.mudkipability2)
    '''

    

def computermoves(computerpokemondata, defensetype,pokemonstats1):
    
    possiblemoves = []
    usedmoveurls = []
    computermoves = computerpokemondata['moves']
    for i in range(len(computerpokemondata['moves'])):
      if len(usedmoveurls) < 4:
        if computerpokemondata['moves'][i]['version_group_details'][0]['move_learn_method']['name'] == 'level-up':
            #possiblemoves.append(computerpokemondata['moves'][i]['move']['url'])
            possiblemoves = requests.get(computerpokemondata['moves'][i]['move']['url']).json()
            if possiblemoves['power']!= None:
              usedmoveurls.append(computerpokemondata['moves'][i]['move']['url'])


        
    computerslot1 = requests.get(usedmoveurls[0]).json()
    computerslot2 = requests.get(usedmoveurls[1]).json()
    computerslot3 = requests.get(usedmoveurls[2]).json()
    computerslot4 = requests.get(usedmoveurls[3]).json()
    for k in range(len(computerslot1['names'])):
        if computerslot1['names'][k]['language']['name'] == 'en':
              computerslot1name = computerslot1['names'][k]['name']
              
    for k in range(len(computerslot2['names'])):
         if computerslot2['names'][k]['language']['name'] == 'en':
           computerslot2name = computerslot2['names'][k]['name']

    for k in range(len(computerslot3['names'])):
         if computerslot3['names'][k]['language']['name'] == 'en':
           computerslot3name = computerslot3['names'][k]['name']

    for k in range(len(computerslot4['names'])):
         if computerslot4['names'][k]['language']['name'] == 'en':
           computerslot4name = computerslot4['names'][k]['name']

              

    
            
    computerslot1power = computerslot1['power']
    computerslot2power = computerslot2['power']
    computerslot3power = computerslot3['power']
    computerslot4power = computerslot4['power']

    computerslot1type = defensetype[computerslot1['type']['name']]
    computerslot2type = defensetype[computerslot2['type']['name']]
    computerslot3type = defensetype[computerslot3['type']['name']]
    computerslot4type = defensetype[computerslot4['type']['name']]
    pokemonstats1.computerpokemonmoves = [computerslot1name, computerslot2name, computerslot3name, computerslot4name]
    
    
    pokemonstats1.computerpokemonmoves2[computerslot1name] = computerslot1power
    pokemonstats1.computerpokemonmoves2[computerslot2name] = computerslot2power
    pokemonstats1.computerpokemonmoves2[computerslot3name] = computerslot3power
    pokemonstats1.computerpokemonmoves2[computerslot4name] = computerslot4power

    pokemonstats1.movetypes[computerslot1name] = computerslot1type
    pokemonstats1.movetypes[computerslot2name] = computerslot2type
    pokemonstats1.movetypes[computerslot3name] = computerslot3type
    pokemonstats1.movetypes[computerslot4name] = computerslot4type


def playermoves(mudkipdata, defensetype,pokemonstats1):
    
    possiblemoves = []
    usedmoveurls = []
    mudkipmoves = mudkipdata['moves']
    for i in range(len(mudkipdata['moves'])):
      if len(usedmoveurls) < 4:
        if mudkipdata['moves'][i]['version_group_details'][0]['move_learn_method']['name'] == 'level-up':
            #possiblemoves.append(mudkipdata['moves'][i]['move']['url'])
            possiblemoves = requests.get(mudkipdata['moves'][i]['move']['url']).json()
            if possiblemoves['power']!= None:
              usedmoveurls.append(mudkipdata['moves'][i]['move']['url'])


        
    mudkipslot1 = requests.get(usedmoveurls[0]).json()
    mudkipslot2 = requests.get(usedmoveurls[1]).json()
    mudkipslot3 = requests.get(usedmoveurls[2]).json()
    mudkipslot4 = requests.get(usedmoveurls[3]).json()
    for k in range(len(mudkipslot1['names'])):
        if mudkipslot1['names'][k]['language']['name'] == 'en':
              mudkipslot1name = mudkipslot1['names'][k]['name']
              
    for k in range(len(mudkipslot2['names'])):
         if mudkipslot2['names'][k]['language']['name'] == 'en':
           mudkipslot2name = mudkipslot2['names'][k]['name']

    for k in range(len(mudkipslot3['names'])):
         if mudkipslot3['names'][k]['language']['name'] == 'en':
           mudkipslot3name = mudkipslot3['names'][k]['name']

    for k in range(len(mudkipslot4['names'])):
         if mudkipslot4['names'][k]['language']['name'] == 'en':
           mudkipslot4name = mudkipslot4['names'][k]['name']

              

    
            
    mudkipslot1power = mudkipslot1['power']
    mudkipslot2power = mudkipslot2['power']
    mudkipslot3power = mudkipslot3['power']
    mudkipslot4power = mudkipslot4['power']

    mudkipslot1type = defensetype[mudkipslot1['type']['name']]
    mudkipslot2type = defensetype[mudkipslot2['type']['name']]
    mudkipslot3type = defensetype[mudkipslot3['type']['name']]
    mudkipslot4type = defensetype[mudkipslot4['type']['name']]
    pokemonstats1.mudkipmoves = [mudkipslot1name, mudkipslot2name, mudkipslot3name, mudkipslot4name]
    
    
    pokemonstats1.mudkipmoves2[mudkipslot1name] = mudkipslot1power
    pokemonstats1.mudkipmoves2[mudkipslot2name] = mudkipslot2power
    pokemonstats1.mudkipmoves2[mudkipslot3name] = mudkipslot3power
    pokemonstats1.mudkipmoves2[mudkipslot4name] = mudkipslot4power

    pokemonstats1.movetypes[mudkipslot1name] = mudkipslot1type
    pokemonstats1.movetypes[mudkipslot2name] = mudkipslot2type
    pokemonstats1.movetypes[mudkipslot3name] = mudkipslot3type
    pokemonstats1.movetypes[mudkipslot4name] = mudkipslot4type

