import os

import deepl


class Translator:
    def __init__(self):
        self.__deepl_translator = deepl.Translator(os.getenv('DEEPL_AUTH_KEY'))
        entries = {"artist": "Maler", "prize": "Gewinn"}
        sample_glossary = self.__deepl_translator.create_glossary(
            'Sample Glossary',
            source_lang='EN',
            target_lang='DE',
            entries=entries
        )
        print(sample_glossary.glossary_id)
