from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator, MyMemoryTranslator

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
        # Intentar primero con GoogleTranslator
        try:
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            translated_text = translator.translate(text)
        except Exception as e:
            # Si Google falla (por límite de peticiones u otro error), usar MyMemoryTranslator como respaldo
            print(f"GoogleTranslator falló ({e}), usando MyMemoryTranslator...")
            # MyMemory no soporta 'auto', por lo que si está en 'auto' forzamos a intentar inferirlo o usar español por defecto
            if source_lang == 'auto':
                source_lang = 'es'
            
            translator_fallback = MyMemoryTranslator(source=source_lang, target=target_lang)
            translated_text = translator_fallback.translate(text)

        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
