import itertools

with open("day1/input", "r") as fh:
    lines = [int(l) for l in fh.readlines()]

comb = itertools.combinations(lines, 3)
comb = [(a, b, c) for a, b, c in comb if a + b + c == 2020]
print(comb[0][0] * comb[0][1] * comb[0][2])
