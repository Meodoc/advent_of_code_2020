from aocd import get_data, submit


class Problem:
    def __init__(self, day: int, store_input=True):
        self._day = day
        self._data = get_data(day=day)

        if store_input:
            with open('input.in', 'w') as fh:
                fh.writelines('\n'.join(self._data))

    def raw_data(self):
        return self._data

    # def data(self, delim='\n', dtype=str):
    #     for line in self._data.split(delim):
    #         yield dtype(line)

    def data(self, delim='\n', dtype=str):
        return [dtype(line) for line in self._data.split(delim)]

    # def test_data(self, delim='\n', dtype=str):
    #     for line in self._raw_test_input().split(delim):
    #         yield dtype(line)

    def test_data(self, delim='\n', dtype=str):
        return [dtype(line) for line in self._raw_test_input().split(delim)]

    def submit(self, answer, part: str, store_answer=True):
        submit(answer, part=part, day=self._day)

        if store_answer:
            with open(f'answer_{part}.out', 'w') as fh:
                if isinstance(answer, list):
                    fh.writelines('\n'.join(str(answer)))
                else:
                    fh.write(str(answer))

    # -- Helpers --
    def _raw_test_input(self):
        with open('test.in', 'r') as fh:
            return "".join(fh.readlines())

