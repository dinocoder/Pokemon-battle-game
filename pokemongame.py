import random
import requests
import json
import math
import re
from player import Player
from pokemon import Pokemon
import playerTeams
import socket
from termcolor import cprint

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
player1data = playerTeams.player1data
player2data = playerTeams.player2data

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
  
  '''
  def __init__(self):
    #unused data goes here
  '''

def multiplier(pokemonType, opponentType, move, pokemonstats):
  
  #move type and stab multipliers here
  multiplier = 1
  typematchup = 1
  extratext = ""
  #type matchups
  for i in opponentType:
    typematchup *= (attacktype[i][move.type])
    
  multiplier *= typematchup

    
  multiplier *= (random.randint(0, 15) / 100) + .85

  if typematchup > 1:
    extratext = "It's super effective!"
  elif typematchup < 1:
    extratext = "It's not very effective..."
  
  #STAB bonus
  counter = 0
  for k in pokemonType:
    if move.type == defensetype[opponentType[counter]]:
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

def calculateDamage(move, multiplier, attackingPokemon, defendingPokemon):
  if move.designation == 'physical':
    usedAttack = 'Attack'
    usedDefense = 'Defense'
  else:
    usedAttack = 'specialAttack'
    usedDefense = 'specialDefense'

  multiplierResult =  multiplier(attackingPokemon.type, defendingPokemon.type, move, pokemonstats)
    
  damage = ((((2 * sttackingPokemon.level / 5) + 2) * move['power'] * attackingPokemon.pokemonActiveStats[usedAttack] / defendingPokemon.pokemonactiveStats[usedDefense] / 50) + 2) * multiplier

  return damage 


name = input('Enter your name')
opponentname = 'placeholder'
#yourpokemondata = input('Enter your team data')
'''
mypokemon = yourpokemondata.split('\n\n')
print(len(mypokemon))
pokemonname = yourpokemondata
#pokemonstats =
'''

def attack(pokemonstats):
  extratext = ''
  extratext2 = ''
  print('A challenger approaches!')
  print('Who will you send out first?')

  playerPokemonList = '\n'
  for i in pokemonstats.player1.pokemonNames:
    playerPokemonList += (i + '    ')
  print(playerPokemonList + '\n')
  print('Choose a Pokemon!/nType "data <Pokemon Name> to see all info about it')
  chosenPokemonName = input()

  chosenPokemon2 = random.choice(player2.playerPokemonStats)

  for i in pokemonstats.player1.playerPokemonStats:
    if i.name == chosenPokemonName:
      chosenPokemon = i
      break
    
  
  while chosenPokemon.hp > 0 and chosenPokemon2.hp > 0:
    print('What will ' + chosenPokemon.name + ' do? Type "switch" to switch out.\n')
    for i in chosenPokemon.moves:
      print(i.name)

    chosenMove = input()
    chosenMove2 = random.choice(player2.moves)

    if chosenMove['priority'] > chosenMove2['priority']:
      moveFirst = 'player1'
    else if chosenmove['priority'] < chosenmon2['priority']:
      moveFirst = 'player2'
    else:
      if chosenPokemon.pokemonActiveStats['speed'] == chosenPokemon2.pokemonActiveStats['speed']:
        moveFirst = random.choice('player1', 'player2')
      else if chosenPokemon.pokemonActiveStats['speed'] > chosenPokemon2.pokemonActiveStats['speed']:
        moveFirst = 'player1'
      if chosenPokemon.pokemonActiveStats['speed'] < chosenPokemon2.pokemonActiveStats['speed']:
        moveFirst = 'player2'

    
    
    
    #damage algorithm
    if moveFirst = 'player1':
      attackingPokemon = chosenPokemon
      defendingPokemon = chosenPokemon2
      calculateDamage(chosenMove, multiplierResult[0], chosenPokemon, chosenPokemon2)
    else:
      attackingPokemon = chosenPokemon
      defendingPokemon = chosenPokemon2
      calculateDamage(chosenMove, multiplierResult[0], chosenPokemon, chosenPokemon2)
      
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

  
pokemonstats1 = pokemonstats()
attack(pokemonstats1)



  
  
