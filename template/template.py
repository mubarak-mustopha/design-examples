import json
import sys
from bs4 import BeautifulSoup

from expander import Expander


def main():
    with open(sys.argv[1], "r") as reader:
        variables = json.load(reader)

    with open(sys.argv[2], "r") as reader:
        page = reader.read()

    doc = BeautifulSoup(page, "html.parser")

    expander = Expander(doc.find("html"), variables)
    expander.walk()

    print(expander.getResult())


if __name__ == "__main__":
    main()
