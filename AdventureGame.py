import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1.5)


def intro():
    print_pause("\nThe biggest castle in the kingdom is having a "
                "contest.")
    print_pause("Knighthood and eternal fame will be granted to any "
                "brave \nsoul who defeats a creature in the Grand "
                "Arena.")
    print_pause("You are determined to win against any foe.")
    print_pause("You declare your place in the contest.")
    print_pause("You have arrived at the castle.")


def guild_master(items):
    print_pause("\nYou pay a visit to the guildmaster.")
    if "sword" in items:
        print_pause("Having already given you a good sword, the "
                    "guildmaster pauses.")
        print_pause("\"I have nothing more to give you. Be well!\" he says.")
        print_pause("He wishes you the best of luck in your endeavors.")
    else:
        print_pause("Surrounded by his fine metal creations, he says, ")
        print_pause("\"Many have perished in this contest before... but never "
                    "with one of my weapons.\"")
        print_pause("He lends you a sword to use in battle and bring "
                    "more notoriety to his name.")
        items.append("sword")
    print_pause("You return back to the main hall.")
    choose_path(items)


def visit_armoury(items):
    print_pause("\nYou wander into the Armoury of Champions.")
    if "shield" in items:
        print_pause("The armed guard welcomes you again.")
        print_pause("\"The shield in your possession will serve "
                    "you well.\"")
    else:
        print_pause("An armed guard welcomes you.")
        if "sword" in items:
            print_pause("A shield was reserved for you in the contest.")
            print_pause("The armed guard logs your visit.")
            print_pause("\"For the untrained warrior, a shield may be "
                        "the difference between life and death.")
            print_pause("To surpass the level of squire in a mere "
                        "contest is a test of will and luck.\"")
            print_pause("You are given a shield made mostly of bronze.")
            items.append("shield")
        else:
            print_pause("He tells you that only an armed competitor "
                        "may collect an item from the Armoury of "
                        "Champions.")
            print_pause("You are advised to return with a weapon, or "
                        "perish in the Arena with nothing.")
    print_pause("You return back to the main hall.")
    choose_path(items)


def enter_arena(items):
    creature_list = ["fire-breathing dragon", "deadly ogre",
                     "cruel witch"]
    creature = random.choice(creature_list)
    print_pause("\nYou make your way to the Grand Arena entrance.")
    print_pause("You are greeted by a scribe documenting the event.")
    print_pause("\"Heavens be with you. The newest addition to the "
                "Arena is a " + creature + "!\"")
    print_pause("An armed guard pushes you forward and closes the "
                "gates behind you.")
    if "sword" in items:
        print_pause("\nYou unsheathe your sword and prepare to fight.")
        if "shield" in items:
            print_pause("Now with the sword and shield staggered, you "
                        "advance toward your foe.")
            print_pause("Though the " + creature + " puts up a big "
                        "fight, you emerge victorious.")
            print_pause("You forced a surrender before a final "
                        "blow would be dealt.")
            victory()
        else:
            print_pause("Oops! You walked into the Arena without "
                        "anything to defend yourself!")
            print_pause("Without a shield, the " + creature +
                        " overpowers you in battle.")
            print_pause("Badly wounded, your life is spared.")
            print_pause("You live, but are expelled from the contest.")
            defeat()
    else:
        print_pause("\nOops! You walked into the Arena without a "
                    "weapon!")
        print_pause("With nothing to defend yourself, you cower.")
        print_pause("As the " + creature + " laughs, the armed "
                    "guards remove you.")
        print_pause("Though you live, you will never be allowed "
                    "to enter the Arena again.")
        print_pause("You leave the castle in shame.")
        defeat()


def choose_path(items):
    print_pause("\nPlease enter the number for the "
                "path you choose to take:\n")
    room_path = input("1. Consult with a Guildmaster\n"
                      "2. Visit the Armoury\n"
                      "3. Enter the Grand Arena\n\n")
    if room_path == '1':
        guild_master(items)
    elif room_path == '2':
        visit_armoury(items)
    elif room_path == '3':
        enter_arena(items)
    else:
        print_pause("\nThe following options will help in your pursuit.")
        choose_path(items)


def victory():
    print_pause("Victory is yours! The sword and shield proved "
                "their worth, as did you.")
    print_pause("The lord of the castle has deemed you to be "
                "worthy of knighthood.")
    print_pause("A ceremony will be initiated post-haste.")
    play_again()


def defeat():
    print_pause("\nUnfortunately, you did not succeed in the Grand Arena.")
    print_pause("The possibility of knighthood and eternal fame have "
                "eluded your grasp.")
    play_again()


def play_again():
    print_pause("\nGAME OVER")
    restart_option = input("\nWould you like to play again? (Enter "
                           "\"Yes\" to Restart or \"No\" to quit.) ")
    if restart_option.lower() == "yes":
        print_pause("\nOkay! The game will restart.")
        play_game()
    elif restart_option.lower() == "no":
        print_pause("\nThank you for playing! The game has ended.")
    else:
        play_again()


def play_game():
    items = []
    intro()
    choose_path(items)


play_game()
