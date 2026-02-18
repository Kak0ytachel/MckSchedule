from os import listdir, path, mkdir, rename
import json

TRANSLATIONS_FOLDER = "translations/"
TRANSLATION_KEYS_FILE = "lines.json"
DEFAULT_LANGUAGE = "en"
DEFAULT_TRANSLATION_FILE = "en-US.json"

class LanguageManager:
    languages = []
    translations = {}
    keys = []

    def __init__(self):
        self.create_files()

        files = listdir(TRANSLATIONS_FOLDER)
        self.keys = json.load(open(TRANSLATIONS_FOLDER + TRANSLATION_KEYS_FILE))

        for filename in files:
            if filename == TRANSLATION_KEYS_FILE:
                continue
            lang = filename.split(".")[0]
            if lang.find("-") != -1:
                lang = lang.split("-")[0]
            lang.lower()
            self.languages.append(lang)

            try:
                with open(TRANSLATIONS_FOLDER + filename, "r", encoding="utf-8") as f:
                    translation: dict = json.load(f)
            except json.decoder.JSONDecodeError:
                rename(TRANSLATIONS_FOLDER + filename, TRANSLATIONS_FOLDER + filename + ".bak")
                print(f"Error loading {filename}, overwriting it...")
                translation = {}
            counter = 0
            for key in self.keys:
                if key not in translation.keys():
                    translation[key] = "No translation yet #TODO"
                    counter += 1
            if counter != 0:
                print(f"Added {counter} missing translations to {lang}")
                with open(TRANSLATIONS_FOLDER + filename, "w", encoding="utf-8") as f:
                    json.dump(translation, f, indent=4, ensure_ascii=False)
            self.translations[lang] = translation

    def check_lang(self, lang: str) -> bool:
        return lang in self.languages

    # def get(self, lang: str, key: str) -> str:
    #     if lang.find("-") != -1:
    #         lang = lang.split("-")[0]
    #     lang.lower()
    #     if lang not in self.languages:
    #         raise ValueError("No such translation language: " + lang)
    #     if key not in self.keys:
    #         raise ValueError("No such translation key: " + key)
    #     return self.translations[lang][key]

    def get(self, lang: str, key: str) -> str:
        if lang.find("-") != -1:
            lang = lang.split("-")[0]
        lang.lower()
        if lang not in self.languages:
            result = "No such translation language: " + lang
            print(result)
            return result
        if key not in self.keys:
            result = "Error: No such translation key: " + key
            print(result)
            return result
        return self.translations[lang][key]

    def check_get_lang(self, lang: str) -> str:
        if lang not in self.languages:
            return DEFAULT_LANGUAGE
        else:
            return lang

    def create_files(self):
        if not path.isdir(TRANSLATIONS_FOLDER):
            mkdir(TRANSLATIONS_FOLDER)
        if not path.isfile(TRANSLATIONS_FOLDER + TRANSLATION_KEYS_FILE):
            with open(TRANSLATIONS_FOLDER + TRANSLATION_KEYS_FILE, "w", encoding="utf-8") as f:
                json.dump(["sample-key"], f, indent=4, ensure_ascii=False)
        if not path.isfile(TRANSLATIONS_FOLDER + "en-US.json"):
            with open(TRANSLATIONS_FOLDER + DEFAULT_TRANSLATION_FILE, "w", encoding="utf-8") as f:
                json.dump({"sample-key": "Hello world!"}, f, indent=4, ensure_ascii=False)