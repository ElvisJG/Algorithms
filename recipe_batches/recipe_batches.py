#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
    # None can also be used here
    possible = float('inf')
    # If the length of recipes is less than 1, kick out
    if len(recipe) < 1:
        return 0
    # For each component in a recipe
    for component in recipe:
        # use the key to get the value for each item in recipe
        needed = recipe[component]
        # map through the supplied ingredients, optionally returns 0 if key is not found
        supplied = ingredients.get(component, 0)
        # If the supplied ingredient is less than what is needed, return 0. The recipe cannot be made.
        if supplied < needed:
            return 0
        # If we are able to make a recipe, use floor division to get a whole int value
        abletomake = supplied // needed
        # recursively rerun individual components
        possible = min(abletomake, possible)

    # Return the possible amount of recipes
    return possible


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
