from src.problem import Problem

import itertools as it


def part_a():
    diffs = list(map(lambda x1, x2: x2 - x1, data, data[1:]))
    return diffs.count(1) * diffs.count(3)


def part_b():
    # arrangements = 1
    # visited = list()
    # for i1, x1 in enumerate(data):
    #     local_arrangements = 1
    #     for i2, x2 in enumerate(data[1+i1:], i1+1):
    #         if x2 - x1 <= 3:
    #             if data[:i1+1] + data[i2:] not in visited:
    #                 print(data[:i1+1] + data[i2:])
    #                 visited.append(data[:i1+1] + data[i2:])
    #                 local_arrangements += 1
    #         else:
    #             break
    #     if local_arrangements > 0:
    #         arrangements *= local_arrangements

    for i1, x1 in enumerate(data):
        for i2, x2 in enumerate(data[1+i1:], i1+1):
            if x2 - x1 <= 3:
                print(data[:i1+1] + data[i2:])
            else:
                break

    # print(len(data))
    arrangements = list()
    #visited = list()
    #count_shit(data, arrangements, 0)

    #arrangements = get_arrangements(data)
    # print("-- Result --")
    # for r in arrangements:
    #     print(r)
    return arrangements




def get_arrangements(data):
    total_arrangements = 0
    for i in reversed(range(len(data))):
        arrangements = try_change(i, len(data))
        print(f"i: {i}, arrs: {arrangements}")
        total_arrangements += arrangements
    return total_arrangements


def try_change(start, end):
    local = data[start:end]
    arrangements = 0
    for i1, x1 in enumerate(local):
        for i2, x2 in enumerate(local[i1:], i1):
            print(local[:i1] + local[i2:])
            arrangements += 1

    return arrangements






def count_shit(data, arrangements, i):
    #print(i)
    if i == len(data) - 1:
        return
    for i1, x1 in enumerate(data[i:], i):
        for i2, x2 in enumerate(data[1 + i1:], i1+1):
            if x2 - x1 <= 3 and data[:i1+1] + data[i2:] not in arrangements:
                print(data[:i1 + 1] + data[i2:])
                count_shit(data, arrangements, i + 1)
                arrangements.append(data[:i1 + 1] + data[i2:])


# test solution: 19208

# 36132988816414656965872925540352 too high
# 2251799813685248 too high

def load():
    return sorted((data := problem.test_data(dtype=int)) + [0, max(data) + 3])  # Append charging outlet and adapter


if __name__ == '__main__':
    problem = Problem(10)
    data = load()

    #print(part_a())
    print(part_b())
    # problem.submit(part_a(), 'a')  # 2775
    # problem.submit(part_b(), 'b')
