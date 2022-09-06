from typing import Optional

from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString, Comment

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
        self.__logger = logger
        with open(self.__filename) as file:
            self.__soup = BeautifulSoup(file, self.__PARSER)
        self.__translator = Translator(
            self.__language,
            glossary,
            self.__filename,
            self.__logger
        )

    def process(self):
        self.__logger.info(f'Started translating {self.__filename}')
        self.__walkthrough(self.__soup.html)
        if self.__soup.html.get('lang'):
            self.__soup.html['lang'] = self.__language
        with open(self.__filename, 'w') as file:
            file.write(self.__soup.prettify(formatter='html5'))
        self.__logger.info(f'Finished translating {self.__filename}')

    def __walkthrough(self, current: Tag):
        for child in current.children:
            if isinstance(child, Comment):
                continue
            if isinstance(child, NavigableString) and not str(child).isspace():
                translation = self.__translator.translate(
                    str(child),
                    current.sourceline
                )
                child.replace_with(translation)
            elif isinstance(child, Tag) and not \
                    self.__skip(element=child) and not \
                    self.__translate_as_tag(child):
                self.__walkthrough(child)

    @staticmethod
    def __skip(*, element: Tag) -> bool:
        if 'notranslate' in element.get_attribute_list('class') \
                or element.name == 'script' or element.name == 'style':
            return True
        return False

    def __translate_as_tag(self, element: Tag) -> bool:
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
        return False
