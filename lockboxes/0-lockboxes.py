#!/usr/bin/python3

def canUnlockAll(boxes):
    limit = len(boxes)
    temp = [0]
    second_temp = set(range(limit))

    while temp:
        current_box = temp.pop()
        second_temp.discard(current_box)

        for key in boxes[current_box]:
            if key < limit and key in second_temp:
                temp.append(key)

    return len(second_temp) == 0
