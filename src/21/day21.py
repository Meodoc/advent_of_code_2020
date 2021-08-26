from src.problem import Problem
from collections import defaultdict
from itertools import chain
from copy import deepcopy


def part_a(foods: list):
    allergens = set(chain.from_iterable([food[1] for food in foods]))
    ingredients = list(chain.from_iterable([food[0] for food in foods]))

    allergen_map = {}
    while len(allergen_map) < len(allergens):
        for allergen in allergens:
            containing = [set(food[0]) for food in foods if allergen in food[1]]
            ingredient = containing[0].intersection(*containing)

            if len(ingredient) == 1:
                ingredient = ingredient.pop()
                allergen_map[ingredient] = allergen
                for food in foods:
                    if ingredient in food[0]:
                        food[0].remove(ingredient)

    no_allergen = [ingredient for ingredient in ingredients if ingredient not in allergen_map.keys()]
    return len(no_allergen)


def part_b(data: list):
    return None


def load(p: Problem):
    foods = []
    for food in p.data():
        ingredients = food.split(' (')[0].split(' ')
        allergens = food.split(' (')[1].replace('contains ', '').rstrip(')').split(', ')
        foods.append((ingredients, allergens))
    return foods


if __name__ == '__main__':
    problem = Problem(21, test=False)

    print(part_a(load(problem)))
    # print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
