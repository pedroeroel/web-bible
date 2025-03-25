from flask import Flask, Blueprint, render_template, request
import requests

main = Blueprint('main', __name__, template_folder='templates')

API_ENDPOINT = "https://bible-api.com/"

@main.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        book = request.form.get('book')
        chapter = request.form.get('chapter')
        verse = request.form.get('verse')
        translation = request.form.get('translation', 'kjv')

        if book and chapter and verse:
            url = f"{API_ENDPOINT}{book}+{chapter}:{verse}?translation={translation}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                verse_text = data['text']
                reference_verse = data['reference']

                return render_template('index.html', verse_text=verse_text, reference_verse=reference_verse)
            else:
                return render_template('index.html', msg='Verse not found or API error.')
        else:
            return render_template('index.html', msg='Please fill in all fields.')

    elif request.method == 'GET':
        return render_template('index.html')