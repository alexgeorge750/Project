from dataclasses import dataclass


class Location:
    def __init__(self, description:str, coordinates:tuple, usables: list, locked_description: str, key_item: str):
        self.description = description
        self.coordinates = coordinates
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.pickups = []
        self.locked = bool
        self.locked_description = locked_description
        self.key_item = key_item
        self.enemy = Enemy


    def addPickup(self, obj):
        self.pickups.append(obj)

    def removePickup(self, obj):
        self.pickups.remove(obj)
        return obj

    def unlock(self):
        current_location.locked = False


@dataclass
class Enemy:
    name: str
    health: int
    description = str
    defeater = str

    def attack(self):
        current_player.health -= 1
        print('The enemy attacked! You now have ' + str(current_player.health) + ' health points.' )


dog = Enemy('dog', 3,)
dog.description = 'You encounter a dog!'
dog.defeater = 'dog bone'
mummy = Enemy('mummy', 3)
mummy.description = 'You encounter a mummy!'
mummy.defeater = 'knife'
ghost = Enemy('final boss', 5)
ghost.description = 'You encounter a ghost!'
ghost.defeater = 'ray gun'


current_enemy = None
weapon_list = ['dog bone', 'knife', 'ray gun']
@dataclass
class LockedObject():
    item = str
    locked = bool
    locked_description = str
    key_item = str
    inside_object = []
    open_description = str


    def unlock(self, item):
        self.locked = False


trapdoor = LockedObject()
trapdoor.item = 'trapdoor'
trapdoor.locked = True
trapdoor.locked_description = 'The trapdoor is locked. Use key to open.'
trapdoor.key_item = 'key'
trapdoor.open_description = "Opening the trapdoor reveals a staircase to a basement. Type 'go south' to  continue. "
chest = LockedObject()
chest.item = 'chest'
chest.locked = True
chest.inside_object = ['ray gun']
chest.locked_description = 'The chest is locked. Use key2 to open.'
chest.key_item = 'key2'
mailbox = LockedObject()
mailbox.item = 'mailbox'
mailbox.locked = False
mailbox.inside_object = ["a note with writing '1234'", ' a dog bone']
dresser = LockedObject()
dresser.item = 'dresser'
dresser.locked = False
dresser.inside_object = ['key2']
foyer = Location('''An open foyer with a large dimly lit chandelier hanging from 
the ceiling.''', (2,1), [], '', '')
foyer.enemy = None
livingRoom = Location('''A dark, dusty living room with a couch that has a key 
on it.''', (3,1), [], '','')
livingRoom.addPickup('key')
livingRoom.enemy = None
diningRoom = Location('''A large dining room containing a long table with a 
picture frame in the middle.''', (1,1), [], '','')
diningRoom.addPickup('picture frame')
diningRoom.enemy = None
driveway = Location('A long driveway leading to the mansion.',(2,3),[],
'The gate is locked preventing you from entering. Enter code to open.','1234')
driveway.locked = True
driveway.enemy = dog
street = Location('Under a streetlamp facing a large metal gate. You see a mailbox.',(2,1),
['gate','mailbox'],'','')
street.addPickup('note')
street.addPickup('dog bone')
street.enemy = None
kitchen = Location('''An oddly put together kitchen with an open drawer 
revealing a knife inside.''',(2,2), [], '','')
kitchen.addPickup('knife')
kitchen.enemy = None
bathroom = Location('''A small bathroom with blood splattered on the 
mirror.''',(1,2),[], '','')
bathroom.enemy = None
bedroom = Location('''A dark bedroom with an old bed and a bedside table.''', (1,3),
['bedside table'], '','')
bedroom.enemy = None
closet = Location('''A small closet with a strange rug on the floor.''',
(2,3),['rug', 'trapdoor'], '','')
closet.enemy = None
theatre = Location('''A small movie theatre with an old projector that seems to 
be working.''', (3,2), ['projector'], '','')
theatre.enemy = mummy
basementStart = Location('''A large, open basement with many doors to other 
rooms.''', (2,2), [], '', '')
basementStart.enemy = None
artRoom = Location('''A small room with many old portraits on the 
walls.''', 
(2,3), [], '','')
artRoom.enemy = None
library = Location('''A large library with one book that seems to be out of 
place on the shelf.''', (1,1), ['book'], '','')
library.enemy = ghost
basementBedroom = Location('''A small bedroom with a large chest at the foot of 
the bed.''', (2,1), ['chest'], '','')
basementBedroom.addPickup('ray gun')
basementBedroom.enemy = None
basementCloset = Location('A tiny closet with a dresser.',(3,1), ['dresser'],
'','')
basementCloset.addPickup('key2')
basementCloset.enemy = None
pianoRoom = Location('A small room with a large piano.', (3,2), ['piano'],
'','')
pianoRoom.enemy = None
escapeRoom = Location('A mysterious room with a single locked door.', 
(1,2), [], '','bookshelf door')
escapeRoom.enemy = None
escapeRoom.locked = True


foyer.north = kitchen
foyer.east = livingRoom
foyer.west = diningRoom
foyer.south = driveway

livingRoom.north = theatre
livingRoom.west = foyer

diningRoom.north = bathroom
diningRoom.east = foyer

driveway.north = foyer
driveway.south = street

street.north = driveway

kitchen.south = foyer
kitchen.east = theatre
kitchen.west = bathroom

bathroom.north = bedroom
bathroom.east = kitchen
# bathroom.south = dining is this correct?

bedroom.east = closet
bedroom.south = bathroom

closet.west = bedroom
closet.south = basementStart

theatre.west = kitchen
theatre.south = livingRoom

basementStart.north = artRoom
basementStart.south = basementBedroom
basementStart.east = pianoRoom

artRoom.south = basementStart

library.north = escapeRoom
library.east = bedroom

basementBedroom.north = basementStart
basementBedroom.east = basementCloset
basementBedroom.west = library

basementCloset.west = basementBedroom

pianoRoom.west = basementStart

escapeRoom.south = library

all_locations = [street,driveway,foyer, livingRoom, diningRoom, theatre, bedroom, bathroom, closet, artRoom,
basementStart,escapeRoom, pianoRoom, basementBedroom, basementCloset, library]

all_locked_objects = [trapdoor, chest, dresser]
@dataclass
class Player:
    coordinates: tuple
    name: str
    health: int
    items: list[str]


    def pickup_item(self, item: str):
        if item in  current_location.pickups:
            self.items.append(item)
            print(item + ' picked up')
        else:
            print('Command not recognized.')

    def attack(self):
        current_enemy.health -= 1
        print('You attacked! The enemy now has ' + str(current_enemy.health) + ' health points.')


current_location = street


def go_north(next_location):
    global current_location, current_enemy
    if next_location is None:
        print("You can't go north from here.")
        return
    if current_enemy:
        if current_enemy.health > 0:
            current_enemy.attack()
            return
    if next_location.locked == True:
       print(next_location.locked_description)
       return
    if current_location.north:
        current_player.coordinates = (current_player.coordinates[0], current_player.coordinates[1] + 1)
        current_location = current_location.north
        current_enemy = current_location.enemy
        print("Your current location is now: " + current_location.description)
        if current_enemy:
            print(current_enemy.description)
            current_enemy.attack()
    else:
        print("You can't go north from here.")

def go_south(next_location):
    global current_location, current_enemy
    if next_location is None:
        print("You can't go south from here.")
        return
    if current_enemy:
        if current_enemy.health > 0:
            current_enemy.attack()
            return
    if next_location.locked == True:
       print(next_location.locked_description)
       return
    if current_location.south:
        if next_location is basementStart:
            current_player.coordinates = (2,2)
            current_location = current_location.south
            print("Your current location is now: " + current_location.description)
        else:
            current_player.coordinates = (current_player.coordinates[0], current_player.coordinates[1] - 1)
            current_location = current_location.south
            current_enemy = current_location.enemy
            print("Your current location is now: " + current_location.description)
            if current_enemy:
                print(current_enemy.description)
                current_enemy.attack()
    else:
        print("You can't go south from here.")

def go_east(next_location):
    global current_location, current_enemy
    if next_location is None:
        print("You can't go east from here.")
        return
    if current_enemy:
        if current_enemy.health > 0:
            current_enemy.attack()
            return
    if next_location.locked == True:
       print(next_location.locked_description)
       return
    elif current_location.east:
        current_player.coordinates = (current_player.coordinates[0] + 1, current_player.coordinates[1])
        current_location = current_location.east
        current_enemy = current_location.enemy
        print("Your current location is now: " + current_location.description)
        if current_enemy:
            print(current_enemy.description)
            current_enemy.attack()
    else:
        print("You can't go east from here.")

def go_west(next_location):
    global current_location, current_enemy
    if next_location is None:
        print("You can't go west from here.")
        return
    if current_enemy:
        if current_enemy.health > 0:
            current_enemy.attack()
            return
    if next_location.locked == True:
       print(next_location.locked_description)
       return
    if current_location.west:
        current_player.coordinates = (current_player.coordinates[0] - 1, current_player.coordinates[1])
        current_location = current_location.west
        current_enemy = current_location.enemy
        print("Your current location is now: " + current_location.description)
        if current_enemy:
            print(current_enemy.description)
            current_enemy.attack()
    else:
        print("You can't go west from here.")



def getCurrentLocation():
        return current_player.coordinates


def run_game():
    global current_enemy
    run = True 
    while run == True:
        response = input('>>')
        if response == 'quit':
            break
        if response == "go north":
            direction = response.split('go', 1)[1].strip()
            next_location = current_location.__getattribute__(direction)
            go_north(next_location)
        if response == "go south":
            direction = response.split('go', 1)[1].strip()
            next_location = current_location.__getattribute__(direction)
            go_south(next_location)
        if response == "go east":
            direction = response.split('go', 1)[1].strip()
            next_location = current_location.__getattribute__(direction)
            go_east(next_location)
        if response == "go west":
            direction = response.split('go', 1)[1].strip()
            next_location = current_location.__getattribute__(direction)
            go_west(next_location)
        if response.startswith('take '):
            item = response.split('take' , 1)[1].strip()
            current_player.pickup_item(item)
        if response.startswith('use '):
            for location in all_locations:
                if location.key_item == response.split('use' , 1)[1].strip():
                    location.locked = False
                    print("Successful unlock.")
            for object in all_locked_objects:
                if object.key_item == response.split('use' , 1)[1].strip():
                    object.locked = False
                    print("Successful unlock.")
            if current_enemy:
                if response.split('use' , 1)[1].strip() in weapon_list:
                    if current_enemy == dog:
                        print('The dog chased the dog bone. You are safe!')
                        current_enemy = None
                    else:
                        if response.split('use', 1)[1].strip() == current_enemy.defeater:
                            current_player.attack()
                            if current_enemy.health == 0:
                                current_enemy = None
                                print('You defeated the enemy!')
                        else:
                            print('Wrong weapon!')
        if response.startswith('open '):
            for object in all_locked_objects:
                if response.split('open ', 1)[1].strip() == object.item:
                    if object.locked == True:
                        print(object.locked_description)
                    else:
                        if response.split('open ', 1)[1].strip() == 'trapdoor':
                            print(object.open_description)
                        elif len(object.inside_object) == 1:
                            print("Opening the " + str(object.item) + ' reveals: ' + object.inside_object[0])
                        else:
                            print("Opening the " + str(object.item) + ' reveals a ' + object.inside_object[0] + ' and '
                                  + object.inside_object[1])
        if response.startswith('move' ):
            if response.split('move' , 1)[1].strip() == 'rug':
                print('Moving the rug reveals a trapdoor underneath')
        if response == 'use projector':
            print('turning on the projector reveals an image of a bookshelf')





print('''Welcome to the haunted mansion text based adventure game! In this  
game, you have stumbled upon a haunted mansion one night, and you decide  
to go explore. Can you make it out alive? Type your character's name below 
to start!''')

player_name = input('>>')
current_player = Player((2,1),player_name,5,[])
 
print("Your current location is: " + current_location.description)

run_game()

