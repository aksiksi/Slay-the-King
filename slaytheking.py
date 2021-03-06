############################################################
## This silly game is coded by Assil Ksiksi.              ##
## It is not complete yet.                                ##
############################################################

import sys
import os
from sys import exit
from time import sleep
from random import randrange, seed

def clear_console():
    if sys.platform in ["darwin", "linux2"]:
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")

# A simple battle algorithm. Sadly, it took me over 45 minutes to get right..
def battle(player_level, knight_number):
    # Define player and enemy stats based on passed variables
    knight_stats = [knight_number, knight_number * 30, knight_number * 4]
    player_stats = [player_level, player_level * 30, player_level * 4]

    print "\nBattle Mode -> Enemy: Tower Knight #%d\n" % knight_stats[0]

    your_hp = player_stats[1] # Assign HP to a variable
    enemy_hp = knight_stats[1] # Assign HP to a variable

    while your_hp > 0 and enemy_hp > 0: # Loop is broken once player or enemy gets to 0 HP.
        action = raw_input("What will you do? ")
        if action == "attack":
            seed(None)
            your_hit_chance = randrange(2, 4) # Randomly generates a number between 2 and 10, non-inclusive, to determine hit chance.
            your_damage = randrange(player_stats[2], player_stats[2] + 4 * player_stats[0]) # Damage is calculated based on player/enemy's level.
            if your_hit_chance % 2 == 0: # Hit takes place only if your_hit_chance is even, making it a 50% chance.
                print "\nYou hit the knight with %d damage!" % your_damage
                enemy_hp -= your_damage # Damage dealt (randomly generated) is negated from enemy's HP
            else:
                print "\nYour attack was blocked by the enemy!"
            seed(None)
            enemy_hit_chance = randrange(2, 10)
            enemy_damage = randrange(knight_stats[2], knight_stats[2] + 4 * knight_stats[0])
            if enemy_hit_chance % 2 != 0: # Same thing, but deals damage when result is odd.
                print "Knight #%d hit you back with %d damage!\n" % (knight_stats[0], enemy_damage)
                your_hp -= enemy_damage
            else:
                print "You blocked the knight's attack!\n"
        elif action == "defend": # Same as above, except enemy has a 25% to land a hit.
            print "\nYou are now in a defensive stance."
            enemy_hit_chance = randrange(2, 10)
            enemy_damage = randrange(knight_stats[2], knight_stats[2] + 4 * knight_stats[0])
            if enemy_hit_chance == 3 or enemy_hit_chance == 5:
                print "Knight #%d broke your defense and hit you with %d damage!\n" % (knight_stats[0], enemy_damage)
                your_hp -= enemy_damage
            else:
                print "You blocked the knight's attack!\n"
        elif action == "heal" and your_hp == player_stats[1]:
            print "\nYou HP is full already!\n"
        elif action == "heal" and your_hp < player_stats[1]:
            hp_gain = 15 * player_stats[0] # HP gained is based on player level.
            if your_hp + hp_gain <= player_stats[1]:
                print "\nYou have gained %d HP!\n" % hp_gain
                your_hp += hp_gain
            else:
                print "\nYour HP is now full to the brim!"
                hp_gain = player_stats[1] - your_hp
                your_hp += hp_gain
            enemy_hit_chance = randrange(2, 10)
            enemy_damage = randrange(knight_stats[2], knight_stats[2] + 4 * knight_stats[0])
            if enemy_hit_chance % 2 != 0:
                print "Knight #%d hit you with %d damage!\n" % (knight_stats[0], enemy_damage)
                your_hp -= enemy_damage
            else:
                print "You were lucky enough to evade the enemy's attack.\n"
        elif action == "hp":
            print "\nYour current HP is %d.\n" % your_hp # Shows player's current HP.
        elif action == "enemyhp":
            print "\nThe enemy has %d HP remaining.\n" % enemy_hp
        elif action == "help":
            print "\nAvailable commands:\n"
            print "attack -> Attack the enemy."
            print "defend -> Skip your turn to tighten your defense."
            print "heal -> Replenish your HP."
            print "hp -> Check your current HP."
            print "enemyhp -> Check the enemy's HP."
            print "exit -> Quit the game.\n"
        elif action == "exit":
            exit(0)
        else:
            print "\nUnknown command dude.\n"

    if your_hp == 0:
        print "You lost the battle! Game over. Boo-hoo."
        exit(0)
    else:
        print "Knight #%d has been crushed! Hooray!\n" % knight_stats[0]

def first_floor_right(): # A silly function to give player a "choice".
    clear_console()
    print "\nPrince: Let's head right then."
    cont()
    print "Cloverfield: Roger that, sir."
    cont()
    print "Our heroes head forward, passing by all sort of rooms and prison cells. They see horrible things inside."
    cont()
    print "However, they are not scared because they have one goal: defeat the king."
    cont()
    print "Prince: There's a large door up ahead. It seems to be locked. What do we do? Open it or return?\n"

    while True:
        answer = raw_input("> ")
        if answer == "open":
            print "\nA giant troll appears. It eats you both in one bite.\n"
            print "Game over, I guess."
            exit(0)
        elif answer == "return":
            break
        else:
            print "\nWhat?\n"
    return None

def cont(): # My way to deal with the "press enter to continue" problem. Should work well for people who want to play.
    cont = raw_input("")
    if cont == "":
        pass
    else:
        print "\nPlease don't enter characters before hitting enter. Thank you."
    return None

clear_console() # This simply clears the cmd screen.
#battle(100,100)

# Intro
print "\nIntroduction:\n"
print "A young heir to the throne is sitting in his room. He hates his father, and wants to become king. Why? That's none of your business. All you have to know is that you will be guiding him on this quest."
cont()
print "The prince's father resides in his room, which is located in the highest tower of the castle. He is fatally ill, and rarely leaves the room, if at all."
cont()
print "Guarding the path to this lone room are the king's faithful Tower Knights. There are 10 of these knights, each one stronger than the knight before him."
cont()
print "Your personal bodyguard, Sir Cloverfield, will give you a helping hand, if you need it. He is waiting outside the door."
cont()
print "Good luck, young prince. The road ahead of you is long and perilous...."
cont()

clear_console()

# First dialogue, approach to staircase
print "\nA sword and shield lay at the foot of the prince's bed. He picks them up, and heads towards the door. He knows that there is no turning back...."
cont()
print "Cloverfield: I've been waiting for you, young master. Shall we be on our way now?"
cont()
print "Prince: Yes, Cloverfield. We shall begin now. Keep your sword sheathed, so as to not direct attention towards us."
cont()
print "Cloverfield: I understand, sir."
cont()
print "The two cautiously proceed to the northern staircase. This will take them to the next floor. The king's room is 5 floors above our heroes."
cont()
print "Why is the prince cautious, you say? Long story short, he's under \"room-arrest\". No kidding. The reason? It's bad."
cont()

clear_console()

# Prelude to fight with #10
print "\nCloverfield: Sir, there seems to be a knight in the middle of the staircase. I doubt he'll let us pass, without a fight of course."
cont()
print "Prince: Well, I must do it, in order to reach the king."
cont()
print "Tower Knight #10: I've been expecting you, prince. The king's orders were clear: bring my son to me, dead or alive."
cont()
print "Prince: He did? Well, he'll pay for that later. Right now, you're going to be punished."
cont()

clear_console()

# Battle #10, intro to battle system
print "\nWelcome to Battle Mode! In this mode, you will be able to execute attacks, heal yourself, or defend against an approaching attack."
cont()
print "This is an RPG, so battles will be of a turn-by-turn fashion. For instance, if you defend, you can't attack. The same goes for potions and what-not."
cont()
print "Therefore, you must plan out what you will do properly, or else you will die."
cont()
print "If you need help at any moment during battle, simple use the help command to see what you can do."
cont()
print "Death in a battle will result in a game over, which is why you should be extremely careful."
cont()
print "Enjoy the battle!"

clear_console()
battle(1,1)
clear_console()

# After battle is won
print "Prince: We won the battle. Only 6 knights to go, it seems."
cont()
print "Cloverfield: That is indeed true, sir."
cont()
print "Prince: So... where do we go now?"
cont()

print "Like I said, YOU will guide this crappy prince. So, where will it be: left or right?\n"
while True:
    result = raw_input("> ")
    if result == "right":
        first_floor_right()
    elif result == "left":
        break
    else:
        print "\nNo such thing exists in this context. Try again please\n."

print "\nPrince: Left it is then. Let us make us make haste, Cloverfield."
cont()
print "The duo walk for a while, until they reach a passageway blocked by a sturdy Tower Knight. He is #4, obviously."
cont()
print "Tower Knight #4: LOL. Wth you doing here? You should be in your room! Oh wait, the king did in fact mention somethin' about this..."
cont()
print "I forgot... well, you are his son, so you may pass."
cont()
print "Prince and Cloverfield: o.0"
cont()
print "Prince: Thanks.."
cont()

clear_console()
