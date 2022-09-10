import csv
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

        file_base_name = self.__filename.rsplit('.', maxsplit=1)[0]
        self.__dictionary_name = f'{file_base_name}_{self.__SOURCE_LANG}_\
{self.__language}.csv'
        self.__old_dictionary = []
        if os.path.exists(self.__dictionary_name):
            with open(self.__dictionary_name, 'r') as dictionary:
                self.__old_dictionary = list(csv.reader(dictionary))
        self.__new_dictionary = [['text', 'translation', 'time']]

    def __del__(self):
        with open(self.__dictionary_name, 'w') as dictionary:
            csv.writer(dictionary, quotechar='"', quoting=csv.QUOTE_ALL)\
                .writerows(self.__new_dictionary)

    def translate(self, texts: List[str], line_numbers: List[int]) -> str:
        results = [None] * len(texts)
        translation = []
        for i in range(len(texts)):
            translation.append(texts[i])
        translation = [str(s) for s in self.__deepl_translator.translate_text(
            translation,
            source_lang=self.__SOURCE_LANG,
            target_lang=self.__language,
            glossary=self.__glossary
        )]
        for i in range(len(results)):
            if results[i] is None:
                results[i] = translation.pop(0)

        for text, result, line_number in zip(texts, results, line_numbers):
            if text == result:
                message = f'Unsuccessful translation on \
"{self.__filename}" at line {line_number}:\n{text}'
                self.__logger.warn(message)
        return results
