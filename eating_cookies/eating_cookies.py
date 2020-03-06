#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if cache is not None and cache[n]:
        return cache[n]

    if n == 0:
        if cache is not None:
            cache[n] = 1
        return 1

    total_ways = 0
    if n >= 3:
        total_ways += eating_cookies(n - 3, cache)

    if n >= 2:
        total_ways += eating_cookies(n - 2, cache)

    if n >= 1:
        total_ways += eating_cookies(n - 1, cache)

    if cache is not None:
        cache[n] = total_ways
    return total_ways


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
