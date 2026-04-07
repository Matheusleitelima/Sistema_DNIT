from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Processo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), unique=True, nullable=False)
    tipo = db.Column(db.String(20))
    interessado = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))

    