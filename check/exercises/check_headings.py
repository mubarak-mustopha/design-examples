import sys
from enum import IntEnum
from bs4 import BeautifulSoup

from visitor import Visitor

class Headings(IntEnum):
    h1 = 1
    h2 = 2
    h3 = 3
    h4 = 4

class CheckHeadings(Visitor):
    def __init__(self):
        super().__init__()
        self.seen = []
        self.problems = []

    def _tag_enter(self, node):
        if node.name in Headings.__members__:
            if not self.seen and node.name != "h1":
                self.problems.append((None, node))
            elif self.seen:
                prev = self.seen[-1]
                current = node
                if node.name == "h1" or (Headings[prev.name] > Headings[current.name]) or (Headings[current.name] - Headings[prev.name]) > 1:
                    self.problems.append((prev, current))

            self.seen.append(node)

if __name__=="__main__":
    assert len(sys.argv) == 2, "Usage: python check_headings.py headings.html" 

    with open(sys.argv[1], "r") as reader:
        page = reader.read()
    doc = BeautifulSoup(page, "html.parser")

    headings_checker = CheckHeadings()
    headings_checker.visit(doc.html)
    for heading in headings_checker.seen:
        print(f"{heading.sourceline} -> {heading}")

    for prev, next in headings_checker.problems:
        print(f"{next} follows {prev}")