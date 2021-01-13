import items

class Armoury:
    armors = items.makeArmor()
    helmets = items.makeHelmet()
    weapons = items.makeWeapon()
    #potions = items.makePotion()
    shields = items.makeShield()
    def getItem(self, itemType, id):
        if itemType == 'armor':
            return self.armors[id]
        elif itemType == 'helmet':
            return self.helmets[id]
        elif itemType == 'weapon':
            return self.weapons[id]
        elif itemType == 'shield':
            return self.shields[id]
class Viking:
    def __init__(self):
        self.name = 'Viking'
        self.attributes = {
            "vitality": 1,
            "strength": 1,
            "agility": 1,
            "stamina": 1,
            "defence": 1
        }
        self.appearance = {
            "hair": 1,
            "beard": 0,
            "face": 1,
            "body": 1
        }
        self.eq = {
            'gold': 150,
            'armor': 1,
            'helmet': 0,
            'shield': 1,
            'weapon': 2,
            'hPotions': 0,
            'sPotions': 0
        }
        self.maxHitpoints = 10 + self.attributes['vitality'] + int(self.attributes['strength']/3)
        #self.maxDmg =

    def setName(self, name):
        self.name = name

    def attrU(self, attr: str, points: int):
        self.attributes[attr] += points

    def attrD(self, attr: str, points: int):
        self.attributes[attr] -= points

    def getattr(self, item: str):
        return self.attributes[item]

    def appU(self, feature: str):
        self.appearance[feature] += 1

    def appD(self, feature: str):
        self.appearance[feature] -= 1

    def getapp(self, item: str):
        return self.appearance[item]

    def setapp(self, item, number):
        self.appearance[item] = number

    def firstPoints(self, base):
        points = base
        for k in self.attributes:
            points -= self.attributes[k]
            points += 1
        return points
    '''def defence(self, viking: Viking):
        defence = self.baseDefence
        if self.aClass == 'light armor':
            defence += int(viking.getattr('agility')/2)
        elif self.aClass == 'heavy armor':
            defence += int(viking.getattr('strength')/3)
        return defence'''
    '''def attack(self, viking: Viking):
        attack = self.baseAttack
        if self.wClass == 'tHanded':
            attack += viking.getattr('strength')
        elif self.wClass == 'sword':
            attack += int(viking.getattr('agility')/2)
        elif self.wClass == 'axe':
            attack += int(viking.getattr('strength')/2)
        return attack'''
    def changeItem(self, item: int, itemType: str):
        currentGold = self.eq['gold'] + Armoury.getItem(itemType, self.eq[itemType])
        price = Armoury.getItem(itemType, item)
        if currentGold > price:
            self.eq[itemType] = item

    def changeApperiance(self, part, action):
        if action == 'up':
            if part == 'hair':
                if self.getapp('hair') == 7:
                    self.setapp('hair', 0)
                else:
                    self.appU('hair')
            elif part == 'face':
                if self.getapp('face') == 4:
                    self.setapp('face', 1)
                else:
                    self.appU('face')
            elif part == 'body':
                if self.getapp('body') == 4:
                    self.setapp('body', 1)
                else:
                    self.appU('body')
            elif part == 'beard':
                if self.getapp('beard') == 5:
                    self.setapp('beard', 0)
                else:
                    self.appU('beard')
        elif action == 'down':
            if part == 'hair':
                if self.getapp('hair') == 0:
                    self.setapp('hair', 7)
                else:
                    self.appD('hair')
            elif part == 'face':
                if self.getapp('face') == 1:
                    self.setapp('face', 4)
                else:
                    self.appD('face')
            elif part == 'body':
                if self.getapp('body') == 1:
                    self.setapp('body', 4)
                else:
                    self.appD('body')
            elif part == 'beard':
                if self.getapp('beard') == 0:
                    self.setapp('beard', 5)
                else:
                    self.appD('beard')


