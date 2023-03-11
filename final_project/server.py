from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator
from ibm_watson.language_translator_v3 import LanguageTranslatorV3
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

apiKey = '9sbzM8EvV7mH1UonYke0dHKf88BR4CJ_gONeZUfvZYG1'
service_url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/336cb1d6-a1ab-460f-a580-e4f6010dee13'

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')

    auth = IAMAuthenticator(apiKey)
    en_fr_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=auth
    )
    en_fr_translator.set_service_url(service_url)

    en_fr_translated_text = __en_to_fr(textToTranslate, en_fr_translator)

    return en_fr_translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    
    auth = IAMAuthenticator(apiKey)
    fr_en_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=auth
    )
    fr_en_translator.set_service_url(service_url)

    fr_en_translated_text = __fr_to_en(textToTranslate, fr_en_translator)

    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    pass

def __en_to_fr(text: str, translator: LanguageTranslatorV3) -> str:
    en_fr_translation = translator.translate(
            text,
            'en-fr'
        )
    en_fr_translated_text = en_fr_translation.get_result()[0].get('translation')
    return en_fr_translated_text


def __fr_to_en(text: str, translator: LanguageTranslatorV3) -> str:
    fr_en_translation = translator.translate(
            text,
            'fr-en'
        )
    fr_en_translated_text = fr_en_translation.get_result()[0].get('translation')
    return fr_en_translated_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
