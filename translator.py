from googletrans import Translator

translator = Translator()

LANG_MAP = {
    "tamil": "ta",
    "hindi": "hi",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "english": "en"
}

def translate_text(text, target_lang):
    if target_lang not in LANG_MAP:
        return "Please select a language"

    result = translator.translate(text, dest=LANG_MAP[target_lang])
    return result.text
