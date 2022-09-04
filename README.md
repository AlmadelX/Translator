# Translator
Usage:
1. Setup ```.env``` file:
   ```
   DEEPL_AUTH_KEY=DeepL_API_auth_key
   ```
2. Run the script:
   ```commandline
   python translator.py -f path_to/file.html \
   --logfile path_to/logfile.log \
   --language target_language_code [--glossary glossary_id]
   ```
