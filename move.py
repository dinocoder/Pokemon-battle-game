class Move:
        
        def __init__(self, rawMoveData):
            typeData = rawMoveData['type']['url']
            moveTypeIndex = typeData.find('type')
            self.moveType = typeData[moveTypeIndex:].strip('type/')
            self.power = int(rawMoveData['power']) if rawMoveData['power'] != None else 0
            self.accuracy = int(rawMoveData['accuracy']) if rawMoveData['power'] != None else -1
            self.pp = int(rawMoveData['pp'])
            self.priority = int(rawMoveData['priority']) if rawMoveData['priority'] != None else 0
            self.power = rawMoveData['damage_class']['name']
            self.healing = int(rawMoveData['meta']['healing']) if rawMoveData['meta']['healing'] != None else 0
            self.stat_chance = int(rawMoveData['meta']['stat_chance']) if rawMoveData['meta']['stat_chance'] != None else 0
            self.flinch_chance = int(rawMoveData['meta']['flinch_chance']) if rawMoveData['meta']['flinch_chance'] != None else 0
            self.stat_chance = int(rawMoveData['meta']['min_hits']) if rawMoveData['meta']['min_hits'] != None else 0
            self.stat_chance = int(rawMoveData['meta']['max_hits']) if rawMoveData['meta']['max_hits'] != None else 0
            self.stat_chance = int(rawMoveData['meta']['drain']) if rawMoveData['meta']['drain'] != None else 0
            self.stat_chance = rawMoveData['names'][2]['name']
            '''
            print(rawMoveData)
            print(rawMoveData['power'])
            print(rawMoveData['accuracy'])
            print(rawMoveData['pp'])
            print(rawMoveData['priority'])
            print(rawMoveData['damage_class']['name'])
            print(rawMoveData['meta']['healing'])
            print(rawMoveData['meta']['stat_chance'])
            print(rawMoveData['meta']['flinch_chance'])
            print(rawMoveData['meta']['min_hits'])
            print(rawMoveData['meta']['max_turns'])
            print(rawMoveData['meta']['max_hits'])
            print(rawMoveData['meta']['drain'])
            print(rawMoveData['names'][2]['name'])
            
            moveData.append(dict(power = rawMoveData['power'], accuracy = rawMoveData['accuracy'], type = int(moveType), pp = int(rawMoveData['pp']) * 1.6, priority = int(rawMoveData['priority']), specification = rawMoveData['damage_class']['name'], healing = int(rawMoveData['meta']['healing']), stat_chance = int(rawMoveData['meta']['stat_chance']),flinch_chance = int(rawMoveData['meta']['flinch_chance']), min_hits = int(rawMoveData['meta']['min_hits']), ailment_chance = int(rawMoveData['meta']['ailment_chance']), crit_rate = int(rawMoveData['meta']['crit_rate']), min_turns = int(rawMoveData['meta']['min_turns']), max_turns = int(rawMoveData['meta']['max_turns']), max_hits = int(rawMoveData['meta']['max_hits']), drain = int(rawMoveData['meta']['drain']), name = rawMoveData['names'][2]['name']))
            '''
