#!/usr/bin/python3
"""
File for can unlock all boxes
"""


def canUnlockAll(boxes):
    """
    Function for unlock all boxes
    """
    if len(boxes) < 1:
        return True
    found_keys = []
    for box in range(len(boxes)):
        box_opened = False
        if box == 0:
            found_keys += boxes[0]
            box_opened = True
            continue

        for item in found_keys:
            if item == box:
                found_keys += boxes[box]
                box_opened = True
                break

        for keys in range((box + 1), len(boxes)):
            for eachbox in boxes[keys]:
                if eachbox == box:
                    found_keys += boxes[box]
                    box_opened = True
                    break
            break
        if box_opened is False:
            return False
    return True
