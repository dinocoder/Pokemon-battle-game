import re


class Pokemon:
    
    def setBaseStats(self, isHP, baseStat, natureModifier, statIV, statEV, level):
        #Determines effective stat
        if isHP:
            print(str(baseStat) + ' ' + str(statIV) + ' ' + str(statEV) + ' ' + str(level) + ' ')
            effectiveStat = (((2 * baseStat + statIV + (statEV / 4)) * level) / 100) + level + 10
        else:
            print(str(baseStat) + ' ' + str(statIV) + ' ' + str(statEV) + ' ' + str(level) + ' ' + str(natureModifier))
            effectiveStat = ((((2 * baseStat + statIV + (statEV / 4)) * level) / 100) + 5 ) * natureModifier
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
            test = findlevel.findall(rawpokemondata)[0]:
        except:
            return 100
        else:
            return findlevel.findall(rawpokemondata)[0]


    
    #Class must take raw data as well as links
    def __init__(self, rawpokemondata, pokemonStats):
        #gets base stat
        
        level = getLevel(rawpokemondata)
        
        natureModifer = 1
        
        EVs = self.extractEVdata(rawpokemondata, 'EV')
        IVs = self.extractEVdata(rawpokemondata, 'IV')
        natureModifier = 1

        #kEY ERROR 'stats' on 2nd pkmn
        baseHP = pokemonStats['stats'][5]['base_stat']
        baseAttack = pokemonStats['stats'][4]['base_stat']
        baseSpecialAttack = pokemonStats['stats'][3]['base_stat']
        baseDefense = pokemonStats['stats'][2]['base_stat']
        baseSpecialDef = pokemonStats['stats'][1]['base_stat']
        baseSpeed = pokemonStats['stats'][0]['base_stat']

        self.pokemonActiveStats = {'hp': self.setBaseStats(True, baseHP, natureModifier, IVs[0], EVs[0], level), 'attack': self.setBaseStats(False, baseAttack, natureModifier, IVs[1], EVs[1], level), 'specialAttack': self.setBaseStats(False, baseSpecialAttack, natureModifier, IVs[2], EVs[2], level), 'defense': self.setBaseStats(False, baseDefense, natureModifier, IVs[3], EVs[3], level), 'specialDefense': self.setBaseStats(False, baseSpecialDef, natureModifier, IVs[4], EVs[4], level), 'speed': self.setBaseStats(False, baseSpeed, natureModifier, IVs[5], EVs[5], level)}        
        print(self.pokemonActiveStats)
        return

    

    
