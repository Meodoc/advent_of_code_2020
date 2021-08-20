from aocd import get_data, submit
import subprocess


class Problem:
    def __init__(self, day: int, test=False, store_input=True):
        self._day = day
        self._data = get_data(day=day)
        self._test = test

        if store_input:
            with open(input_path := f'../../data/{day}/input.in', 'w') as fh:
                fh.writelines(self._data)
            subprocess.run(['git', 'add', input_path])

    def data(self, delim='\n', dtype=str) -> list:
        return [dtype(line) for line in
                (self._raw_test_input().split(delim) if self._test else self._data.split(delim))]

    def raw_data(self) -> str:
        return self._raw_test_input() if self._test else self._data

    def submit(self, answer, part: str, store_answer=True) -> None:
        submit(answer, part=part, day=self._day)

        if store_answer:
            with open(file_path := f'../../data/{self._day}/{part}.out', 'w') as fh:
                fh.write(str(answer))
            subprocess.run(['git', 'add', file_path])

    # -- Helpers --
    @staticmethod
    def _raw_test_input() -> str:
        with open('test.in', 'r') as fh:
            return "".join(fh.readlines())
