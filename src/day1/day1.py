import itertools

from src.problem import Problem

problem = Problem(1)
data = problem.get_data('int')

# Part a
comb = itertools.combinations(data, 2)
comb = [(a, b) for a, b in comb if a + b == 2020]
answer = comb[0][0] * comb[0][1]

problem.submit(answer, 'a')

# Part b
comb = itertools.combinations(data, 3)
comb = [(a, b, c) for a, b, c in comb if a + b + c == 2020]
answer = comb[0][0] * comb[0][1] * comb[0][2]

problem.submit(answer, 'b')
