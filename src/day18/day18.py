from src.problem import Problem

from dataclasses import dataclass
from enum import Enum


@dataclass
class Token:
    class Kind(Enum):
        number = "number",
        add = "+",
        mul = "*",
        lpar = "(",
        rpar = ")",
        eol = "eol",
        none = "none"
    kind: Kind = Kind.none
    val: int = 0


class Scanner:
    data: str
    pos: int = -1
    ch: str = ""

    def __init__(self, data: str):
        self.data = data
        self._next_ch()

    def next(self):
        while self.ch.isspace():
            self._next_ch()

        token = Token()

        if '0' <= self.ch <= '9':
            self._read_number(token)
        elif self.ch == '+':
            token.kind = Token.Kind.add
            self._next_ch()
        elif self.ch == '*':
            token.kind = Token.Kind.mul
            self._next_ch()
        elif self.ch == '(':
            token.kind = Token.Kind.lpar
            self._next_ch()
        elif self.ch == ')':
            token.kind = Token.Kind.rpar
            self._next_ch()
        elif self.ch == 'eol':
            token.kind = Token.Kind.eol

        return token

    def _next_ch(self):
        try:
            self.pos += 1
            self.ch = self.data[self.pos]
        except IndexError:
            self.ch = "eol"
            self.pos = 0

    def _read_number(self, token: Token):
        num = ""
        while '0' <= self.ch <= '9':
            num += self.ch
            self._next_ch()
        token.kind = Token.Kind.number
        token.val = int(num)


class Parser:
    data: list
    scanner: Scanner
    t: Token = Token()
    la: Token = Token()
    sym: Token.Kind = Token.Kind.none
    pos: int = 0
    results: list = []

    def __init__(self, data):
        self.data = data
        self.scanner = Scanner(data[self.pos])

    def parse(self):
        self._scan()
        self.results.append(self._expr())
        self._check(Token.Kind.eol)

        self.pos += 1
        try:
            self.scanner = Scanner(self.data[self.pos])
        except IndexError:
            print("Parsing finished!")

    def sum_results(self):
        return sum(self.results)

    def _scan(self):
        self.t = self.la
        self.la = self.scanner.next()
        self.sym = self.la.kind

    def _check(self, expected: Token.Kind):
        if self.sym == expected:
            self._scan()
        else:
            raise RuntimeError()

    def _expr(self):
        left_elem = self._elem()
        while self.sym == Token.Kind.add or self.sym == Token.Kind.mul:
            op = self._op()
            right_elem = self._elem()
            if op == Token.Kind.add:
                left_elem += right_elem
            else:
                left_elem *= right_elem
        return left_elem

    def _elem(self):
        if self.sym == Token.Kind.number:
            self._scan()
            elem = self.t.val
        elif self.sym == Token.Kind.lpar:
            self._scan()
            elem = self._expr()
            self._check(Token.Kind.rpar)
        else:
            raise RuntimeError()
        return elem

    def _op(self):
        if self.sym == Token.Kind.add:
            self._check(Token.Kind.add)
            return self.t.kind
        else:
            self._check(Token.Kind.mul)
            return self.t.kind


def part_a(data: list):
    parser = Parser(data)
    for _ in range(len(data)):
        parser.parse()
    return parser.sum_results()


def part_b():
    return None


def load():
    return problem.data()


if __name__ == '__main__':
    problem = Problem(18)

    problem.submit(part_a(load()), 'a')  # 8929569623593
    # problem.submit(part_b(), 'b')
