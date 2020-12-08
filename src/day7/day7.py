from src.problem import Problem
from day7.bag import Bag

import pickle as pkl


def part_a():
    # Collect all parent nodes of all 'shiny gold bag' nodes
    containing_bags = set()
    for shiny_gold_bag in shiny_gold_bags:
        collect_parent_nodes(shiny_gold_bag.parent, containing_bags)
    return len(containing_bags)


def part_b():
    shiny_gold_bag = shiny_gold_bags[0]
    return collect_n_child_bags(shiny_gold_bag, 1)


def find_nodes(bag_name, root, found):
    if root is None:
        return
    if root == bag_name:
        found.append(root)
    for child in root.children:
        find_nodes(bag_name, child, found)


def collect_parent_nodes(bag, containing_bags):
    if not bag:
        return
    containing_bags.add(bag)
    collect_parent_nodes(bag.parent, containing_bags)


def collect_n_child_bags(node, multiplier):
    res = 0
    for child in node.children:
        res += node.amount[child.name] * multiplier
        res += collect_n_child_bags(child, node.amount[child.name] * multiplier)
    return res


def parse_nodes(data):
    nodes = dict()
    for line in data:
        name = line.split("contain")[0][:-2]
        children = list()
        for child in line.split("contain")[1][1:].split(", "):
            try:
                n = int(child[0])
            except:  # contains no other children
                continue
            child_name = child[2:]
            if child_name.endswith('.'):
                child_name = child_name[:-1]
            if child_name.endswith('s'):
                child_name = child_name[:-1]
            children.append((child_name, n))
        nodes[name] = children
    return nodes


def build_trees(entries):
    children = [child[0] for children in entries.items() for child in children[1]]  # Flatten children list
    roots = [entry[0] for entry in entries.items() if entry[0] not in children]  # Root elements are not in children
    return [build_tree(root, entries, None) for root in roots]


def build_tree(entry_name, entries, parent):
    entry = [entry for entry in entries.items() if entry[0] == entry_name][0]  # Find entry in list
    bag = Bag(entry[0], parent)
    for child in entry[1]:
        bag.children.add(build_tree(child[0], entries, bag))  # Add child bag
        bag.amount[child[0]] = int(child[1])  # Add amount of child bag
    return bag


def debug_print_entries(entries):
    with open('entries.txt', 'w') as fh:
        for entry in entries.items():
            node, children = entry
            fh.write(f"{node}: {children}\n")


def pickle_trees():
    entries = parse_nodes(problem.data())
    debug_print_entries(entries)
    trees = build_trees(entries)
    with open('trees.pkl', 'wb') as fh:
        pkl.dump(trees, fh)


def load():
    with open('trees.pkl', 'rb') as fh:
        return pkl.load(fh)


if __name__ == '__main__':
    problem = Problem(7)
    # pickle_trees()
    trees = load()

    # Collect every 'shiny gold bag' nodes in all trees
    shiny_gold_bags = list()
    for tree in trees:
        find_nodes('shiny gold bag', tree, shiny_gold_bags)

    problem.submit(part_a(), 'a')  # 124
    problem.submit(part_b(), 'b')  # 34862
