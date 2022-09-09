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
   DIRECTORY = абсолютный_путь_к_директории_с_переводимыми_файлами
   LOG_FILE = абсолютный_путь_к_лог-файлу/logfile.log
   LANGUAGE = код_конечного_языка
   GLOSSARY = ID_глоссария
   ```
4. Запустите скрипт:
   ```commandline
   python3 translator.py
   ```
