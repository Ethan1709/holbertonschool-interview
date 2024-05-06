#!/usr/bin/python3

def rain(walls):
    if not walls:
        return 0
    c = 0
    water = 0
    new = []
    for i in range(len(walls)):
        if walls[i] != 0:
            c = 0
            for j in range(i + 1, len(walls)):
                if walls[j] == 0:
                    c += 1
                else:
                    water = c * min(walls[i], walls[j])
                    new.append(water)
                    break
    return sum(new)
        