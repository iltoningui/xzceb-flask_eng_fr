"""
    Translation module
"""
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator
from ibm_watson.language_translator_v3 import LanguageTranslatorV3

APY_KEY = '9sbzM8EvV7mH1UonYke0dHKf88BR4CJ_gONeZUfvZYG1'
SERVICE_URL = ('https://api.eu-gb.language-translator.'
               'watson.cloud.ibm.com/instances/'
               '336cb1d6-a1ab-460f-a580-e4f6010dee13')

def get_translator():
    """
    get_translator Creates an instance of a translator

    Returns:
        LanguageTranslatorV3: returns a language translator
    """
    auth = IAMAuthenticator(APY_KEY)
    translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=auth
    )
    translator.set_service_url(SERVICE_URL)
    return translator

def en_to_fr(text: str, translator: LanguageTranslatorV3) -> str:
    """
    en_to_fr translate english to french

    Args:
        text (str): The text to translate
        translator (LanguageTranslatorV3): Translator instance

    Returns:
        str: translated text
    """
    en_fr_translation = translator.translate(
        text,
        model_id='en-fr'
    )
    en_fr_translated_text = en_fr_translation\
        .get_result()['translations'][0]['translation']
    return en_fr_translated_text


def fr_to_en(text: str, translator: LanguageTranslatorV3) -> str:
    """
    fr_to_en translate en to fr

    Args:
        text (str): Text to translate
        translator (LanguageTranslatorV3): translator instance

    Returns:
        str: translated text
    """
    fr_en_translation = translator.translate(
        text,
        model_id = 'fr-en',
    )
    fr_en_translated_text = fr_en_translation\
        .get_result()['translations'][0]['translation']
    return fr_en_translated_text
