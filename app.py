from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        src = request.form.get('src')
        dest = request.form.get('dest')

        if text and src and dest:
            translated = translator.translate(text, src=src, dest=dest)
            return jsonify({'translated_text': translated.text})

        return jsonify({'error': 'Missing data'}), 400

    # For GET, render the page
    languages = LANGUAGES
    return render_template('index.html', languages=languages)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
