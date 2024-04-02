def directionToDirectionNumber(direction):
    """Converts a direction to a number.

    Args:
        direction: The direction to convert.

    Returns:
        The direction number.
    """

    if direction == "north":
        return 0
    elif direction == "east":
        return 1
    elif direction == "south":
        return 2
    elif direction == "west":
        return 3
    else:
        raise ValueError("Invalid direction: {}".format(direction))
