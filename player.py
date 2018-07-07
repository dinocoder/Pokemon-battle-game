from pokemon import Pokemon
import re
import requests

class Player:
    
    pokemonList = []
    
    
    def __init__(self, pokemonlist):

        self.playerPokemonStats = []
        pokemondata = []
        getdata = re.compile('.+?(?=\s@|\s\()')
        
        playerdata = pokemonlist.split('\n\n')
        for i in range(len(playerdata)):
          tempPokeData = playerdata[i]
          pokeName = getdata.findall(tempPokeData)[0].lower()
          pokeRequest = 'http://pokeapi.co/api/v2/pokemon/' + getdata.findall(tempPokeData)[0].lower() + '/'
          pokemondata.append(requests.get('http://pokeapi.co/api/v2/pokemon/' + getdata.findall(playerdata[i])[0].lower() + '/'))
        for i in range(len(playerdata)):
            self.pokemonList.append(pokemondata[i].json())

        for basePokemonStats in self.pokemonList:
            #Creates a pokemon using base stats and pokemon data
            try:
                myPokemonStats = playerdata[self.pokemonList.index(basePokemonStats)]
            except IndexError:
                break
            else:
                myPokemonStats = playerdata[self.pokemonList.index(basePokemonStats)]
                
            #print(myPokemonStats)
            self.playerPokemonStats.append(Pokemon(myPokemonStats, basePokemonStats))
        
        


        '''
        #Player 1 moves
        getmoves = re.compile('(?<=\-\s).+')
        move = []
        for i in range(len(playerdata)):
          tempPokeMoves = playerdata[i]
          move.append(getmoves.findall(tempPokeMoves))
          #add moves to class
          '''



    
