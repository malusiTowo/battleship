from Ship import Ship

"""
Board Class to hold players ships and to handle interaction with those ships
"""


class Board:
    player_one_ships = []
    player_two_ships = []

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.player_two_ships = [Ship(val + 2) for val in range(4)]
        self.player_one_ships = [Ship(val + 2) for val in range(4)]

    """
    Method to locate a specific ship for one of the players
    """

    def find_correct_ship_for_player(self, ships, ship_length):
        for ship in ships:
            if ship.ship_length == ship_length:
                return ship
        return

    """
    Method to place ship on board with position coordinates, once user has chosen location
    """

    def place_ship_for_player(self, player, ship_length, ship_positions):
        ships = self.player_one_ships if player == 1 else self.player_two_ships
        correct_ship = self.find_correct_ship_for_player(ships, ship_length)

        # TODO check if ship is found

        if correct_ship:
            correct_ship.set_ship_positions(ship_positions)

    """
    Method to called when user attempts to attack enemy ships
    """

    def attack_by_user(self, player, ship_position):
        ships = self.player_one_ships if player == 1 else self.player_two_ships
        attack_hit_ship = False

        for ship in ships:
            if (ship.check_hit(ship_position)):
                attack_hit_ship = True
                break

        return attack_hit_ship

    def are_enemies_ships_destroyed(self, player):
        ships = self.player_one_ships if player == 1 else self.player_two_ships
        ships_destroy_values = [ship.is_destroyed for ship in ships]
        are_all_ships_destroyed = bool(
            list(filter(lambda x: x, ships_destroy_values))
        )
        return are_all_ships_destroyed


# Init
# Give user list of 5 ships to place on board
# once user set ship on board set coords on ship and
# Board add new ship to list


# game loop
#  check whos turn
#  get user input position
#  iterate over ships on board to check if pos eq pos of ship then set to True
# if hit send message to client
# if hit and ship dead send message to client
# next turn
