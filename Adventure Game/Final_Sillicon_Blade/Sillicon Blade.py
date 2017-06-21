import copy
import random

class Room():
    """Room Class represents a room in the game"""

    # Define line length for printing, so that each line is only 40 characters long
    line_limit = 70

    def __init__(self, name, description, entrances, npc=None):
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

    def hp_update(self):
        """
        Ensures that player's hp is never negative
        """

        # Set player's hp to zero if it is below zero
        if self.hp < 0:
            self.hp = 0

    def regen_energy(self):
        self.energy += 10

        if self.energy > 100:
            self.energy = 100

        elif self.energy < 0:
            self.energy = 0

    def action(self, other):
        inventory_copy = copy.deepcopy(self.inventory)
        while True:
            for i in range(len(inventory_copy)):
                for j in range(len(inventory_copy[i])):
                    inventory_copy[i][j] = str(inventory_copy[i][j])

                print("{0:<10}{1:>15}".format("Item " + str(i + 1) + " : ", "/".join(inventory_copy[i])))

            try:
                attack_number = int(input("Choose an item to use: "))
                attack = self.inventory[attack_number-1]

            except ValueError:
                print("Enter a valid item number.")
                continue

            break

        print("You use " + attack[0])
        other.hp -= attack[1]
        self.hp += attack[2]
        self.energy -= attack[3]

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

    def __str__(self):
        return self.name

    def do_opening_statement(self):
        print(self.opening_statement)

    def do_attack(self, other):
        attack = self.attacks[random.randint(0, len(self.attacks)-1)]
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
    # Generate the smithbots
    smithbot_list = generate_npc()

    # Define Rooms
    # Floor 0
    entrance = Room("Entrance", "Just as you leave the innocuous hovercar that brought you to the doorstep of the relatively infamous and shady Gaspire, the immense height of the building catches you by surprise. As you gaze up in front of you, you see the metallic spire stretches upwards for hundreds of floors. You gaze back down to your objective. The rusting metal doors deter you from entering, especially because of the rain. But you have a job. ", ["n"])
    bistro = Room("Bistro", "Gang members that were probably born into the Three Brothers gang along with regular office workers that are employed there to keep their mouths shut and their wallets open, are either eating or are in a NERVE induced stupor. The white noise of a restaurant permeates the space as they sit in their bar stools sharing details of their day", ["e"])
    corridor_1 = Room("Corridor", "As the doors slide open, the incandescent lights of the corridor suddenly confront you from behind the metal doors, highlighting the rusty metal tunnel and the Bistro to the s", ["n", "s", "w"])
    mech_turk_room = Room("Mechanical Turk Room", "As you key in your stolen pass to your door, the doors slide open, you see hundreds upon hundreds of rows of poor good-for nothings hammering away at their keyboards. You mutter to yourself: \"They're probably all doing this to pay off their debts to the middle brother for buying too much NERVE.\"", ["e"], smithbot_list[0])
    corridor_2 = Room("Corridor", "As you walk through the rusted steel doors, piles of long-forgotten machinery fall through the dark shelves in the shadows.", ["n", "s", "w", "e"])
    server_room = Room("Server Room", "You see dusty computational relics gently whirring in the stark darkness.", ["w"])
    office_1 = Room("Office", "Mafia bureaucrats look up from their work as you walk through, but they forget you were even there due to the sheer load of work that they receive", ["e", "s"], smithbot_list[2])
    front_desk = Room("Front Desk", "As you walk towards the front desk of the building, you see an office on the west wing and a corridor leading to an elevator on the right. However, you realize too late that the receptionist is actually a Smithbot", ["n", "e", "w"], smithbot_list[1])
    corridor_3 = Room("Corridor", "The indu", ["w", "s"])
    office_2 = Room("Office", "Insert description", ["n"])

    elevator = Stairs("Elevator", "You see an elevator and enter it to get closer to the objective of your mission", ["n"])
    # Floor 1
    corridor_4 = Room("Corridor", "Insert description", ["n", "s", "w", "e"])
    corridor_5 = Room("Corridor", "Insert description", ["n", "s", "w", "e"])
    corridor_6 = Room("Corridor", "Insert description", ["n", "s", "w", "e"])
    corridor_7 = Room("Corridor", "Insert description", ["n", "s", "w", "e"])
    corridor_8 = Room("Corridor", "Insert description", ["n", "s", "w", "e"])
    mechanical_slaves = Room("Mechanical Slave Room", "Insert description", ["n"])
    gun_hold = Room("Armory", "Insert description", ["w"])
    broken_elevator_1 = Room("Broken Elevator Shaft", "Insert description", ["n"])
    office_3 = Room("Office", "Insert description", ["w"])

    balcony = Stairs("Balcony", "Insert description", ["s"])

    # Floor 2
    open_air = Room("Open Air", "Insert description", [])
    little_brother_room = Room("The Little Brother's Office", "Insert description", ["e"])
    torture_room = Room("Mechanical Encouragement Room 23", "Insert description", ["w", "s"])
    corridor_9 = Room("Corridor", "Insert description", ["n", "w", "e"])
    broken_elevator_2 = Room("Broken elevator shaft", "Insert description", ["e"])

    rooftop_access = Stairs("Rooftop Access Stairs", "Insert description", ["n"])

    # Floor 3
    heli_pad = Room("Helicopter Pad", "Insert description", [])

    # Position Rooms
    map = \
    [
        [  # Floor 0
            [None, entrance, None],
            [bistro, corridor_1, None],
            [mech_turk_room, corridor_2, server_room],
            [office_1, front_desk, corridor_3],
            [office_2, None, elevator]
        ],
        [ # Floor 1
            [None, balcony, None],
            [corridor_8, office_3],
            [corridor_7, gun_hold],
            [corridor_6, corridor_5, corridor_4],
            [mechanical_slaves, None, broken_elevator_1]
        ],
        [ # Floor 2
            [None, open_air, None],
            [little_brother_room, corridor_9, torture_room],
            [rooftop_access, None, broken_elevator_2],
        ],
        [ # Floor 3
            [None, None, None],
            [None, None, None],
            [heli_pad, None, None],
        ]
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

def display_player_stats(character):
    character = copy.deepcopy(character)
    name = "Agent " + character.name

    bar = "||||||||||"
    health_bar = ["[", bar[:int(round(character.hp/10.0, 0))], "]"]
    health_bar = "".join(health_bar)

    energy_bar = ["[", bar[:int(round(character.energy/10.0, 0))],  "]"]
    energy_bar = "".join(energy_bar)

    inventory = character.inventory
    # inventory_placeholder = "___________"
    for i in range(len(inventory)):
        for j in range(len(inventory[i])):
            inventory[i][j] = str(inventory[i][j])

        inventory[i] = "/".join(inventory[i])

        """
        if inventory[i] == None:
            inventory[i] = inventory_placeholder
        """

    inventory = " | ".join(inventory)

    print("")
    print("{0:<10}{1:>15}".format("Name: ", name))
    print("{0:<10}{1:>15}".format("Shield: ", health_bar))
    print("{0:<10}{1:>15}".format("Energy: ", energy_bar))
    print("{0:<10}{1:>15}".format("Inventory(damage/heal/energy cost): ", inventory))
    print("")

def display_npc_stats(character):
    character = copy.deepcopy(character)
    name = character.name

    bar = "||||||||||"
    empty_bar = "          "
    
    health_bar_length = int(round(character.hp/10.0, 0))
    health_bar = ["[", bar[:health_bar_length], empty_bar[:health_bar_length - 10], "]"]
    health_bar = "".join(health_bar)

    print("")
    print("{0:<10}{1:>15}".format("Name: ", name))
    print("{0:<10}{1:>15}".format("Shield: ", health_bar))
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
        if map[z][y][x].check_go_up():
            return True
        else:
            return False

    else:
        return False

def check_npc(map, current_room):
    x = current_room["x"]
    y = current_room["y"]
    z = current_room["z"]

    if map[z][y][x].npc != None:
        return True

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
    clear()

    # Starting Messages
    print("")
    print(text_format("Hello agent " + my_name + ", we at sector 6 apologize for the inconvenience of delivering a rather... delicate mission to you in such a short time frame. However we trust that you will take it very seriously given your, ah, very reassuring track record. The target is the Little Brother, the youngest of the Three Brother's gang. Wanted for the abuse of sentient AI, trafficking of NERVE drugs, and several accounts of assault, coercion, and assassination of high-profile figures.", line_limit))
    print("")
    print(text_format("Our inside agents have finally gotten leads to where he is located. Currently, he is located in the Galspire tower of the Rhodium district. We're providing you with a Silicon Blade, because we are expecting resistance from his entourage of Smithbots and of course the Little Brother Himself.", line_limit))
    print("")
    while True:
        accept = input("Do you accept your mission? (y/n)")
        if accept == "y":
            print(text_format("Splendid. We'll be sending you to the Galspire entrance with all of your equipment. There will be a helicopter evac ready to meet you at a moment's notice on the roof once your finished with your mission", line_limit))
            break
        elif accept == "y":
            print(text_format("Ah. We prepared for this eventuality, so we freezed all your assets. You aren't going to regain control of them until you accomplish this mission. We'll be sending you to the Galspire entrance with all of your equipment. There will be a helicopter evac ready to meet you at a moment's notice on the roof once your finished with your mission", line_limit))
            break
        else:
            print("please enter a valid input.")

    clear()

    print("")
    print("Floor 1")
    print("")

    # Create Player object
    my_player = Player(my_name, 100, 100, first_room, [["Phaser",30,0,10], ["Stimpak",0,10,10]])

    # Game loop
    while not game_over:

        # Define more convenient variables to hold the player's coordinates
        x = my_player.current_room["x"]
        y = my_player.current_room["y"]
        z = my_player.current_room["z"]

        # Display the current room
        display_room(map, my_player.current_room)

        # Check if there is an npc
        if check_npc(map, my_player.current_room):

            # define a temporary variable to hold the id of the npc
            current_npc = map[z][y][x].npc

            # Check if npc is dead
            if not(current_npc.hp < 0):

                # Display the npc's opening statement
                current_npc.do_opening_statement()
                while not(my_player.hp < 0 or current_npc.hp < 0):


                    # Show npc stats
                    display_npc_stats(current_npc)

                    # Have npc  attack
                    current_npc.do_attack(my_player)
                    if my_player.hp < 0:
                        return False
                    # Show player stats
                    display_player_stats(my_player)

                    # Have Player perform a move
                    my_player.action(current_npc)

                    # Regenerate player energy after move
                    print("Regenerated energy! +10 energy!")
                    my_player.regen_energy()
                    clear()

                if my_player.hp < 0:
                    return False

                if current_npc.hp < 0:
                    current_npc.do_death_statement

        # Display player_stats
        display_player_stats(my_player)

        # Check if player is currently in a stair room and ask if player wants to ascend
        if check_stairs_go_up(map, my_player.current_room):
            clear()
            my_player.current_room["z"] += 1

            # Print out the new floor's display name
            print("")
            print("Floor ", display_level[my_player.current_room["z"]])
            print("")

            # Go back to the top of the loop so that the new room on the new floor can be displayed
            continue

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

        clear()


def check_won(map):
    """
    Check if the player won
    :return:
    """

    # Check if the player's hp is less than or equal to zero
    if player.hp >= 0:
        return False

    elif boss.hp <= 0:
        return True

def display_opening_message():
    file = open("opening_message", "r")
    msg = file.read()
    print(msg)

def clear():
    print("\n"*50)

def main():
    """
    Runs the main body of the program
    """

    # define the clear function


    # Display the opening message that is stored in a seperate file
    display_opening_message()

    # Generates the map with all of the rooms and characters inside of it
    map = generate_map()

    # Initiates game loop
    play_game(map)

main()
