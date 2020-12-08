class Bag:
    def __init__(self, name: str, parent=None, children=None, amount=None):
        if amount is None:
            amount = dict()
        if children is None:
            children = set()
        self.name = name
        self.parent = parent
        self.children = children
        self.amount = amount

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Bag):
            return self.name == other.name
        if isinstance(other, str):
            return self.name == other
        raise NotImplementedError("Equals should only be called with Bag or str")