from src.problem import Problem

from enum import Enum


class Token:
    class Kind(Enum):
        number = "number",
        add = "+",
        mul = "*",
        lpar = "(",
        rpar = ")",
        eol = "eol",
        eof = "eof",
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
        while self.ch == ' ':
            self._next_ch()

        token = Token()

        if '0' <= self.ch <= '9':
            token.kind = Token.Kind.number
            token.val = int(self.ch)
            self._next_ch()
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
        elif self.ch == '\n':
            token.kind = Token.Kind.eol
            self._next_ch()

        return token

    def _next_ch(self):
        try:
            self.pos += 1
            self.ch = self.data[self.pos]
        except IndexError:
            self.ch = '\n'


class Parser:
    scanner: Scanner
    t: Token
    la: Token
    sym: Token.Kind
    results: list

    def __init__(self, data):
        self.scanner = Scanner(data)
        self.t = Token()
        self.la = Token()
        self.sym = Token.Kind.none
        self.results = []
        self._scan()

    def parse(self):
        raise NotImplementedError()

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
            raise RuntimeError("Unexpected token")


class LRParser(Parser):
    def parse(self):
        self.results.append(self._expr())
        self._check(Token.Kind.eol)

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
            raise RuntimeError("Elem must be called with number or lpar token")
        return elem

    def _op(self):
        if self.sym == Token.Kind.add:
            self._check(Token.Kind.add)
            return self.t.kind
        else:
            self._check(Token.Kind.mul)
            return self.t.kind


class PunstriParser(Parser):
    def parse(self):
        self.results.append(self._expr())
        self._check(Token.Kind.eol)

    def _expr(self):
        left_factor = self._factor()
        while self.sym == Token.Kind.mul:
            self._scan()
            right_factor = self._factor()
            left_factor *= right_factor
        return left_factor

    def _factor(self):
        left_term = self._term()
        while self.sym == Token.Kind.add:
            self._scan()
            right_term = self._term()
            left_term += right_term
        return left_term

    def _term(self):
        if self.sym == Token.Kind.number:
            self._scan()
            term = self.t.val
        elif self.sym == Token.Kind.lpar:
            self._scan()
            term = self._expr()
            self._check(Token.Kind.rpar)
        else:
            raise RuntimeError("Term must be called with number or lpar token")
        return term


def part_a(data: str):
    parser = LRParser(data)
    for _ in range(len(data.split('\n'))):
        parser.parse()
    return parser.sum_results()


def part_b(data: str):
    parser = PunstriParser(data)
    for _ in range(len(data.split('\n'))):
        parser.parse()
    return parser.sum_results()


def load():
    return problem.raw_data()


if __name__ == '__main__':
    problem = Problem(18)

    problem.submit(part_a(load()), 'a')  # 8929569623593
    problem.submit(part_b(load()), 'b')  # 231235959382961
