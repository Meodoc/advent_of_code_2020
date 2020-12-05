import click
import os


@click.command()
@click.option('-d', '--day', required=True, type=int, help='Day you want to create')
@click.option('-t', '--create-test-file', is_flag=True, help='Create a test file')
def create_day_stub(day: int, create_test_file: bool):
    if not os.path.exists(f'src/day{day}'):
        os.mkdir(f'src/day{day}')

    # Create day.py
    override_day = True
    if os.path.exists(file_name := f'src/day{day}/day{day}.py'):
        override_day = _prompt_override(file_name)
    if override_day:
        with open(f'src/day{day}/day{day}.py', 'w') as fh:
            fh.write("from src.problem import Problem\n\n\n")
            fh.write("def part_a():\n    return None\n\n\n")
            fh.write("def part_b():\n    return None\n\n\n")
            fh.write("def load():\n    return problem.data()\n\n\n")
            fh.write("if __name__ == '__main__':\n")
            fh.write(f"    problem = Problem({day})\n")
            fh.write("    data = load()\n\n")
            fh.write("    # problem.submit(part_a(), 'a')\n")
            fh.write("    # problem.submit(part_b(), 'b')\n")

    # Create test.in (optional)
    if create_test_file:
        if os.path.exists(file_name := f'src/day{day}/test.in'):
            if not _prompt_override(file_name):
                return
        with open(f'src/day{day}/test.in', 'w'):
            pass


def _prompt_override(file_name: str):
    while (x := input(f"{file_name} already exists. Do you want to override? (y/n): ",)) != 'y' and x != 'n':
        print("Invalid input, try again.")
    return x == 'y'


if __name__ == '__main__':
    create_day_stub()
