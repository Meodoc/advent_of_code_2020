import click
import os


@click.command()
@click.argument('day', nargs=1, type=int)
@click.option('-t', '--create-test-file', is_flag=True, help='Create a test file')
def generate_day_template(day: int, create_test_file: bool):
    src_path = f'src/{day:02}'
    data_path = f'data/{day:02}'
    file_path = f'{src_path}/day{day}.py'

    if not os.path.exists(src_path):
        os.mkdir(src_path)
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    # Create day.py
    override_day = True
    if os.path.exists(file_path):
        override_day = _prompt_override(file_path)
    if override_day:
        with open(file_path, 'w') as fh:
            fh.write("from src.problem import Problem\n\n\n"
                     "def part_a(data: list):\n    return None\n\n\n"
                     "def part_b(data: list):\n    return None\n\n\n"
                     "def load(p: Problem):\n    return p.data()\n\n\n"
                     "if __name__ == '__main__':\n"
                     f"    problem = Problem({day}, test=True)\n\n"
                     "    print(part_a(load(problem)))\n"
                     "    # print(part_b(load(problem)))\n\n"
                     "    # problem.submit(part_a(load(problem)), 'a')\n"
                     "    # problem.submit(part_b(load(problem)), 'b')\n")

    # Create test.in (optional)
    if create_test_file:
        if os.path.exists(test_path := f'{src_path}/test.in'):
            if not _prompt_override(test_path):
                return
        with open(test_path, 'w'):
            pass


def _prompt_override(file_name: str):
    while (x := input(f"{file_name} already exists. Do you want to override? (y/n): ", )) != 'y' and x != 'n':
        print("Invalid input, try again.")
    return x == 'y'


if __name__ == '__main__':
    generate_day_template()
