import os
from random import *

class Room():
    """Room Class represents a room in the game"""

    # Define line length for printing, so that each line is only 40 characters long
    line_limit = 70

    def __init__(self, name, description, entrances, item=None, npc=None):
        """
        Create a new room
        :param name: Name of the room
        :param description: Description of the room
        :param entrances: Which compass directions the room can be entered from
        :param enemy: What enemy is present in the room(defaults to none)
        """

        self.name = name
        self.description = description
        self.entrances = entrances
        self.npc = npc

    def __str__(self):
        """
        :return: The name and the description of a room after formatting
        """
        description_formatted = text_format(self.description, self.line_limit)

        return "You are in the " + self.name + "\n" + description_formatted

    def can_enter(self, direction):
        """
        Checks if you can enter this room by moving from another room with a certain direction
        :param direction: Direction from other room
        :return: Whether or not player can enter by moving from that direction
        """

        # Make a direction with all of the compass directions inverted so that we can see if the current room has an
        # Entrance that allows player to enter
        inverse_direction = {"n": "s", "s": "n", "w": "e", "e": "w"}
        direction = inverse_direction[direction]

        # Checks if the inverted direction is in the list of possible entrances
        if direction in self.entrances:
            return True

class Player():
    """Creates a player object"""

    def __init__(self, name, hp, energy, current_room, inventory):
        """
        :param name: Name of the character
        :param hp: amount of hp the player has
        :param current_room: The dictionary that holds the coordinates of the room that the player is currently in
        """
        self.name = name
        self.hp = hp
        self.energy = energy
        self.current_room = current_room
        self.inventory = inventory
    """
    def hp_update(self, hp_change):
        ""
        Updates the players hp to any changes
        :param hp_change: Amount of hp change(positive for increase and negative for a decrease)
        :return: None
        ""

        # Apply the change in hp
        self.hp += hp_change

        # Set player's hp to zero if it is below zero
        if self.hp < 0:
            self.hp = 0
    """
    def action(self, other):
        items = [self.inventory[i] for i in range(len(self.inventory))]

        print("You use " + item[0])
        other.hp -= attack[1]
        self.hp += attack[2]
        other.energy -= attack[3]

class NPC():
    """Creates an enemy object"""

    def __init__(self, name, hp, opening_statement, attacks, death_statement):
        """
        :param name: Name of the eneemy
        :param hp: amount of health the enemy has
        :param opening_statement: The opening statement the enemy makes
        :param attacks: The attacks that the npc does. It is a list of the attacks they do in the format of:
            [["attack name", hp taken away, hp gained, charge taken away]]
        :param death_statement: What is printed when the enemy is defeated
        """
        self.name = name
        self.hp = hp
        self.opening_statement = opening_statement
        self.attacks = attacks
        self.death_statement = death_statement

    def do_opening_statement(self):
        print(self.opening_statement)

    def do_attack(self, other):
        attack = random.ranint(0, len(self.attacks)-1)
        print(self.name + " uses " + attack[0])
        other.hp -= attack[1]
        self.hp += attack[2]
        other.energy -= attack[3]

    def do_death_statement(self):
        print(self.death_statement)

class Stairs(Room):
    """Creates a Stairs child of the Room class"""

    def check_go_up(self):
        """
        Check if player wants to go up
        :return: Whether or not the player wants to go up
        """

        # Repeatedly ask whether the player wants to go up or not, continue if player does not enter a valid input
        while True:
            ask_up_down = input("Go up? y/n:")

            if ask_up_down == "y":
                return True
            elif ask_up_down == "n":
                return False
            else:
                print("Error. Please Enter a valid input")

class Item():
    """An item that can be found and the player can carry that changes stats"""
    def __init__(self, name="name", attacks=[["attack",10,10,10]]):
        self.name = name

    def __str__(self):
        return self.name


def text_format(text, line_limit):
    """
    This function formats text so that it is seperated into multiple lines
    :param text: The text that is to be formatted
    :param line_limit: The limit of the length of one line
    :return: The formatted text
    """

    # Split the word into a list of words
    word_list = text.split(" ")

    # Set the length of the current line to 0 characters
    current_line_length = 0

    # Iterate through each word
    for i in range(len(word_list)):

        # Iterate through the letters of each word
        for j in range(len(word_list[i])):

            # Increment current_line_length with each letter
            current_line_length += 1

            # If current_line_length exceeds the line_limit, then add a newline to the previous word and set
            # current_line_length to zero.
            if current_line_length > line_limit:
                word_list[i] = word_list[i] + "\n"
                current_line_length = 0
                j = 0

    text = " ".join(word_list)

    text = text.replace("\n ", "\n")

    return text

def generate_map():
    smithbot_list = generate_npc()

    # Define Rooms
    # Floor 1
    entrance = Room("Entrance", "The shimmering metal doors deter you from entering, especially because of the rain. But you have a job. ", ["n"])
    bistro = Room("Bistro", "Gang members smoke at their bar stools sharing details of their day", ["e"])
    corridor_1 = Room("Corridor", "As the doors slide open, the incandescent lights of the corridor blink on, highlighting the rusty metal tunnel", ["n", "s", "w"])
    mech_turk_room = Room("Mechanical Turk Room", "As you key in your stolen pass to your door, the doors slide open, you see hundreds upon hundreds of rows of poor good-for nothings hammering away at their keyboards. You mutter to yourself: \"They're probably all doing this to pay off their debts to the middle brother for buying too much ESCP.\"", ["e"])
    corridor_2 = Room("Corridor", "As you walk through the rusted steel doors, piles of long-forgotten machinery fall through the dark shelves in the shadows.", ["n", "s", "w", "e"])
    server_room = Room("Server Room", "You see dusty computational relics gently whirring in the stark darkness.", ["w"])
    office_1 = Room("Office", "Insert description", ["e", "s"])
    front_desk = Room("Front Desk", "Insert description", ["n", "e", "w"])
    corridor_3 = Room("Corridor", "Insert description", ["w", "s"])
    office_2 = Room("Office", "Insert description", ["n"])

    Elevator = Stairs("Elevator", "Insert description", ["n"])
    # Floor 2


    # Position Rooms
    map = \
    [
        [  # Floor 0
            [None, entrance, None],
            [bistro, corridor_1, None],
            [mech_turk_room, corridor_2, server_room],
            [office_1, front_desk, corridor_3],
            [office_2, None, Elevator]
        ],
        [  # Floor 0
            [None, entrance, None],
            [bistro, corridor_1, None],
            [mech_turk_room, corridor_2, server_room],
            [office_1, front_desk, corridor_3],
            [office_2, None, Elevator]
        ],
        """
        [ # Floor 1
            [None, balcony, None],
            [corridor_7, office_3, None],
            [corridor_6, little_brother_room, gun_hold],
            [corridor_5, corridor_4, corridor_3],
            [mechanical_slaves, None, broken_elevator]
        ],
        [ # Floor 2
            [None, open_air, None],
            [corridor_8, office_4, None],
            [corridor_9, middle_brother_room, torture_room],
            [corridor_10, corridor_11, torture_implements],
            [elevator_2, None, broken_elevator_shaft],
        ],
        [ # Floor 3
            [None, None, None],
            [bacta tank, hostage_room, big_brother_room],
            [corridor_12, office_5, toy_room],
            [mechanical_slave_parts, cash_stash, food_room],
            [mechanical_slaves, None, broken_elevator],
        ]
        [ # Floor 4
            heli_pad
        ]
        """
    ]

    return map

def generate_npc():
    smithbot_amount = 3
    smithbot_attack = [["SMITH SMASH!!", 5, 0, 0], ["SMITH HEAL", 0, 4, 0], ["SMITH LEACH",0,1,4]]
    smithbot_starting_phrase = ["Bwhahahahaha, you thought you could win! But I am here", "HAHAHAHAH BEEP BOOP", "DIE GOVERNMENT AGENDT SCUM", "I'LL RAM YOU iwth DDR4"]
    smithbot_death_phrase = ["AGHHH you got me!!", "DARN MY CIRCUITRY IS FRIED", "MY ALU CAN NO LONGER FETCH AND DECODE", "AGHHHH I NEED MORE RAM"]
    smithbots = []
    for i in range(smithbot_amount):
        smithbot = NPC("Smithbot Mark " + str(i+1),100, smithbot_starting_phrase[i], smithbot_attack, smithbot_death_phrase[i])
        smithbots.append(smithbot)
    return smithbots

def display_room(map, room):
    """
    Displays the text of the current room
    :param map: The map
    :param room: The coordinates of the room =
    """
    x = room["x"]
    y = room["y"]
    z = room["z"]

    print(map[z][y][x])
    #print(type(map[z][y][x]))

def display_player_stats(map, player):
    name = "Agent " + player.name

    bar = "||||||||||"
    health_bar = ["[", bar[:int(round(player.hp/10.0, 0))], "]"]
    health_bar = "".join(health_bar)

    energy_bar = ["[", bar[:int(round(player.energy/10.0, 0))],  "]"]
    energy_bar = "".join(energy_bar)

    inventory = player.inventory
    inventory_placeholder = "___________"
    for i in range(len(inventory)):
        if inventory[i] == None:
            inventory[i] = inventory_placeholder

    inventory = " | ".join(inventory)

    print("")
    print("{0:<10}{1:>15}".format("Name: ", name))
    print("{0:<10}{1:>15}".format("Shield: ", health_bar))
    print("{0:<10}{1:>15}".format("Energy: ", energy_bar))
    print("{0:<10}{1:>15}".format("Inventory: ", inventory))
    print("")

def get_move():
    """
    Receives input from the user telling which compass direction they want the player to move
    :return: The direction the player goes (n, s, w, e)
    """

    # Repeatedly ask the user for a direction until they enter a valid one
    while True:

        # Get input from user
        direction = input("\nEnter a direction: ").lower()

        # Break if input is valid
        if direction in ["n", "s", "w", "e"]:
            break

        # Print an error message and continue if it is not correct
        else:
            print("You must move  a valid direction (n, s, w, e)")

    return direction

def do_move(direction):
    """
    A function that returns the change in coordinates based on moving a certain direction
    :param direction: A compass direction(n, s, w, e)
    :return: the coordinates the player is going to move(x,y)
    """

    # Define the movement variables
    move_x = 0
    move_y = 0

    # Check which direction the player is moving and change the movement variables accordingly
    if direction == "n":
        move_y = -1

    elif direction == "s":
        move_y = 1

    elif direction == "w":
        move_x = -1
    elif direction == "e":
        move_x = 1

    # Return the dictionary of the change in position
    return {"x": move_x, "y": move_y}

def check_move(map, new_room, direction):
    """
    Checks if move is valid
    :param map: The map
    :param new_room: The room that the player will be in after the potential move
    :param direction: The direction that the user inputted
    :return: Whether or not the move is valid
    """

    # Define variables
    x = new_room["x"]
    y = new_room["y"]
    z = new_room["z"]



    # Check if room exists
    try:
        map[z][y][x]

    # if it doesn't return false
    except IndexError:
        return False

    # If the room is a negative number, return False
    if x < 0 or y < 0:
        return False

    # If the room is a None placeholder, return False
    elif map[z][y][x] == None:
        return False

    # Check if can enter that room
    elif not map[z][y][x].can_enter(direction):
        return False

    # If all of the previous checks weren't triggered, then the player can enter that room
    return True

def check_stairs_go_up(map, current_room):
    """
    Checks whether the current room is a stair room or not
    :return: Whether or not the player is in a stairs room
    """
    x = current_room["x"]
    y = current_room["y"]
    z = current_room["z"]

    # Check if the room is actually stairs
    if str(type(map[z][y][x])) ==  "<class '__main__.Stairs'>":
        if map[z][y][x].check_go_up:
            return True
        else:
            return False

    else:
        return False

def play_game(map):
    """
    The game loop
    :param map: The map the game is to be played on
    :return: Whether or not the player won or not
    """

    # Define variables
    line_limit = 70
    first_room = {"x": 1, "y": 0, "z": 0}
    game_over = False
    won = False

    # Display number of levels
    display_level = ["1", "224", "343", "987", "Roof"]

    # Result messages
    win_msg = "Mission successful."
    loss_msg = "Mission failed."

    # Ask user for player name
    my_name = input("For sector 6 authorization to initiate mission, enter your name: ")

    # Starting Messages
    print(text_format("Hello agent " + my_name + " we at sector 6 apologize for the inconvenience of delivering a rather... delicate mission to you in such a short time frame.", line_limit))
    print("")
    print("Floor 1")

    # Player
    my_player = Player(my_name, 100, 100, first_room, ["Phaser", "Stimpak", None])

    # Game loop
    while not game_over:

        # Display the current room
        display_room(map, my_player.current_room)

        # TODO: Draw map
        # draw_map(map)

        # Display player_stats
        display_player_stats(map, my_player)

        # Check if player is currently in a stair room and ask if player wants to ascend
        if check_stairs_go_up(map, my_player.current_room):
            my_player.current_room["z"] += 1
            print("")
            print("Floor ", display_level[my_player.current_room["z"]])
            print("")
            continue

        # TODO: Check if there is an enemy
        if check_npc(map, current_room):

            # fight_loop
                # NPC attack
                # Give player options

                #player attack
                # break when player.hp>0

        # TODO: Check if there is an item
        # if check_item(map, current_room):
            # check_item_add

        # Repeatedly ask the user for a move until they enter a valid one
        while True:

            # Query user for the direction they wish to move
            direction = get_move()

            # Get the coordinate direction for the move
            move = do_move(direction)

            # Set the new_room with the coordinates of the new room the player will be in after instigating the move
            new_room = {"x": my_player.current_room["x"] + move["x"], "y": my_player.current_room["y"] + move["y"], "z": my_player.current_room["z"]}

            # Check if the move is valid
            if check_move(map, new_room, direction):

                # If it is valid, then set the current_room to the new_room coordinates and break out of this loop
                my_player.current_room["x"] = new_room["x"]
                my_player.current_room["y"] = new_room["y"]
                break

            # If the move is invalid, print an error message and continue
            else:
                print("Can't go that way.")

        # TODO: Check if the game is over

        #clear()

    # Check won/lost
    """
    # If the player won, display the winning message
    if won:
        print(win_msg)

    # If the player lost display the losing message
    else:
        print(lost_msg)
    """

def check_won():
    """
    Check if the player won
    :return:
    """

    # Check if the player's hp is less than or equal to zero
    if player.hp >= 0:
        return False

    elif boss.hp <= 0:
        return True

def main():
    """
    Runs the main body of the program
    """
    map = generate_map()
    play_game(map)

main()
