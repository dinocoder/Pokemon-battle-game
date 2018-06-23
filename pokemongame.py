import random
import requests
import json
import math
import re
from player import Player
from pokemon import Pokemon
player1pokemondata = []
player1pokemon = []
player1PokemonStats = []
#test = re.compile('[a-z]+')
#print(test.match('tempo'))

# hpmodifier1 = re.compile('\d+(?=\sHP)+')
 
'''
\d+(?=\sHP)+
\d+(?=\sAtk)+
\d+(?=\sDef)+
\d+(?=\sSpA)+
\d+(?=\sSpD)+
\d+(?=\sSpe)+
 
'''
player1data = """Alakazam-Mega @ Alakazite  
Ability: Synchronize  
EVs: 4 Atk / 252 SpA / 252 Spe  
Hasty Nature  
- Calm Mind  
- Dazzling Gleam  
- Drain Punch  
- Energy Ball  

Chansey @ Eviolite  
Ability: Natural Cure  
EVs: 248 HP / 8 Atk / 252 Def  
Relaxed Nature  
- Brick Break  
- Drain Punch  
- Fire Blast  
- Counter  

Salamence @ Choice Specs  
Ability: Beast Boost  
EVs: 4 Atk / 252 SpA / 252 Spe  
Hasty Nature  
IVs: 30 Atk  
- Hidden Power [Electric]  
- Fire Blast  
- Explosion  
- Heat Wave  

Heatran @ Life Orb  
Ability: Flash Fire  
EVs: 4 Atk / 252 SpA / 252 Spe  
Hasty Nature  
- Earthquake  
- Flash Cannon  
- Dragon Pulse  
- Flame Charge  

Garchomp @ Choice Specs  
Ability: Sand Veil  
EVs: 4 Atk / 252 SpA / 252 Spe  
Naive Nature  
- Crunch  
- Earthquake  
- Fire Blast  
- Dragon Pulse  

Hawlucha @ Berry Juice  
Ability: Limber  
EVs: 252 Atk / 4 SpA / 252 Spe  
Naughty Nature  
IVs: 30 Atk  
- Agility  
- Hidden Power [Fire]  
- Fire Punch  
- Defog  
"""
player2data='''
Clefable (F) @ Life Orb  
Ability: Cute Charm  
Level: 1  
Shiny: Yes  
Happiness: 54  
EVs: 116 Atk / 28 SpA / 196 Spe  
Lonely Nature  
IVs: 3 HP / 3 Atk / 3 Def / 3 SpA / 3 SpD / 3 Spe  
- Dazzling Gleam  
- Drain Punch  
- Facade  
- Body Slam

Chansey @ Eviolite  
Ability: Natural Cure  
EVs: 248 HP / 8 Atk / 252 Def  
Relaxed Nature  
- Brick Break  
- Drain Punch  
- Fire Blast  
- Counter 

Blissey @ Choice Specs  
Ability: Beast Boost  
EVs: 4 Atk / 252 SpA / 252 Spe  
Hasty Nature  
IVs: 30 Atk  
- Hidden Power [Electric]  
- Fire Blast  
- Explosion  
- Heat Wave  

Heatran @ Life Orb  
Ability: Flash Fire  
EVs: 4 Atk / 252 SpA / 252 Spe  
Hasty Nature  
- Earthquake  
- Flash Cannon  
- Dragon Pulse  
- Flame Charge  

Garchomp @ Choice Specs  
Ability: Sand Veil  
EVs: 4 Atk / 252 SpA / 252 Spe  
Naive Nature  
- Crunch  
- Earthquake  
- Fire Blast  
- Dragon Pulse  

Hawlucha @ Berry Juice  
Ability: Limber  
EVs: 252 Atk / 4 SpA / 252 Spe  
Naughty Nature  
IVs: 30 Atk  
- Agility  
- Hidden Power [Fire]  
- Fire Punch  
- Defog
'''

#get information from api

#split data for each pokemon

#print (len(player1data))
a=0
pokedex_seen = []
pokedex_caught = []
effectiveness = []

attacktype = {'normal': [1,2,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1], 'fighting': [1,1,2,1,1,0.5,0.5,1,1,1,1,1,1,2,1,1,0.5,2], 'flying': [1,0.5,1,1,0,2,0.5,1,1,1,1,0.5,2,1,2,1,1,1], 'poison': [1,0.5,1,0.5,2,1,0.5,1,1,1,1,0.5,1,2,1,1,1,0.5], \
              'ground': [1,1,1,0.5,1,0.5,1,1,1,1,2,2,0,1,2,1,1,1], 'rock': [0.5,2,0.5,0.5,2,1,1,1,2,0.5,2,2,1,1,1,1,1,1], 'bug': [1,0.5,2,1,0.5,2,1,1,1,2,1,0.5,1,1,1,1,1,1], 'ghost': [0,0,1,0.5,1,1,0.5,2,1,1,1,1,1,1,1,1,2,1], \
              'steel': [0.5,2,0.5,0,2,0.5,0.5,1,0.5,2,1,0.5,1,0.5,0.5,0.5,1,0.5], 'fire': [1,1,1,1,2,2,0.5,1,0.5,2,2,0.5,1,1,0.5,1,1,0.5], 'water': [1,1,1,1,1,1,1,1,0.5,0.5,0.5,2,2,1,0.5,1,1,1], \
              'grass': [1,1,2,2,0.5,1,2,1,1,2,0.5,0.5,0.5,1,2,1,1,1], 'electric': [1,1,0.5,1,2,1,1,1,0.5,1,1,1,0.5,1,1,1,1,1], 'psychic': [1,0.5,1,1,1,1,2,2,1,1,1,1,1,0.5,1,1,2,1], 'ice': [1,2,1,1,1,2,1,1,2,2,1,1,1,1,0.5,1,1,1], \
              'dragon': [1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,1,2,2,1,2], 'dark': [1,2,1,1,1,1,2,0.5,1,1,1,1,1,0,1,1,0.5,2], 'fairy': [1,0.5,1,2,1,1,0.5,1,2,1,1,1,1,1,1,0,0.5,1]}

defensetype = {'normal': 0, 'fighting': 1, 'flying': 2, 'poison': 3, 'ground': 4, 'rock': 5, 'bug': 6, 'ghost': 7, 'steel': 8, 'fire': 9, 'water': 10, 'grass': 11, 'electric': 12, 'psychic': 13, 'ice': 14, \
              'dragon': 15, 'dark': 16, 'fairy': 17}

computerpokemonabilities = []
mudkipabilities = []
getdata = re.compile('.+?(?=\s@|\s\()')

#Extracts evs
#Make one for IVs




#print(player1data)
#print(getdata.findall(player1data[0])[0].lower())
#print(getdata.findall(player1data[1])[0].lower())



#Add something for player 2
#Gets pokemon stat data



randompokemon = random.randint(1, 802)
computerpokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(randompokemon) + '/')
computerpokemondata = computerpokemon.json()





class pokemonstats:

  player1 = Player(player1data)
  player2 = Player(player2data)

  print(player1.playerPokemonStats)
  print(player2.playerPokemonStats)  
  
  
  def __init__(self):
    
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
  
  
def multiplier(pokemonType, opponentType, chosenMove, pokemonstats):
  #move type and stab multipliers here
  multiplier = 1
  typematchup = 1
  extratext = ""
  #type matchups
  for i in opponentType:
    typematchup *= (attacktype[i][pokemonstats.movetypes[chosenMove]])
    
  multiplier *= typematchup

    
  multiplier *= (random.randint(0, 15) / 100) + .85

  if typematchup > 1:
    extratext = "It's super effective!"
  elif typematchup < 1:
    extratext = "It's not very effective..."
  
  #STAB bonus
  counter = 0
  for k in pokemonType:
    if pokemonstats.movetypes[chosenMove] == defensetype[pokemonType[counter]]:
      multiplier *= 1.5
      counter += 1
      break
  else:
    counter += 1

  #Item bonus
    if pokemonstats.mudkipitem == 'Life Orb':
      multiplier *= 1.3
    #elif pokemonstats.mudkipItem == 'Choice Band'
    
  
  
  return multiplier, extratext



name = input('Enter your name')
opponentname = 'placeholder'
#yourpokemondata = input('Enter your team data')

mypokemon = yourpokemondata.split('\n\n')
print(len(mypokemon))
pokemonname = yourpokemondata
#pokemonstats =


def attack(pokemonstats):
  computermoves(computerpokemondata, defensetype,pokemonstats1)
  extratext = ''
  extratext2 = ''
  print('A wild ' + pokemonstats.computerpokemonname + ' appeared!')
  while pokemonstats.mudkiphp > 0 and pokemonstats.computerpokemonhp > 0:
    pokemonstats.a = 1
    print('What will Mudkip do?\n')
    print(pokemonstats.mudkipmoves)
    while pokemonstats.a == 1:
      chosenmove = input()
      try:
        mudkipbasepower = pokemonstats.mudkipmoves2[str(chosenmove)]
        pokemonstats.a = 0
      except:
        print('Enter a valid move')
        pokemonstats.a = 1
        break
      

    multiplierResult =  multiplier(pokemonstats.mudkiptype, pokemonstats.computerpokemontype, chosenmove, pokemonstats)
    pokemonstats.mudkipmultiplier = multiplierResult[0]
    #damage algorithm
    mudkipdamage = ((((2 * pokemonstats.mudkiplevel / 5) + 2) * mudkipbasepower * pokemonstats.mudkipattack / pokemonstats.computerpokemondefense / 50) + 2) * pokemonstats.mudkipmultiplier
    pokemonstats.computerpokemonhp -= mudkipdamage
    extratext = multiplierResult[1]
    print('Mudkip used ' + chosenmove + '!')
    print(extratext)


    if pokemonstats.computerpokemonhp <= 0:
        print(pokemonstats.computerpokemonname + ' has 0 HP left.')
    else:
        print(pokemonstats.computerpokemonname + ' has ' + str(math.floor(pokemonstats.computerpokemonhp / pokemonstats.fullcomputerpokemonhp * 100)) + '% HP left.')
    typematchup = 1



    
    if pokemonstats.computerpokemonhp >= 0:
      computerpokemonchosenmove = random.choice(pokemonstats.computerpokemonmoves)
      computerpokemonbasepower = pokemonstats.computerpokemonmoves2[computerpokemonchosenmove]

      computertypematchup = 1

    multiplierResult2 =  multiplier(pokemonstats.computerpokemontype, pokemonstats.mudkiptype, computerpokemonchosenmove, pokemonstats)

    pokemonstats.computerpokemonmultiplier = multiplierResult2[0]
    computerpokemondamage = ((((2 * pokemonstats.computerpokemonlevel / 5) + 2) * computerpokemonbasepower * pokemonstats.computerpokemonattack / pokemonstats.mudkipdefense / 50) + 2) * pokemonstats.computerpokemonmultiplier
    pokemonstats.mudkiphp -= computerpokemondamage
    print('The opposing ' + pokemonstats.computerpokemonname + ' used ' + computerpokemonchosenmove + '!')
    extratext = multiplierResult2[1]
    print(extratext)
    print(extratext2)
    if pokemonstats.mudkiphp <= 0:
        print('Mudkip has 0 HP left.')
    else:
        print('Mudkip has ' + str(math.floor(pokemonstats.mudkiphp)) + ' (' + str(math.floor(pokemonstats.mudkiphp / pokemonstats.mudkipfullhp * 100)) + '%) ' + 'HP left.')




      
  if pokemonstats.mudkiphp > pokemonstats.computerpokemonhp:
      print('You won!')
  else:
      print('You Lost!')
  for i in pokedex_seen:
      if i == pokemonstats.computerpokemonname:
          notseen = False
      if notseen:  
        pokedex_seen.append(pokemonstats.computerpokemonname)
    
print('You are on an island with a Mudkip that you found that seems to like you.')
print('But soon you realize you are stuck with nothing except a bunch of wild Pokemon around.')
print('It seems you need to train your pokemon to find a way off the island.')
continuegame = input('Do you want to continue?')
if continuegame == 'yes':
  print('Ok, great choice!')
else:
  print('Oh no, your Mudkip ran off and drew attention to some wild Pokemon!')


  
pokemonstats1 = pokemonstats()
attack(pokemonstats1)

print('What do you want to do?\n')
print('View Pokedex')
action = input()
if action == 'View Pokedex':
  print ('Seen:\n' + str(pokedex_seen))
  print ('\nCaught:\n' + str(pokedex_caught))
  

'''if mudkipability2 == 'torrent' and pokemonstats.mudkiphp / pokemonstats.mudkipfullhp <= (1/3) and movetypes[chosenmove] == 10:
      pokemonstats.mudkipmultiplier += 1.3
  else:
      pokemonstats.mudkipmultiplier = 1
'''

  
  
