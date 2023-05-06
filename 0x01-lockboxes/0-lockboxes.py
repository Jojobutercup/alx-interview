#!/usr/bin/python3

"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box may
contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists containing keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False if the boxes cat be.
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for keys in boxes[n]:
            if keys not in unlocked and keys < len(boxes):
                unlocked.append(keys)
    if len(unlocked) == len(boxes):
        return True
    return False
