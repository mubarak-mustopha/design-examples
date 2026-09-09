import yaml
from bs4 import BeautifulSoup, Tag

from visitor import Visitor

class Check(Visitor):
    def __init__(self, manifest):
        super().__init__()
        self.manifest = manifest
        self.problems = {}

    def _tag_enter(self, node):
        if isinstance(node, Tag):
            children = {child.name for child in node if isinstance(child,Tag)}
            errors = children - self.manifest.get(node.name, set())
            if errors:
                errors |= self.problems.get(node.name, set())
                self.problems[node.name] = errors

with open("page.html", "r") as reader:
    text = reader.read()
doc = BeautifulSoup(text, "html.parser")

with open("manifest.yaml", "r") as reader:
    result = yaml.load(reader, yaml.FullLoader)
    result = {k: set(v) for k, v in result.items()}

checker = Check(manifest=result)
checker.visit(doc.html)

for node, children in sorted(checker.problems.items()):
    print(f"{node}: {', '.join(children)}")