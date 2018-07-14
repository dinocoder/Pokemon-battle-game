import random
import requests
import json
import math
import re
from player import Player
from pokemon import Pokemon
import playerTeams
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
  
  
  def __init__(self):
    #unused data goes here
  
  
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

  
  
