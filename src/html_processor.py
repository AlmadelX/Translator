from typing import Optional

from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

from src.logger import Logger
from src.translator import Translator


class HTMLProcessor:
    __PARSER = 'html.parser'

    def __init__(
            self,
            filename: str,
            language: str,
            glossary: Optional[str],
            logger: Logger
    ):
        self.__filename = filename
        self.__language = language
        with open(self.__filename) as file:
            self.__soup = BeautifulSoup(file, self.__PARSER)
        self.__translator = Translator(
            self.__language,
            glossary,
            self.__filename,
            logger
        )

    def process(self):
        self.__walkthrough(self.__soup)
        if self.__soup.html.get('lang'):
            self.__soup.html['lang'] = self.__language
        with open(self.__filename, 'w') as file:
            file.write(self.__soup.prettify(formatter='html5'))

    def __walkthrough(self, current: Tag):
        for child in current.children:
            if not isinstance(child, Tag) or self.__skip(element=child):
                continue

            if not self.__translate(element=child):
                self.__walkthrough(child)

    @staticmethod
    def __skip(*, element: Tag) -> bool:
        if 'notranslate' in element.get_attribute_list('class'):
            return True

    def __translate(self, *, element: Tag) -> bool:
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
                    element['content'] = self.__translator.translate(
                        element['content'],
                        element.sourceline
                    )
                    return True

                if element.get('alt'):
                    element['alt'] = self.__translator.translate(
                        element['alt'],
                        element.sourceline
                    )
                    return True
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
                    element.string = self.__translator.translate(
                        str(element.string),
                        element.sourceline
                    )
                    return True
        return False
