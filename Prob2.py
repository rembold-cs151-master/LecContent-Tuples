from positions import KAREL_POS


def interval_of_greatest_movement(position_list):
    """Returns the starting and ending times of the interval which was the largest
    movement in Karel's position.

    Args:
        position_list (list of tuples): The list of the position tuples, in time, x, y order
    Returns
        (tuple of int): The starting and ending times of the interval
    """


def enhance_records(position_list):
    """Enhances the records in the position list be add a boolean that indicates if
    Karel moves in the following interval.

    Args:
        position_list (list of tuples): The list of the position tuples, in time, x, y order
    Returns:
        None: The position_list is edited in place
    """


if __name__ == "__main__":
    print(interval_of_greatest_movement(KAREL_POS))

    ##Uncomment when ready for Part 2
    # enhance_records(KAREL_POS)
    # print(KAREL_POS)
