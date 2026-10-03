from bs4 import Tag, NavigableString


class Visitor:
    def __init__(self, root: Tag):
        self.root = root

    def walk(self, node: Tag | NavigableString | None = None):
        if node is None:
            node = self.root
        if self.open(node):
            for child in node.children:
                self.walk(child)
        self.close(node)

    def open(self, node):
        raise NotImplementedError("open")

    def close(self, node):
        raise NotImplementedError("close")
