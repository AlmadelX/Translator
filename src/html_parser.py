import bs4
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString


def match(element: Tag) -> bs4.element:
    return element


class HTMLParser:
    PARSER = 'html.parser'

    def __init__(self, filename: str):
        self.filename = filename
        with open(self.filename) as file:
            self.soup = BeautifulSoup(file, self.PARSER)
        self.matching_strings = []
        self.parse(self.soup.html)
        print(self.matching_strings)

    def parse(self, current_element: bs4.element):
        for child in current_element.children:
            if not isinstance(child, Tag):
                continue
            matching_element = match(child)
            if isinstance(matching_element, NavigableString):
                self.matching_strings.append(matching_element)
            elif isinstance(matching_element, Tag):
                self.parse(matching_element)
