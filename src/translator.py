import os
from typing import Optional, List

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

    def translate(self, texts: List[str], line_numbers: List[int]) -> str:
        results = [str(txt) for txt in self.__deepl_translator.translate_text(
            texts,
            source_lang=self.__SOURCE_LANG,
            target_lang=self.__language,
            glossary=self.__glossary
        )]
        for text, result, line_number in zip(texts, results, line_numbers):
            if text == result:
                message = f'Unsuccessful translation on \
"{self.__filename}" at line {line_number}:\n{text}'
                self.__logger.warn(message)
        return results
