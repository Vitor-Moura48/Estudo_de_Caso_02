from flask import Flask, request, jsonify, render_template, make_response
from app import app

from controller.autenticacao_controller import AutenticacaoController


# pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" --add-data "database;database" app.py

@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            data = request.get_json()
            return AutenticacaoController.autenticar_usuario(data)

        return render_template('auth/login.html')
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Rota para a página de cadastro
@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        # Verificar se o método é POST, ou seja, se o formulário foi submetido
        if request.method == 'POST':
            data = request.get_json()
            return AutenticacaoController.cadastrar_usuario(data)
        
        return render_template('auth/register.html')
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/gestao_leitos')
def gestao_leitos():
    return render_template('modulo1/index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

# Rota para a página de splash screen
@app.route('/splash')
def splash():
    return render_template('splash.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404