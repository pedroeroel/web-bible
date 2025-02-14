from flask import Flask, Blueprint, render_template, request
import requests
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

main = Blueprint('main', __name__, template_folder='templates', )

API_ENDPOINT = "https://brasilapi.com.br/api/cep/v2/{cep}"

SOUTH = ('PR', 'SC', 'RS')
SOUTHEAST = ('SP', 'RJ', 'MG', 'ES')
MIDWEST = ('MT', 'MS', 'GO', 'DF')
NORTHEAST = ('BA', 'SE', 'AL', 'PE', 'PB', 'RN', 'CE', 'PI', 'MA')
NORTH = ('AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC')

@main.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        
        cep = request.form.get('cep', '').strip()
        weight = int(request.form.get('weight', 0))
        wprice = weight / 100

        response = requests.get(API_ENDPOINT.format(cep=cep))

        if response.status_code == 200:
            data = response.json()
            state = data.get('state')

            if state in SOUTH:
                freight = wprice * 6
            elif state in SOUTHEAST:
                freight = wprice * 5
            elif state in MIDWEST:
                freight = wprice * 7
            elif state in NORTHEAST:
                freight = wprice * 8
            elif state in NORTH:
                freight = wprice * 10
            
            if freight:
                freight = locale.currency(freight, grouping=True)

                return render_template('index.html', freight=freight)
        
        elif response.status_code == 400:

            return render_template('index.html', msg='ERROR: Postal Code not found.')
        
        else:
            return render_template('index.html', msg='API offline. Contact support.')

    elif request.method == 'GET':
        
        return render_template('index.html')