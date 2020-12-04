from src.problem import Problem

import re


def part_a():
    valid_passports = 0
    for document in problem.data():
        fields = re.split(' |\n', document)
        keys = [field.split(':')[0] for field in fields]
        if len(fields) == 8 or len(fields) == 7 and 'cid' not in keys:
            valid_passports += 1

    return valid_passports


def part_b():
    valid_passports = 0
    for document in problem.data():
        fields = re.split(' |\n', document)
        fields = [(field.split(':')[0], field.split(':')[1]) for field in fields]
        keys = [field[0] for field in fields]
        if len(fields) == 8 or len(fields) == 7 and 'cid' not in keys:
            if check_passport(fields):
                valid_passports += 1
    return valid_passports


def check_passport(fields):
    for key, value in fields:
        if key == 'byr':
            if not (1920 <= int(value) <= 2002):
                return False
        elif key == 'iyr':
            if not (2010 <= int(value) <= 2020):
                return False
        elif key == 'eyr':
            if not (2020 <= int(value) <= 2030):
                return False
        elif key == 'hgt':
            if value.endswith('cm'):
                height = int(value[:-2])
                if not (150 <= height <= 193):
                    return False
            elif value.endswith('in'):
                height = int(value[:-2])
                if not (59 <= height <= 76):
                    return False
            else:
                return False
        elif key == 'hcl':
            if value[0] == '#':
                rgb = value[1:]
                for c in rgb:
                    if not (c.isdigit() or c == 'a' or c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f'):
                        return False
            else:
                return False
        elif key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif key == 'pid':
            if len(value) != 9:
                return False
        elif key == 'cid':
            pass  # ignore cid
    return True


if __name__ == '__main__':
    problem = Problem(4)

    print(part_b())
    problem.submit(part_a(), 'a')
    problem.submit(part_b(), 'b')
