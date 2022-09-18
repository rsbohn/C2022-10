
class Group:
    def __init__(self):
        self._content = []
    def __iter__(self):
        yield from self._content
    def __str__(self):
        return f"Group([{self._content.__str__}])"
    def append(self, item):
        self._content.append(item)
