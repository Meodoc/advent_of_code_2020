import click
import os


@click.command()
@click.option('--day', '-d', help='Day you want to create')
def create_day_stub(day):
    if not os.path.exists(f'day{day}'):
        os.mkdir(f'day{day}', )
    with open(f'day{day}/day{day}.py', 'w') as fh:
        fh.write("from src.problem import Problem\n\n")
        fh.write("def part_a():\n    return None\n\n")
        fh.write("def part_b():\n    return None\n\n")
        fh.write("if __name__ == '__main__':\n")
        fh.write(f"    problem = Problem({day})\n")
        fh.write("    data = problem.get_data('int')\n\n")
        fh.write("    # problem.submit(part_a(), 'a')\n")
        fh.write("    # problem.submit(part_b(), 'b')\n")


if __name__ == '__main__':
    create_day_stub()
