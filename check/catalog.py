from bs4 import BeautifulSoup, Tag

from visitor import Visitor

class Catalog(Visitor):
    def __init__(self, catalog={}):
        super().__init__()
        self.catalog = catalog

    def _tag_enter(self, node):
        if node.name not in self.catalog:
            self.catalog[node.name] = set()
        for child in node:
            if isinstance(child, Tag):
                self.catalog[node.name].add(child.name)

with open("page.html", "r") as reader:
    page = reader.read()

doc = BeautifulSoup(page, "html.parser")
cataloger = Catalog()
cataloger.visit(doc.html)

for node, children in sorted(cataloger.catalog.items()):
    print(f"{node}: {', '.join(children)}")
