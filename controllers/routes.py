from flask import render_template, request

jogadores = []
productsIt = [{'Nome' : 'Ubuntu', 'Ano' : 2011, 'Categoria' : 'Servidor'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/sistemas_operacionais', methods=['GET', 'POST'])
    def games():
        game = productsIt[0]
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
        return render_template('games.html',
                                game=game,
                                jogadores=jogadores)
        
    @app.route('/products_cad', methods=['GET', 'POST'])
    def products_cad():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('ano') and request.form.get('categoria'):
                productsIt.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
        
        return render_template('cadgames.html',
                                productsIt=productsIt)