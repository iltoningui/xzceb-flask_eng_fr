from flask import request
from flask import Flask
from pkg.translation import en_to_fr, fr_to_en, get_translator

app = Flask('web translator')


@app.route("/englishToFrench")
def english_to_french():
    """
        Endpoint to translate english to french

    Returns:
        str: the text translated to french
    """
    text = request.args.get('text')

    translator = get_translator()

    en_fr_translated_text = en_to_fr(text, translator)

    return en_fr_translated_text

@app.route("/frenchToEnglish")
def french_to_english():
    """
        Endpoint to translate french to english

    Returns:
        str: the text translated to english
    """
    text = request.args.get('text')

    translator = get_translator()

    fr_en_translated_text = fr_to_en(text, translator)

    return fr_en_translated_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)