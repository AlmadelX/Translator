import os
from typing import Optional

import deepl

from src.logger import Logger


class Translator:
    __SOURCE_LANG = 'EN'

    def __init__(
            self,
            language: str,
            glossary: Optional[str],
            filename: str,
            logger: Logger
    ):
        self.__language = language
        self.__glossary = glossary
        self.__filename = filename
        self.__logger = logger
        self.__deepl_translator = deepl.Translator(os.getenv('DEEPL_AUTH_KEY'))

    def translate(self, text: str, line_number: int) -> str:
        if os.getenv('DEBUG') == 'true':
            self.__logger.info(f'Translating:\n{text}')
        result = str(self.__deepl_translator.translate_text(
            text,
            source_lang=self.__SOURCE_LANG,
            target_lang=self.__language,
            glossary=self.__glossary
        ))
        if text == result:
            message = f'Unsuccessful translation on \
"{self.__filename}" at line {line_number}:\n{text}'
            self.__logger.warn(message)
        return result
