from aocd import get_data, submit


class Problem:
    def __init__(self, day: int, store_input=True):
        self._day = day
        self._data = get_data(day=day).split('\n')

        if store_input:
            with open('input.in', 'w') as fh:
                fh.writelines('\n'.join(self._data))

    def get_data(self, dtype='str'):
        if dtype == 'str':
            return self._data
        elif dtype == 'int':
            return [int(line) for line in self._data]
        elif dtype == 'float':
            return [float(line) for line in self._data]

    def data(self, dtype='str'):
        for line in self._data:
            if dtype == 'str':
                yield line
            elif dtype == 'int':
                yield int(line)
            elif dtype == 'float':
                yield float(line)

    def submit(self, answer, part: str, store_answer=True):
        submit(answer, part=part, day=self._day)

        if store_answer:
            with open(f'answer_{part}.out', 'w') as fh:
                if isinstance(answer, list):
                    fh.writelines('\n'.join(str(answer)))
                else:
                    fh.write(str(answer))
