from flask import Flask, Blueprint, render_template, request
import requests
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

main = Blueprint('main', __name__, template_folder='templates', )

API_ENDPOINT = "https://api.thecatapi.com/v1/images/search"

@main.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        
        response = requests.get(API_ENDPOINT)

        if response.status_code == 200:
            data = response.json()
            catURL = data[0]['url']
            
            input = request.form.get('name')

            return render_template('index.html', catURL=catURL, input=input)
        
        elif response.status_code == 400:

            return render_template('index.html', msg='ERROR: CAT NOT FOUND.')
        
        else:
            return render_template('index.html', msg='API offline. Contact support.')

    elif request.method == 'GET':
        
        return render_template('index.html')