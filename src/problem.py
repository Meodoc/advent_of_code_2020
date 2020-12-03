from aocd import get_data, submit


class Problem:
    def __init__(self, day: int, store_input=True):
        self._day = day
        self._data = get_data(day=day).split('\n')

        if store_input:
            with open('input.in', 'w') as fh:
                fh.writelines('\n'.join(self._data))

    def get_data(self, dtype=str):
        return [dtype(line) for line in self._data]

    def data(self, dtype=str):
        for line in self._data:
            yield dtype(line)

    def get_test_input(self, dtype=str):
        return [dtype(line) for line in self._open_test_input()]

    def test_input(self, dtype=str):
        for line in self._open_test_input():
            yield dtype(line)

    def submit(self, answer, part: str, store_answer=True):
        submit(answer, part=part, day=self._day)

        if store_answer:
            with open(f'answer_{part}.out', 'w') as fh:
                if isinstance(answer, list):
                    fh.writelines('\n'.join(str(answer)))
                else:
                    fh.write(str(answer))

    # -- Helpers --
    def _open_test_input(self):
        with open('test.in', 'r') as fh:
            return fh.readlines()

