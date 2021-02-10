import sys

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

    'Hall' : { 
        'south' : 'Kitchen',
        'up' : 'Northern Attic'
    },

    'Kitchen' : {
            'north' : 'Hall',
            'up' : 'Southern Attic'
    },
    
    'Northern Attic' : {
        'down' : 'Hall',
        'south' : 'Southern Attic',
        'item' : 'sword'
    },

    'Southern Attic' : {
        'down' : 'Kitchen',
        'north' : 'Northern Attic',
        'enemy' : 'goblin'
    }
         }

enemyDefenders = ['sword']

#start the player in the Hall
global currentRoom
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    elif move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    
    else:
        print('That\'s not a command!')
    
    if 'enemy' in rooms[currentRoom]:
        enemy = rooms[currentRoom]['enemy']
        vowels = ['a', 'i', 'e', 'o', 'u']
        n = ''
        safe = False
        for vowel in vowels:
            if enemy.startswith(vowel): n = 'n'
        def checkIfSafe(enemyDefendersList):
            for defenderItem in enemyDefendersList:
                if defenderItem in inventory:
                    return True, defenderItem
                else:
                    return False, None
        safe, defender = checkIfSafe(enemyDefenders)
        if safe == False:
            print(f'A{n} {enemy} has got you... GAME OVER!')
            sys.exit()
        elif safe == True:
            print(f'The {enemy} tried to eliminate \nyou, but you were \nfaster and destroyed it \nwith your {defender}.')
            del rooms[currentRoom]['enemy']