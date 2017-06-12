class room():

    def __init__(self, name, description, entrances):
        self.name = name
        self.description = description
        self.entrances = entrances

    def __str__(self):
        return "You are in the " + self.name + "\n" + self.description

    def can_enter(self, direction):
        inverse_direction = {"n":"s", "s":"n", "w":"e", "e":"w"}
        direction = inverse_direction[direction]

        if direction in self.entrances:
            return True

def main():
    """
    Runs the main body of the program
    """
    map = generate_map()
    play_game(map)

def generate_map():
    # Define Rooms
    entrance = room("Entrance", "The shimmering metal doors deter you from entering, especially because of the rain. But you have a job. ", ["n"])
    corridor_1 = room("Corridor", "As the doors slide open, the incandescent lights of the corridor blink on, highlighting the rusty metal tunnel", ["n","e"])
    computer_room_1 = room("Computer_Room", "You see computational relics gently whirring in the stark darkness.", ["w"])

    room_grid = [[entrance, None],
                 [corridor_1, computer_room_1]]

    return room_grid

def check_move(map, new_room, direction):
    x = new_room["x"]
    y = new_room["y"]


    # Check if room exists
    try:
        map[y][x]

    except IndexError:
        return False

    if x < 0 or y < 0:
        return False

    elif map[y][x] == None:
        return False

    # Check if can enter that room
    elif not map[y][x].can_enter(direction):
        return False

    return True

def do_move(direction):
    move_x = 0
    move_y = 0

    if direction == "n":
        move_y = -1

    elif direction == "s":
        move_y = 1

    elif direction == "w":
        move_x = -1
    elif direction == "e":
        move_x = 1

    return {"x":move_x, "y":move_y}

def get_move():
    while True:
        direction = input("Enter a direction: ").lower()
        if direction not in ["n", "s", "w", "e"]:
            print("You must move  a valid direction (n, s, w, e)")

        else:
            break

    return direction

def display_room(map, room):
    x = room["x"]
    y = room["y"]

    print(map[x][y])

def play_game(map):

    current_room = {"x":0, "y":0}
    game_over = False

    while not game_over:
        display_room(map, current_room)
        while True:
            direction = get_move()
            move = do_move(direction)
            new_room = {"x": current_room["x"] + move["x"], "y": current_room["y"] + move["y"]}

            if check_move(map, new_room, direction):
                current_room["x"] = new_room["x"]
                current_room["y"] = new_room["y"]
                break

            else:
                print("Can't go that way.")

        if game_over:
            break
    """
    if won:
        print(win_msg)

    else:
        print(lost_msg)
    """

main()
