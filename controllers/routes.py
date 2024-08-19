from flask import render_template, request
productsIt = [{'Nome' : 'Ubuntu', 'Ano' : 2011, 'Categoria' : 'Servidor'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/produtos', methods=['GET', 'POST'])
    def produtos():

        
       
        return render_template('produtos.html',
                                products=productsIt)
        
    @app.route('/products_cad', methods=['GET', 'POST'])
    def products_cad():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('ano') and request.form.get('categoria'):
                productsIt.append({'Nome' : request.form.get('nome'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
        
        return render_template('cadastro_produtos.html',
                                productsIt=productsIt)