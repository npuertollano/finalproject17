import sys
import time
import random

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./10)

# list of 21 towns
towns = [ 'Berkeley Heights', 'Clark', 'Cranford', 'Elizabeth', 'Fanwood', 'Garwood' , 'Hillside', 'Kenilworth', 'Linden', 'Mountainside', 'New Providence', 'Plainfield', 'Rahway', 'Roselle', 'Roselle Park', 'Scotch Plains', 'Springfield', 'Summit', 'Union', 'Westfield', 'Winfield']
# list of MHS 2019
names = [ 'Adam', 'Alexander', 'An', 'Andre', 'Andrew', 'Ash', 'Arthur', 'Betia' , 'Betina' , 'Blaise', 'Brian', 'Briella', 'Caitlin', 'Chris', 'Damon', 'Daniel', 'Diego' , 'Elie', 'Erika' , 'Gaya' , 'Giovanna' , 'Greyson', 'Griffin', 'Hannah', 'Isabella', 'Jacey', 'Janessa', 'Jason', 'Jeanique', 'Jeff' , 'Jenna', 'Jennifer' , 'Jon', 'Josh', 'Julien' , 'Justin', 'Karlo', 'Katie', 'Madison', 'Makayla', 'Maria', 'Massimo', 'Maxdavis', 'Max', 'Michael', 'Monica', 'Neil', 'Nixon', 'Njideka', 'Olivia', 'Preston', 'Rachael', 'Ronnie', 'Sabrina', 'Samory', 'Simon', 'Sofia', 'Sri', 'Toran', 'Vanna', 'Varun', 'Vincent', 'Virendra', 'Xavier', 'Kathryn']
# list of class types
classtypes = [ 'Athlete', 'Gamer', 'Tryhard']

generate():

class Character(object):
    def __init__(self, name, town, classtype , exp, energy, strength ):
        self.name = name
        self.town = town
        self.classtype = classtype
        self.exp = 0
        self.energy = 100
        self.strength = 10

class Enemy(object):
    def __init__(self, name, town, classtype, exp, strength):
        self.name = name
        self.exp = 10
        self.strength = 5

def fight():





slowprint('Welcome to the MHS Freshman year simulator. You are going to start your first day.')
introduction = input('Type ok to continue >>>   ').lower()

if introduction == 'ok':
    print('''
    "Wow, I'm finally here." You say to yourself. The day has just begun, and you make the long walk all
    the way to the Magnet building.
    ''')
    time.sleep(4)
    print('''
    Upon the security guard opening the door, lines are formed behind what looks
    like a small table.
    ''')
    time.sleep(4)
    print('''
    A woman next to the table is directing incoming students,
    "If you are freshman, please get in line here behind the island! Thank you."
    You mind your business, walking to the end of the long freshman line.
    ''')
    time.sleep(6)
    print('''
    "Gradually, the line gets shorter and you are finally at the table. The woman greets you.
    You reply with an esctatic hello.
    ''')
    time.sleep(4)

    playername = (input('''
    "You seem very excited for your first day!
    Well I need to give you your ID and schedule. What is your name?"

    Enter Player Name :  '''))







