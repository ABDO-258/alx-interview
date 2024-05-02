#!/usr/bin/python3
""" locker box interview """


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened
    """
    opened = [0]  # the open box
    box = 0
    keys = []
    for key in boxes:
        if box not in opened:
            # print(box, 'still closed box')
            if box + 1 not in keys:
                return False
        keys.extend(key)
        if key not in opened or key not in keys:
            opened.extend(key)
        # print('keys')
        # print(keys)
        # print('open')
        # print(opened)
        # print('-----')
        # print(box)
        box += 1
    return True
