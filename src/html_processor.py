from typing import Optional

from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

from src.translator import Translator


class HTMLProcessor:
    __PARSER = 'html.parser'

    def __init__(self, filename: str, language: str, glossary: Optional[str]):
        with open(filename) as file:
            self.__soup = BeautifulSoup(file, self.__PARSER)
        self.__translator = Translator(language, glossary)

    def process(self):
        self.__walkthrough(self.__soup.html)

    def __walkthrough(self, current: Tag):
        for child in current.children:
            if not isinstance(child, Tag) or self.__skip(element=child):
                continue

            if text := self.__get_text_for_translation(element=child):
                result = self.__translator.translate(text)
                print(result)
            else:
                self.__walkthrough(child)

    @staticmethod
    def __skip(*, element: Tag) -> bool:
        if 'notranslate' in element.get_attribute_list('class'):
            return True

    @staticmethod
    def __get_text_for_translation(*, element: Tag) -> Optional[str]:
        match len(element.contents):
            case 0:
                if element.name == 'meta' and (
                        element.get('name') == 'description' or
                        element.get('property') in [
                            'og:title',
                            'og:description',
                            'twitter:title',
                            'twitter:description'
                        ]
                ):
                    return element.get('content')

                if alt := element.get('alt'):
                    return alt
            case 1:
                if isinstance(element.contents[0], NavigableString) and (
                        element.name in [
                            'title',
                            'h1',
                            'h2',
                            'h3',
                            'h4',
                            'h5',
                            'h6',
                            'div',
                            'a',
                            'span'
                        ]
                ):
                    return element.string
        return None
