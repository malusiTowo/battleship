"""
Ship Class to present a single ship on the board
"""


class Ship:
    is_destroyed = False
    is_valid = False

    def __init__(self, ship_length):
        self.ship_length = ship_length

    """
     Method to set position coords and health for ship
    """

    def set_ship_positions(self, ship_positions):
        # TODO: check if ship_length eq to len of ship positions
        self.is_valid = True
        self.ship_positions = ship_positions
        self.health_per_positions = {
            item: False for item in ship_positions
        }

    """
    Method to check if are positions of ship have been hit and set is_destroyed if destroyed
    """

    def check_destroyed(self):
        health_by_pos = [val for val in self.health_per_positions.values()]
        are_all_pos_hit = bool(list(filter(lambda x: x, health_by_pos)))
        if are_all_pos_hit:
            self.is_destroyed = True
        return are_all_pos_hit

    """
     Method to check if incoming attack hits ship returns the ship's health status
    """

    # TODO return more than boolean
    # TODO to indicate when the ship is destroyed
    def check_hit(self, incoming_position):
        for health_per_position_key in self.health_per_positions.keys():
            is_hit = incoming_position == health_per_position_key
            if is_hit:
                self.health_per_positions[incoming_position] = True

                self.check_destroyed()
                return True
        return False
