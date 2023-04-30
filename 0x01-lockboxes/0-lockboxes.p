#!/usr/bin/python3


def canUnlockAll(boxes):
    # Create a list to keep track of which boxes have been opened
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True  # The first box is already opened

    # Create a list to keep track of the keys that we have
    keys = [0]  # We start with the keys in the first box

    # While we have keys to use
    while keys:
        # Get the next key
        key = keys.pop()

        # Try to open all the boxes that this key can open
        for box in boxes[key]:
            if not opened_boxes[box]:
                opened_boxes[box] = True
                keys.append(box)

    # Check if all boxes have been opened
    return all(opened_boxes)
