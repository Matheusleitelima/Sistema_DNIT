from flask import Flask, render_template, request, redirect
from models import db, Processo

app = Flask(__name__)

#Configurando o bd

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/processos_db' #acesso ao banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#Criar tabelas no SQL

with app.app_context():
    db.create_all()

# rota principal
@app.route('/')
def home():
    return render_template('index.html')

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