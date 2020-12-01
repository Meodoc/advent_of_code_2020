import itertools

with open("day1/input", "r") as fh:
    lines = fh.readlines()

comb = itertools.combinations(lines, 2)
comb = [(int(a), int(b)) for a, b in comb if int(a) + int(b) == 2020]
print(comb[0][0] * comb[0][1])
