from src.problem import Problem

import copy

INSTRUCTIONS = {"nop": lambda pc, acc, param: (pc + 1, acc),
                "acc": lambda pc, acc, param: (pc + 1, acc + param),
                "jmp": lambda pc, acc, param: (pc + param, acc)}


def part_a():
    acc, _ = interpret(data)
    return acc


def part_b():
    swap_next.last = 0
    while True:
        patched_data = swap_next(copy.deepcopy(data))
        acc, finished = interpret(patched_data)
        if finished:
            return acc


def interpret(code):
    visited = set()
    pc = acc = 0
    while True:
        instruction = code[pc]
        for idx, cmd in instruction.items():
            if idx in visited:
                return acc, False
            pc, acc = INSTRUCTIONS[cmd[0]](pc, acc, cmd[1])
            visited.add(idx)
            if pc == len(code):
                return acc, True


def swap_next(data):
    next_instruction = next(i.items() for i in data[swap_next.last + 1:] for k, v in i.items() if v[0] in ["jmp", "nop"])
    for idx, cmd in next_instruction:
        if cmd[0] == "jmp":
            data[idx][idx] = ("nop", cmd[1])
        else:
            data[idx][idx] = ("jmp", cmd[1])
        swap_next.last = idx
    return data


def load():
    return [{idx: (line.split(" ")[0], int(line.split(" ")[1]))} for idx, line in enumerate(problem.data())]


if __name__ == '__main__':
    problem = Problem(8)
    data = load()

    print(part_a())
    print(part_b())

    problem.submit(part_a(), 'a')  # 1134
    problem.submit(part_b(), 'b')  # 1205
