import os
from typing import Optional

import deepl


class Translator:
    __SOURCE_LANG = 'EN'

    def __init__(self, language: str, glossary: Optional[str]):
        self.__language = language
        self.__glossary = glossary
        self.__deepl_translator = deepl.Translator(os.getenv('DEEPL_AUTH_KEY'))

    def translate(self, text: str) -> str:
        result = str(self.__deepl_translator.translate_text(
            text,
            source_lang=self.__SOURCE_LANG,
            target_lang=self.__language,
            glossary=self.__glossary
        ))
        return result
