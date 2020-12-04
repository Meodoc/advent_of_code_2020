from src.problem import Problem


def part_a():
    valid_entries = 0
    for entry in data:
        min_occ = int(entry.split("-")[0])
        max_occ = int(entry.split("-")[1].split(" ")[0])
        letter = entry.split(" ")[1].split(":")[0]
        password = entry.split(" ")[2]
        occ = password.count(letter)
        if min_occ <= occ <= max_occ:
            valid_entries += 1

    return valid_entries


def part_b():
    valid_entries = 0
    for entry in data:
        pos1 = int(entry.split("-")[0]) - 1
        pos2 = int(entry.split("-")[1].split(" ")[0]) - 1
        letter = entry.split(" ")[1].split(":")[0]
        password = entry.split(" ")[2]
        if (password[pos1] == letter) ^ (password[pos2] == letter):
            valid_entries += 1

    return valid_entries


def load():
    data = problem.data()
    return data


if __name__ == '__main__':
    problem = Problem(2)
    data = load()

    problem.submit(part_a(), 'a')  # 600
    problem.submit(part_b(), 'b')  # 245
