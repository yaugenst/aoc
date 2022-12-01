#!/usr/bin/env python3

import re
from copy import deepcopy


def play(hands):
    while all(hands):
        draw = [hand.pop(0) for hand in hands]
        hands[draw.index(max(draw))] += sorted(draw)[::-1]
    return [hand for hand in hands if hand][0]


def score(hand):
    return sum([(idx + 1) * card for idx, card in enumerate(hand[::-1])])


def rec_play(hands, count=0):
    seen = set(str(hands))
    while all(hands):
        if str(hands) in seen:
            return 0
        seen.add(str(hands))
        draw = [hand.pop(0) for hand in hands]
        if all([len(hand) >= d for hand, d in zip(hands, draw)]):
            winner = rec_play([hand[:d] for hand, d in zip(hands, draw)], count + 1)
        else:
            winner = draw.index(max(draw))
        hands[winner] += [draw[winner], draw[1 - winner]]
    if count == 0:
        return [hand for hand in hands if hand][0]
    return 0 if hands[0] else 1


fp = "input.txt"
data = open(fp).read().split("\n\n")
hands = [
    [int(card) for card in re.findall(r"\d+", cards)]
    for cards in [line.split(":")[1] for line in data]
]


winner = play(deepcopy(hands))
print(score(winner))
winner = rec_play(deepcopy(hands))
print(score(winner))
