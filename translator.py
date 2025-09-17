# translator.py
# Placeholder for translation (M4)

def detect_language(text):
    """
    Dummy language detector.
    Later this will use Google Translate API or langdetect.
    """
    if any(word in text for word in ["है", "क्या", "कब"]):
        return "hi"  # Hindi
    return "en"  # Default English

def translate(text, target_lang):
    """
    Dummy translation function.
    For now, just returns the same text.
    Later will use Google Translate API.
    """
    return text
