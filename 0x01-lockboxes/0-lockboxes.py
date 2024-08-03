#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    keysNow = {0} | set(boxes[0])
    newKeys = set()
    boxesLen = len(boxes)
    reachedIdx = 0
    while (reachedIdx != len(keysNow)):
        for key in keysNow:
            newKeys.update(set(boxes[key]))
        reachedIdx = len(keysNow)
        keysNow.update(newKeys)
        newKeys = set()
    ignoreKeys = 0
    for key in keysNow:
        if (key >= boxesLen):
            ignoreKeys += 1
    if (reachedIdx - ignoreKeys == boxesLen):
        return True
    return False
