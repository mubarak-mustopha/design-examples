from bs4 import BeautifulSoup
import sys

from visitor import Visitor

class CheckAccessibility(Visitor):
    def __init__(self):
        super().__init__()
        self.no_alt_imgs = []
        self.faulty_figures = []
        self.redundant_text_imgs = []

    def _tag_enter(self, node):
        if node.name == "img":
            self._check_img(node)
        elif node.name == "figure":
            self._check_figure(node)

    def _check_img(self, node):
        assert node.name == "img"

        if "alt" not in node.attrs:
            self.no_alt_imgs.append(node)

        elif node.parent.name == "figure" and node.parent.find("figcaption"):
            if node.parent.figcaption.string == node.attrs["alt"]:
                self.redundant_text_imgs.append(node)

    def _check_figure(self, node):
        assert node.name == "figure"

        if len(node.find_all("figcaption")) != 1:
            self.faulty_figures.append(node)

def display(header, body):
    border = "-" * len(header)
    body = body or "None"
    print("\n".join([border, header, border, body]))

if __name__=="__main__":
    assert len(sys.argv) == 2, "Usage: python check_accessibility.py accessibility.html"

    with open(sys.argv[1], "r") as reader:
        page = reader.read()

    doc = BeautifulSoup(page, "html.parser")
    accessibility_checker = CheckAccessibility()
    accessibility_checker.visit(doc.html)

    no_alt_imgs = [f"{img.sourceline} -> {img}" for img in accessibility_checker.no_alt_imgs]
    display("<img> tags without alt attribute", "\n".join(no_alt_imgs))

    redundant_text_imgs = [f"{img.sourceline} -> {img.parent}" for img in accessibility_checker.redundant_text_imgs] 
    display("Images with redundant text", "\n".join(redundant_text_imgs))

    faulty_figures = [f"{figure.sourceline} -> {figure}" for figure in accessibility_checker.faulty_figures]
    display("Faulty <figure>", "\n".join(faulty_figures))