from bs4 import BeautifulSoup, NavigableString

class Visitor:
    def visit(self, node):
        if isinstance(node, NavigableString):
            self._text(node)
        else:
            self._tag_enter(node)
            for child in node:
                self.visit(child)
            self._tag_exit(node)

    def _text(self, node): pass

    def _tag_enter(self, node): pass

    def _tag_exit(self, node): pass
