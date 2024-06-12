from . import app, models
from flask import render_template, url_for

@app.route("/")
def accueil():
    liste_categories = models.categorie.query.all()
    return render_template('accueil.html',liste=type(liste_categories), liste_cat=liste_categories)

@app.route("/tous_produits")
def produits():
    equipements = models.equipement.query.all()
    return render_template('tous_produits.html', equip=equipements)

@app.route("/categorie/<int:id_cat>")
def produits_categorie(id_cat):
    category = models.categorie.query.get_or_404(id_cat)
    equipements = models.equipement.query.filter_by(id_categorie=id_cat).all()
    return render_template('produits_categorie.html', category=category, equipements=equipements)

