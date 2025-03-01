from Api import app
from Api.db import Carros
from flask import make_response, jsonify, request, render_template,redirect, url_for

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(Carros)
    )

@app.route('/adicionar', methods=['POST', 'GET'])
def create_carro():
    if request.method == 'POST':
        id = request.form.get('id')
        marca = request.form.get('marca')
        nome = request.form.get('modelo')
        ano = request.form.get('ano')
        
        
        dados = {
            'id' : id,
            'marca' : marca,
            'nome' : nome,
            'ano' : ano

        }

        Carros.append(dados)
        redirect(url_for('get_carros'))

    return render_template('adiciona.html')