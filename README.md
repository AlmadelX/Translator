# Translator
Использование:
1. Настройте файл ```.env```:
   ```
   DEEPL_AUTH_KEY=DeepL_API_auth_key
   ```
2. Настройте файл ```config.ini```:
   ```
   [CONFIG]
   HTML_FILE = path_to/file.html
   LOG_FILE = path_to/logfile.log
   LANGUAGE = target_language_code
   GLOSSARY = glossary_id
   ```
3. Настройте среду и зависимости:
   ```commandline
   python3 -m venv .venv
   pip3 install -r requirements.txt
   ```
4. Запустите скрипт:
   ```commandline
   python3 translator.py
   ```
