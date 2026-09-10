from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    if not data or 'text' not in data or 'source_lang' not in data or 'target_lang' not in data:
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    text = data['text']
    source_lang = data['source_lang']
    target_lang = data['target_lang']

    if not text.strip():
        return jsonify({'error': 'El texto a traducir no puede estar vacío'}), 400

    try:
        # deep-translator usa códigos de idioma estándar (ej: 'es', 'en', 'fr')
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translated_text = translator.translate(text)
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
