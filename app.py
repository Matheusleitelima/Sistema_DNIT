from flask import Flask, render_template, request, redirect
from models import db, Processo

app = Flask(__name__)

#Configurando o bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:1205@127.0.0.1:5432/processos_db'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "client_encoding": "utf8"
}
db.init_app(app)

#Criar tabelas no SQL

with app.app_context():
    db.create_all()

# rota principal
@app.route('/')
def home():
    processos = Processo.query.all() #pegar todos os dados do banco
    return render_template('index.html', processos = processos)

# rota de cadastro + crud no bd
@app.route('/cadastrar', methods=['GET', 'POST']) #rota, get abre a pag e post envia os dados
def cadastrar():
    if request.method == 'POST':
        processo = Processo(
            numero=request.form['numero'],
            tipo=request.form['tipo'],
            interessado=request.form['interessado'],
            responsavel=request.form['responsavel']
        )

        db.session.add(processo)
        db.session.commit()

        return redirect('/') #salva e volta a tela de inicio

    return render_template('cadastrar.html') #retornar a pag html


if __name__ == '__main__':
    app.run(debug=True)
