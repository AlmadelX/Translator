# Translator
Использование:
1. Откройте текущую папку в командной строке
2. Настройте среду и зависимости:
   
   Unix:
   ```commandline
   python3 -m venv .venv
   source .venv/bin/activate
   pip3 install -r requirements.txt
   ```
   Windows:
   ```commandline
   python3 -m venv .venv
   .venv/bin/activate.bat
   pip3 install -r requirements.txt
   ```

3. Настройте файл ```config.ini```:
   ```
   [CONFIG]
   DEEPL_AUTH_KEY = ключ_DEEPL_API
   DIRECTORY = абсолютный_путь_к_директории_с_переводимыми_файлами
   GLOSSARY = ID_глоссария
   LANGUAGE = код_конечного_языка
   LOG_FILE = абсолютный_путь_к_лог-файлу/logfile.log
   ```
4. Запустите скрипт:
   ```commandline
   python3 translator.py
   ```
