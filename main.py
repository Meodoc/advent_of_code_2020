import itertools

with open("day1/input", "r") as fh:
    lines = fh.readlines()

comb = itertools.combinations(lines, 3)
comb = [(int(a), int(b), int(c)) for a, b, c in comb if int(a) + int(b) + int(c) == 2020]
print(comb[0][0] * comb[0][1] * comb[0][2])
