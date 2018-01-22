# modules needed for game
import time
import random



# list of 21 towns
towns = [ 'Berkeley Heights', 'Clark', 'Cranford', 'Elizabeth', 'Fanwood', 'Garwood' , 'Hillside', 'Kenilworth', 'Linden', 'Mountainside', 'New Providence', 'Plainfield', 'Rahway', 'Roselle', 'Roselle Park', 'Scotch Plains', 'Springfield', 'Summit', 'Union', 'Westfield', 'Winfield']
# list of MHS 2019
names = [ 'Adam', 'Alexander', 'An', 'Andre', 'Andrew', 'Ash', 'Arthur', 'Betia' , 'Betina' , 'Blaise', 'Brian', 'Briella', 'Caitlin', 'Chris', 'Damon', 'Daniel', 'Diego' , 'Elie', 'Erika' , 'Gaya' , 'Giovanna' , 'Greyson', 'Griffin', 'Hannah', 'Isabella', 'Jacey', 'Janessa', 'Jason', 'Jeanique', 'Jeff' , 'Jenna', 'Jennifer' , 'Jon', 'Josh', 'Julien' , 'Justin', 'Karlo', 'Katie', 'Madison', 'Makayla', 'Maria', 'Massimo', 'Maxdavis', 'Max', 'Michael', 'Monica', 'Neil', 'Nixon', 'Njideka', 'Olivia', 'Preston', 'Rachael', 'Ronnie', 'Sabrina', 'Samory', 'Simon', 'Sofia', 'Sri', 'Toran', 'Vanna', 'Varun', 'Vincent', 'Virendra', 'Xavier', 'Kathryn']
# list of class types
classtypes = [ 'Athlete', 'Gamer', 'Intellectual']
# list of exercises for trainfitness function
exercises = ['leg exercises', 'back exercises', 'bicep exercises', 'shoulder exercises', 'tricep exercises', 'chest exercises', 'cardio', 'high intensity interval training', 'core exercises']
# list of subjects for trainintelligence function
subjects = ['math', 'SIA', 'english', 'history', 'health', 'robotics', 'engineering', 'conversion factors', 'Significant figures', 'coding', 'engineering scales', 'dimensioning', 'AutoCAD', 'derivational morphology', 'the book Things Fall Apart', 'Haroun and the Sea of Stories' ]
# list of games for trainreflex function
games = ['CS GO', 'Roblox', 'Minecraft', 'COD', 'Super Smash Brothers', 'Overwatch', 'Battlefield', 'FIFA' , 'NBA 2K', 'Team Fortress 2', "Gary's Mod", 'Osu', 'League of Legends', 'Fortnite', 'PUBG']

freshmanclasses = ['Math', 'SIA', 'English', 'History', 'Technology & Design', 'Health']
sports = ['basketball', 'soccer', 'baseball', 'track', 'cross country']

# Character class for game. Stores attributes for the player of game, including name, town, and what class they are.

class Character(object):
    def __init__(self, name, town, classtype ,energy = 60, fitness = 0, intelligence = 0, reflex = 0, day = 1, friends = 1 ):
        self.name = name
        self.town = town
        self.classtype = classtype
        # used for actions
        self.energy = energy
        # character attribute,
        self.fitness = fitness
        # character attribute,
        self.intelligence = intelligence
        # character attribute,
        self.reflex = reflex
        # for showing what day the player is on
        self.day = day
        # how many friends you have made
        self.friends = friends
        self.friendsmade = []
    # function for training intelligence
    def trainintelligence(self):
        # adds 1 point to player intelligence
        self.intelligence += 1
        print(f"""
You went to History during CO to talk to Jeff. You guys were studying and talking about {random.choice(subjects)}.
You gained 1 intelligence point.
Intelligence = {player.intelligence}
""")
        # subtracts 30 energy points per training
        self.energy -= 60
    # function for training reflex
    def trainreflex(self):
        # adds 1 point to player reflex
        self.reflex += 1
        print(f"""
You went to Mrs. O'Connor's room to talk to Froden. You guys were hanging out and talking about
{random.choice(games)}. He asked if you wanted to play it when you got home.
You gained 1 reflex point.
Reflex = {player.reflex}
""")
        # subtracts 60 energy points per training
        self.energy -= 60
    # function for training fitness
    def trainfitness(self):
        # adds 1 point to player fitness
        self.fitness += 1
        print(f"""
You went to the gym and trained with Toran.'Hey, {player.name}, looks like we are
going to be doing some {random.choice(exercises)} today.'
You gained 1 fitness point.
Fitness = {player.fitness}
""")
        # subtracts 60 energy points per training
        self.energy -= 60
    # chooses random person from a list of randomly generated characters
    def socialize(self):
        x = random.choice(friendlist)
        x.introduce()
        # they become your friend
        self.friends += 1
        # subtracts 60 energy
        self.energy -= 60
        player.friendsmade.append(f" {x.classtype} {x.name} from {x.town} ")

    # function that keeps track of day simulation and player's energy
    def newday(self):
        player.day += 1
        player.energy += 60
        return player.day
    # basis of the game, function that keeps player in a loop for 180 days. Allows player to use energy on actions for different attributes.
    def simulation(self):
        while self.day <= 180:
            choice = input(f'''
Today is day {player.day}. You learned something new in {random.choice(freshmanclasses)} today.
You have free time during 5 & 6. What would you like to do?
You can:
-Talk to Jeff (type & enter j)
-Talk to Froden (type & enter f)
-Talk to Toran (type & enter t)
-Socialize (type & enter s)
-Check stats (type & enter stats)
''').lower()
            # player's actions in the game, which gives them attributes within the Character class
            if choice == 'j':
                player.trainintelligence()
            elif choice == 'f':
                player.trainreflex()
            elif choice == 't':
                player.trainfitness()
            elif choice == 's':
                player.socialize()
            elif choice == 'stats':
                print(f"""
Current Stats:
Intelligence : {player.intelligence}
Fitness : {player.fitness}
Reflex : {player.reflex}
Friends : {player.friends}
""")
            # if player makes typing error
            else:
                print('''
I think you may have entered a choice wrong!
Try again!
''')
            # begins a new day once player uses all of their energy
            if self.energy <= 0:
                player.newday()

class Friend(object):
    def __init__(self, name, town, classtype):
        self.name = name
        self.town = town
        self.classtype = classtype

    def introduce(self):
        print(f"""You go into Mr. Nowakoski's room looking for students to talk to.
        Looks like {self.classtype} {self.name} from {self.town} wants to talk to you!""")


friendlist = []
for x in range(500):
    friendlist.append(Friend(random.choice(names), random.choice(towns), random.choice(classtypes)))

#def start():
 #   slowprint('Welcome to the MHS Freshman year simulator. You are going to start your first day.')
 #  introduction = input('Type ok to continue >>>   ').lower()

  #  if introduction == 'ok':
   #     intro1()

# introductory exposition to MHS simulation game
print('''
"Wow, I'm finally here." You say to yourself. The day has just begun, and you make the long walk all
the way to the Magnet building.
    ''')
#time.sleep(4)
print('''
Upon the security guard opening the door, lines are formed behind what looks
like a small table.
    ''')
#time.sleep(4)
print('''
A woman next to the table is directing incoming students,"If you are freshman, please get in line
here behind the island! Thank you."You mind your business, walking to the end of the long freshman line.
    ''')
#time.sleep(6)
print('''
Gradually, the line gets shorter and you are finally at the table. The woman greets you.
You reply with an esctatic hello.
    ''')
#time.sleep(4)

# player chooses what to call their character
playername = (input('''
"You seem very excited for your first day! Well I need to give you your ID and schedule. What is your name?"

Enter Player Name :  '''))

#time.sleep(2)

print('''
"Hmm, I cant really find your name... You know what, it might be easier if you give me the town you live in!"
    ''')
#time.sleep(4)

playertown = (input('''
"So, what town are you from?"

Enter Town Name : '''))

#time.sleep(2)

print(f"""
Oh, I found them! Here's your ID and schedule, {playername} from {playertown}!
Please go into the auditorium to wait before the morning assembly.'
    """)

#time.sleep(6)

print("""
You walk into the room and the sound of chatting students fills the air.You notice that there
are several students have formed their own small circles.Three groups stand out to you the most.
    """)

#time.sleep(6)

print("""
One group seems to be talking about which classes they are taking and their academic achievements.
Apparently one of them is taking Pre Calculus and Chemistry this year! They must be really smart.
    """)

#time.sleep(6)

print("""
Another group is talking about sports. Some of them enjoy watching sports and some have played since middleschool.
One of them is an avid baseball player and has also played football.
    """)

#time.sleep(6)

print("""
The last group was talking about different video games. They were arguing aboutwhat video game was their favorite;
Call of Duty, Pokemon, Super Smash Brothers, and even Minecraft. Seemed like a heated debate.
    """)

#time.sleep(6)
while True:

    playertype = input("""
All of the groups and their conversations intrigue you, but you are unsure where you fit between the three.
Which group do you select?

Intellectual
Athlete
Gamer

Choose your group. (Determines your class type!):
    """).lower()

    if playertype == 'intellectual':
        print("""
You approach the group talking about academics. A freshman named Jeff was talking about his interests
in robotics and how there is a team at Magnet. You express your fascination in the subject and he asks for your name.
    """)

    #time.sleep(6)

        print(f"""
'Oh, your name is {playername} and you are from {playertown}! My name's Jeff and I am from Berkeley Heights.
You should definitely join the robotics team when we are allowed to sign up.
If you ever need any help with anything in school, I could definitely teach you a thing or two!'
    """)

    #time.sleep(6)

        print(f"""
Jeff becomes one of your first friends at Magnet, a friendship that is sure to last. When you level up
or want to gain intelligence points,talk to Jeff during school! Intelligence points determine what you accomplish at Magnet.
    """)
        break

    elif playertype == 'athlete':
        print(f"""
You approach the group talking about sports. A freshman named Toran was talking about the one time he
sprained his ankle during a football game. You talk about a similar situation you had when you played
sports in middleschool.
    """)
    #time.sleep(6)

        print(f"""
'Oh, your name is {playername} and you are from {playertown}! My name is Toran and I'm from Plainfield.
I played football and baseball in middleschool. Although I like most sports,I want to become
a baseball player in college and hopefully the MLB later on. If you ever want to train or play a sport with me,
I'd be happy to do that.
    """)

    #time.sleep(6)

        print("""
Toran becomes one of your first friends at Magnet, a friendship that is sure to last. When you level up
or want to gain fitness points,you should talk to Toran during school! Fitness points determine what you accomplish at Magnet.
    """)
        break

    elif playertype == 'gamer':

        print("""
You approach the group talking about video games. Two students in the group seem to be fighting over
which game is better. One of them likes Super Smash Brothers and the other likes Call of Duty.
You enter the conversation and talk about your interest for both games.
    """)

    #time.sleep(6)

        print("""
The two students ignore you and keep going on their tangents about their video games.
A student sitting around the outside of the group comes to you.
"Don't mind them, they are both being ridiculous. It's cool to enjoy all types of games; I do too.""")

    #time.sleep(6)

        print(f"""
Nice to meet you, {playername}. My name is Froden and I'm from Garwood.
I play soccer for my highschool team, but in my off-time I enjoy playing video games.
Well, I'd be down to play any game with you if you ask.
    """)

    #time.sleep(6)

        print(f"""
Froden becomes one of your first friends at Magnet, a friendship that is sure to last.
When you level up or want to gain reflex points, you should talk to Froden.
Reflex points determine what you accomplish at Magnet.
    """)
        break

    else:
        print(f"""
Uh oh, you might have entered your group wrong. Please make your choice again.""")

# takes all of the three player inputs and creates a character with the Character class
player = Character(playername, playertown, playertype)

time.sleep(4)

print("""
Shortly after, the Magnet principal Mr.Rafalowski comes in and everyone begins sitting down.
He greets everyone and talks about his expectations for the upcoming year.
He is excited to be working with the new freshman since it will be his first full 4 year graduating class at Magnet.
""")

time.sleep(6)

print("""
"It's going to be a long 180 days, but I know all of you are going to make something
of it and be the best that you can"
""")

time.sleep(4)

print(f"""
The principal's speech fills you with determination for the upcoming school year.
You, {player.classtype} {player.name} from {player.town}, have the ability to make
something of yourself. The choice is yours this year, and you have 180 days to make it happen.
""")
# intro ends, starts game simulation of school year
player.simulation()

if player.day == 90:
            print(f'''
Well, {player.name}, it looks like you've made it to the half way point of the year.
Let's see what you have accomplished.
''')

        if player.fitness >= 25:
            print(f'''
You've been training consistently in the gym and have seen improvements in your physique.
''')
        elif player.fitness >= 40:
            print(f'''
Your hardwork has rewarded you a spot on your highschool's {random.choice(sports)} team.
''')
        if player.intelligence >= 25:
            print(f'''
Your effort in your classes is showing, and you are maintaining a 90 QPA.
''')
        elif player.intelligence >= 40:
            print(f'''
Your teachers are impressed with your hardwork and participation in class.
You also attained High Honor Roll!
''')
        if player.reflex >= 25:
            print(f'''
You started a video game club at Magnet and a lot of people join.
''')
            player.friends += 5
