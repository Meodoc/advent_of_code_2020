from aocd import get_data, submit


class Problem:
    def __init__(self, day: int, store_input=True):
        self._day = day
        self._data = get_data(day=day)

        if store_input:
            print()
            with open(f'../../data/{day}/input.in', 'w') as fh:
                fh.writelines(self._data)

    def data(self, delim='\n', dtype=str) -> list:
        return [dtype(line) for line in self._data.split(delim)]

    def raw_data(self) -> str:
        return self._data

    def test_data(self, delim='\n', dtype=str) -> list:
        return [dtype(line) for line in self._raw_test_input().split(delim)]

    def raw_test_data(self) -> str:
        return self._raw_test_input()

    def submit(self, answer, part: str, store_answer=True) -> None:
        submit(answer, part=part, day=self._day)

        if store_answer:
            with open(f'../../data/{self._day}/{part}.out', 'w') as fh:
                fh.write(str(answer))

    # -- Helpers --
    @staticmethod
    def _raw_test_input() -> str:
        with open('test.in', 'r') as fh:
            return "".join(fh.readlines())

