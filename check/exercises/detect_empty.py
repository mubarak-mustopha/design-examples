from bs4 import BeautifulSoup, Tag

from visitor import Visitor

class DetectEmptyTag(Visitor):
    def __init__(self):
        super().__init__()
        self.empty_tags = []

    def _tag_enter(self, node):
        if len(node.contents) == 0:
            self.empty_tags.append(node)


if __name__=="__main__":
    text = """<html lang="en">
                        <head></head>
                        <body class="outline narrow">
                            <p align="left" align="right">paragraph</p>
                            <a></a>
                            <div style="height: 90px;width: 180px"></div>
                        </body>
                 </html>"""
    
    doc = BeautifulSoup(text, "html.parser")
    detector = DetectEmptyTag()
    detector.visit(doc.html)
    if detector.empty_tags:
        for tag in detector.empty_tags:
            print(f"{tag.sourceline} -> {str(tag)}")