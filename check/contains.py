from bs4 import BeautifulSoup, Tag

def recurse(node, catalog):
    assert isinstance(node, Tag)

    if node.name not in catalog:
        catalog[node.name] = set()

    for child in node:
        if isinstance(child, Tag):
            catalog[node.name].add(child.name)
            recurse(child, catalog)

    return catalog

with open("page.html", "r") as reader:
    page = reader.read()

doc = BeautifulSoup(page, "html.parser")
catalog = recurse(doc.html, {})

for node, children in sorted(catalog.items()):
    print(f"{node}: {", ".join([child for child in children])}")