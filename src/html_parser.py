from typing import Tuple, Optional

from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString


class HTMLParser:
    __PARSER = 'html.parser'

    def __init__(self, filename: str):
        with open(filename) as file:
            soup = BeautifulSoup(file, self.__PARSER)
        self.__matching_strings = []
        self.__parse(soup.html)

    def parse(self, current_element: Tag):
        for child in current_element.children:
            if not isinstance(child, Tag):
                continue
            matching_result = self.match(child)
            if matching_result[1]:
                self.matching_strings.append(matching_result[1])
            elif not matching_result[0]:
                self.parse(child)

    def match(self, element: Tag) -> Tuple[bool, Optional[str]]:
        """
        Match element with rules.
        :return: [skip, to_translate]
        """
        if 'notranslate' in element.get_attribute_list('class'):
            return True, None
        if element.name == 'title':
            return False, element.string
        if element.name == 'meta':
            if element.get('name') == 'description' \
                    or element.get('property') in ['og:title',
                                                   'og:description',
                                                   'twitter:title',
                                                   'twitter:description']:
                return False, element.get('content')
        if element.get('alt'):
            return False, element.get('alt')
        if len(element.contents) == 1 \
                and isinstance(element.contents[0], NavigableString):
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'a',
                                'span']:
                return False, element.string
        return False, None

    def get_text(self) -> Optional[str]:
        self.id += 1
        if self.id < len(self.matching_strings):
            return self.matching_strings[self.id]

    def set_text(self, text: str):
        self.matching_strings[self.id] = text

