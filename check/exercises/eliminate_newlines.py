import re
import sys
from bs4 import BeautifulSoup

NEWLINES_PATTERN = re.compile(r"\n+")

from visitor import Visitor

class EliminateNewlines(Visitor):
    def __init__(self):
        super().__init__()
        self.newlines = []

    def _text(self, node):
        if NEWLINES_PATTERN.fullmatch(node.string):
            self.newlines.append(node)

    def _tag_exit(self, node):
        if node.parent is None or node.name == 'html':
            for node in self.newlines:
                node.decompose()

if __name__=="__main__":
    assert len(sys.argv) == 3, print("Usage: python eliminate_newlines.py old.html new.html")
    with open(sys.argv[1], "r") as reader:
        page = reader.read()

    doc = BeautifulSoup(page, "html.parser")
    eliminator = EliminateNewlines()
    eliminator.visit(doc.html)

    with open(sys.argv[2], "w") as writer:
        writer.write(str(doc.html))
