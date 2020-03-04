#!/usr/bin/python

import argparse


def find_max_profit(prices):
    p = len(prices)
    # We are only accepting arrays of prices
    if p < 2:
        return 0

    # Initialize lowest and highest
    low = prices[0]
    capitalism = prices[1] - prices[0]

    # Loop through the array of prices
    for i in range(1, p):
        # Set price to run through the array
        price = prices[i]
        # While running through we get profits by calculating the current price against the old lowest val
        profits = price - low
        # Low and max will only return the lowest/highest value, keeping accurate count of the actual min/max
        low = min(low, price)
        capitalism = max(profits, capitalism)

    return capitalism


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
