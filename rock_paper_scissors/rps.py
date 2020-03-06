#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # Define possible moves
    moves = [['rock'], ['paper'], ['scissors']]

    # 0 moves returns an empty list
    if n == 0:
        return [[]]

    # If only one round, return the base set of moves
    if n == 1:
        return moves

    result = []
    # Recursively call function and countdown from the initial given n value
    countdown = rock_paper_scissors(n - 1)
    # Loop through countdown and use the move set from the next series
    for inside in countdown:
        # For every move in moves
        for move in moves:
            # a possible move is created by concatenating the inner list with the move
            possiblemove = inside + move
            # append the possible move(s) to the result of our function
            result.append(possiblemove)

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
