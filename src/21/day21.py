from src.problem import Problem
from itertools import chain


def part_a(foods: list):
    ingredients = list(chain.from_iterable([food[0] for food in foods]))
    allergen_map = map_allergens(foods)

    no_allergen = [ingredient for ingredient in ingredients if ingredient not in allergen_map.keys()]
    return len(no_allergen)


def part_b(foods: list):
    allergen_map = map_allergens(foods)

    sorted_ = dict(sorted(allergen_map.items(), key=lambda item: item[1]))
    return ','.join(sorted_.keys())


def map_allergens(foods: list):
    allergens = set(chain.from_iterable([food[1] for food in foods]))

    allergen_map = {}
    while len(allergens) > 0:
        for allergen in allergens:
            containing = [set(food[0]) for food in foods if allergen in food[1]]
            ingredient = set.intersection(*containing)

            if len(ingredient) == 1:
                ingredient = ingredient.pop()
                allergen_map[ingredient] = allergen
                for food in foods:
                    if ingredient in food[0]:
                        food[0].remove(ingredient)
        allergens.difference_update(allergen_map.values())
    return allergen_map


def load(p: Problem):
    foods = []
    for food in p.data():
        ingredients = food.split(' (')[0].split()
        allergens = food.split(' (')[1].replace('contains ', '').rstrip(')').split(', ')
        foods.append((ingredients, allergens))
    return foods


if __name__ == '__main__':
    problem = Problem(21, test=False)

    # print(part_a(load(problem)))
    # print(part_b(load(problem)))

    # problem.submit(part_a(load(problem)), 'a')
    # problem.submit(part_b(load(problem)), 'b')
