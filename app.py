from flask import Flask, render_template, request, redirect
from models import db, Processo
import os

app = Flask(__name__)

# ================= CONFIG BANCO =================

database_url = os.getenv('DATABASE_URL')

if not database_url:
    raise ValueError("DATABASE_URL não está definida no ambiente!")

#  Corrige QUALQUER formato do Render
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql+psycopg://", 1)

elif database_url.startswith("postgresql://"):
    database_url = database_url.replace("postgresql://", "postgresql+psycopg://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Criar tabelas sem quebrar deploy
try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print("Erro ao criar tabelas:", e)

# ================= ROTAS =================

@app.route('/')
def home():
    processos = Processo.query.all()
    return render_template('index.html', processos=processos)

@app.route('/cadastrar', methods=['GET', 'POST'])
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

        return redirect('/')

    return render_template('cadastrar.html')

@app.route('/excluir/<int:id>')
def excluir(id):
    processo = Processo.query.get(id)

    if processo:
        db.session.delete(processo)
        db.session.commit()

    return redirect('/')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    processo = Processo.query.get(id)

    if not processo:
        return redirect('/')

    if request.method == 'POST':
        processo.numero = request.form['numero']
        processo.tipo = request.form['tipo']
        processo.interessado = request.form['interessado']
        processo.responsavel = request.form['responsavel']

        db.session.commit()
        return redirect('/')

    return render_template('editar.html', processo=processo)

# ================= RUN =================

if __name__ == '__main__':
    app.run(debug=True)
