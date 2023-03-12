from .translation import get_translator, en_to_fr, fr_to_en

def test_en_to_fr_translation():
    text_to_translate = "Hi there"
    translator = get_translator()

    translated_text = en_to_fr(text_to_translate, translator)
    assert translated_text == 'Salut là'


def test_fr_to_en_translation():
    text_to_translate = "Salut là"
    translator = get_translator()

    translated_text = fr_to_en(text_to_translate, translator)
    assert translated_text == "Hi there"


def test_fr_to_en_translation_fails():
    text_to_translate = "Salut là"
    translator = get_translator()

    translated_text = fr_to_en(text_to_translate, translator)
    assert translated_text != "Hi"

def test_en_to_fr_translation_fails():
    text_to_translate = "Hi there"
    translator = get_translator()

    translated_text = en_to_fr(text_to_translate, translator)
    assert translated_text != 'Salut'
