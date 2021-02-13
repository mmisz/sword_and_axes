
class Item:
    def __init__(self, name: str, price: int, id: int, itemType: str):
        self.name = name
        self.price = price
        self.id = id
        self.itemType = itemType

class Armor(Item):
    def __init__(self, name: str, price: int, baseDefence: int, id: int, aClass: str, itemType: str):
        super().__init__(name, price, id, itemType)
        self.baseDefence = baseDefence
        self.aClass = aClass

class Weapon(Item):
    def __init__(self, name: str, price: int, baseAttack: int, id: int, wClass: str, itemType: str):
        super().__init__(name, price, id, itemType)
        self.baseAttack = baseAttack
        self.wClass = wClass

class Shield(Armor):
    def __init__(self, name: str, price: int, baseDefence: int, id: int, aClass: str, blockChance: int, itemType: str):
        super().__init__(name, price, baseDefence, id, aClass, itemType)
        self.blockChance = blockChance
'''class Potion:
    def __init__(self, name: str, price: int, id: int, type: str):
        self.name = name
        self.price = price
        self.id = id
        self.type = type'''

def makeArmor():
    armors = list()
    names = ['nic', 'skórzane pasy', 'sórzana kurtka', 'wzmacniana kurtka', 'zbroja segmentowa', 'hauberk']
    armorClasses = ['light armor', 'heavy armor']
    giveClothClass = [0, 0, 0, 0, 1, 1]
    prices = [0, 3, 7, 11, 16, 21]
    defences = [0, 2, 5, 7, 13, 16]

    for i in range(len(names)):
        armor = Armor(names[i], prices[i], defences[i], i, armorClasses[giveClothClass[i]], 'armor')
        armors.append(armor)
    return armors
def makeHelmet():
    helmets = list()
    names = ['nic', 'kaptur', 'sórzany czepiec', 'pikowany czepiec', 'misiurka', 'norman']
    armorClasses = ['light armor', 'heavy armor']
    giveClothClass = [0, 0, 0, 0, 1, 1]
    prices = [0, 2, 4, 5, 7, 10]
    defences = [0, 1, 3, 4, 6, 8]

    for i in range(len(names)):
        helmet = Armor(names[i], prices[i], defences[i], i, armorClasses[giveClothClass[i]], 'helmet')
        helmets.append(helmet)
    return helmets
def makeWeapon():
    weapons = list()
    names = ['nic', 'żelazny sztylet', 'żelazny miecz', 'żelazny topór', 'żelazny dun',
             'maczuga', 'stalowy miecz', 'stalowy topór', 'stalowy dun',
             'buława', 'miecz jarla', 'topór jarla', 'dun jarla',
             'damasceński sztylet']
    prices = [0, 2, 4, 5, 6,
              7, 8, 9, 12, 13,
              14, 16, 19, 15]
    damages = [8, 40, 80, 84, 160,
               48, 160, 180, 240, 80,
               240, 250, 300, 96]
    weaponClasses = ['dagger', 'mace', 'sword', 'axe', 'tHanded']
    giveWeaponClass = [1, 0, 2, 3, 4,
                       1, 2, 3, 4, 1,
                       2, 3, 4, 0]

    for i in range(len(names)):
        weapon = Weapon(names[i], prices[i], damages[i], i, weaponClasses[giveWeaponClass[i]], 'weapon')
        weapons.append(weapon)
    return weapons
def makeShield():
    shields = list()
    names = ['nic', 'tarcza huskarla', 'tarcza owalna', 'tarcza normańska', 'puklerz']
    armorClasses = ['light armor', 'heavy armor']
    giveClass = [0, 1, 1, 1, 0]
    prices = [0, 5, 6, 8, 4]
    defences = [0, 3, 4, 6, 1]
    chances = [0, 10, 15, 20, 20]

    for i in range(len(names)):
        shield = Shield(names[i], prices[i], defences[i], i, armorClasses[giveClass[i]], chances[i], 'shield')
        shields.append(shield)
    return shields
'''def makePotion():
    potions = list()
    names = ['mikstura wytrzymałości', 'mikstura życia']
    prices = [3, 4]
    types = ['stamina', 'hitpoints']
    for i in range(len(names)):
        potion = Potion(names[i], prices[i], i + 1, types[i])
        potions.append(potion)
    return potions'''
