import re
import requests


class Pokemon:
    
    def setBaseStats(self, isHP, baseStat, natureModifier, statIV, statEV, level):
        #Determines effective stat
        if isHP:
            effectiveStat = int(round(((2 * baseStat + statIV + int(round((int(statEV))) / 4)) * level) / 100) + level + 10)
        else:
            effectiveStat = int(round(((((2 * baseStat + statIV + int(round(int(statEV))) / 4)) * level) / 100) + 5) * natureModifier)
        return effectiveStat
          

    def extractEVdata(self, rawpokemondata, dataType):
            #determine the type of data
            if dataType == "EV":
                findstatdata = re.compile('(?:EVs:).+')
                print(rawpokemondata)
                statdata = findstatdata.findall(rawpokemondata)[0]
                notreq = 0
            else:
                findstatdata = re.compile('(?:IVs:).+')
                try:
                    statdata = findstatdata.findall(rawpokemondata)[0]
                except:
                    notreq = 31
                    statdata = ''
                else:
                    statdata = findstatdata.findall(rawpokemondata)[0]
                    notreq = 0


            
            #determine hp data
            hpmodifier1 = re.compile('\d+(?=\sHP)')
            playerhp = int(hpmodifier1.findall(statdata)[0]) if len(hpmodifier1.findall(statdata)) > 0 else notreq
            
            #determine attack data
            atkmodifier1 = re.compile('\d+(?=\sAtk)')
            playeratk = int(atkmodifier1.findall(statdata)[0]) if len(atkmodifier1.findall(statdata)) > 0 else notreq

            #determine spAtk data
            spAtkmodifier1 = re.compile('\d+(?=\sSpA)')
            playerspAtk = int(spAtkmodifier1.findall(statdata)[0]) if len(spAtkmodifier1.findall(statdata)) > 0 else notreq

            #determine def data
            defmodifier1 = re.compile('\d+(?=\sDef)')
            playerdef = int(defmodifier1.findall(statdata)[0]) if len(defmodifier1.findall(statdata)) > 0 else notreq

            #determine spDef data
            spDefmodifier1 = re.compile('\d+(?=\sSpD)')
            playerspDef = int(spDefmodifier1.findall(statdata)[0]) if len(spDefmodifier1.findall(statdata)) > 0 else notreq

            #determine speed data
            speedmodifier1 = re.compile('\d+(?=\sSpe)')
            playerspeed = int(speedmodifier1.findall(statdata)[0]) if len(speedmodifier1.findall(statdata)) > 0 else notreq

            return [playerhp, playeratk, playerspAtk, playerdef, playerspDef, playerspeed]


    def getLevel(self, rawpokemondata):
        findlevel = re.compile('(?:Level: ).+')

        try:
            test = int(findlevel.findall(rawpokemondata)[0])
        except:
            return 100
        else:
            return findlevel.findall(rawpokemondata)[0]

    def getNature(self, rawpokemondata):
        findNature = re.compile('\w+(?=\sNature)')
        #Find nature not working
        nature = re.findall('\w+(?=\sNature)', rawpokemondata)[0]
        natureModifier = {'hp': 1.0, 'attack': 1.0, 'defense': 1.0, 'specialAttack': 1.0, 'specialDefense': 1.0, 'speed': 1.0}
        
        if nature == 'Lonely':
            natureModifier['attack'] = 1.1
            natureModifier['defense'] = 0.9
        elif nature == 'Brave':
            natureModifier['attack'] = 1.1
            natureModifier['speed'] = 0.9
        elif nature == 'Adamant':
            natureModifier['attack'] = 1.1
            natureModifier['specialAttack'] = 0.9
        elif nature == 'Naughty':
            natureModifier['attack'] = 1.1
            natureModifier['specialDefense'] = 0.9
        elif nature == 'Bold':
            natureModifier['defense'] = 1.1
            natureModifier['attack'] = 0.9
        elif nature == 'Relaxed':
            natureModifier['defense'] = 1.1
            natureModifier['speed'] = 0.9
        elif nature == 'Impish':
            natureModifier['defense'] = 1.1
            natureModifier['specialAttack'] = 0.9
        elif nature == 'Lax':
            natureModifier['defense'] = 1.1
            natureModifier['specialDefense'] = 0.9
        elif nature == 'Timid':
            natureModifier['speed'] = 1.1
            natureModifier['attack'] = 0.9
        elif nature == 'Hasty':
            natureModifier['speed'] = 1.1
            natureModifier['defense'] = 0.9
        elif nature == 'Jolly':
            natureModifier['speed'] = 1.1
            natureModifier['specialAttack'] = 0.9
        elif nature == 'Naive':
            natureModifier['speed'] = 1.1
            natureModifier['specialDefense'] = 0.9
        elif nature == 'Modest':
            natureModifier['specialAttack'] = 1.1
            natureModifier['attack'] = 0.9
        elif nature == 'Mild':
            natureModifier['specialAttack'] = 1.1
            natureModifier['defense'] = 0.9
        elif nature == 'Quiet':
            natureModifier['specialAttack'] = 1.1
            natureModifier['speed'] = 0.9
        elif nature == 'Rash':
            natureModifier['specialAttack'] = 1.1
            natureModifier['specialDefense'] = 0.9
        elif nature == 'Calm':
            natureModifier['specialDefense'] = 1.1
            natureModifier['attack'] = 0.9
        elif nature == 'Gentle':
            natureModifier['specialDefense'] = 1.1
            natureModifier['Defense'] = 0.9
        elif nature == 'Sassy':
            natureModifier['specialDefense'] = 1.1
            natureModifier['Speed'] = 0.9
        elif nature == 'Careful':
            natureModifier['specialDefense'] = 1.1
            natureModifier['specialAttack'] = 0.9

        return natureModifier

    def getMoves(self, rawpokemondata):
        getmoves = re.compile('(?<=\-\s).+')
        rawMoveData = []
        rawMoveList = getmoves.findall(rawpokemondata)
        moveList = []
        moveData = []

        for i in rawMoveList:
            fullname = (i.replace(' ', '-')).lower()
            isHiddenPower = fullname.find('[')
            if isHiddenPower != -1:
                fullname = fullname[:isHiddenPower]
            moveList.append(fullname.rstrip('--'))

        for j in moveList:
            print(j)
            rawMoveData.append(requests.get('http://pokeapi.co/api/v2/move/' + j + '/').json())

        for k in rawMoveData:
            typeData = k['type']['url']
            moveTypeIndex = typeData.find('type')
            moveType = typeData[moveTypeIndex:].strip('type/')
            moveData.append(dict(power = k['power'], accuracy = k['accuracy'], type = moveType, pp = int(k['pp']) * 1.6, priority = k['priority'], specification = k['damage_class']['name'], healing = k['meta']['healing'], stat_chance = k['meta']['stat_chance'], flinch_chance = k['meta']['flinch_chance'], min_hits = k['meta']['min_hits'], ailment_chance = k['meta']['ailment_chance'], crit_rate = k['meta']['crit_rate'], min_turns = k['meta']['min_turns'], max_turns = k['meta']['max_turns'], max_hits = k['meta']['max_hits'], drain = k['meta']['drain'], name = k['names'][2]['name']))
            
        return moveData
        
    

    
    #Class must take raw data as well as links
    def __init__(self, rawpokemondata, pokemonStats, pokemonName):
        #gets base stat
        
        level = self.getLevel(rawpokemondata)

        
        EVs = self.extractEVdata(rawpokemondata, 'EV')
        IVs = self.extractEVdata(rawpokemondata, 'IV')
        natureModifier = self.getNature(rawpokemondata)
        
        baseHP = pokemonStats['stats'][5]['base_stat']
        baseAttack = pokemonStats['stats'][4]['base_stat']
        baseSpecialAttack = pokemonStats['stats'][3]['base_stat']
        baseDefense = pokemonStats['stats'][2]['base_stat']
        baseSpecialDef = pokemonStats['stats'][1]['base_stat']
        baseSpeed = pokemonStats['stats'][0]['base_stat']

        self.name = pokemonName
        self.level = level
        self.pokemonActiveStats = {'hp': self.setBaseStats(True, baseHP, natureModifier['hp'], IVs[0], EVs[0], level), 'attack': self.setBaseStats(False, baseAttack, natureModifier['attack'], IVs[1], EVs[1], level), 'specialAttack': self.setBaseStats(False, baseSpecialAttack, natureModifier['specialAttack'], IVs[2], EVs[2], level), 'defense': self.setBaseStats(False, baseDefense, natureModifier['defense'], IVs[3], EVs[3], level), 'specialDefense': self.setBaseStats(False, baseSpecialDef, natureModifier['specialDefense'], IVs[4], EVs[4], level), 'speed': self.setBaseStats(False, baseSpeed, natureModifier['speed'], IVs[5], EVs[5], level)}        
        print(self.pokemonActiveStats)
        self.remainingHP = self.pokemonActiveStats['hp']
        self.moves = self.getMoves(rawpokemondata)
        print(self.moves)
        return

    

    
