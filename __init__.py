from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8f0435dd8a6e48467800767e1f118e8'
# Supprime les notifications inutiles
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Emplacement de la base de données
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://anonyme:admin@localhost:5432/projetTi'

# Instanciation d'un objet SQLAlchemy
db = SQLAlchemy(app)
#Après avoir instancié db :
from . import routes
