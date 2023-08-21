from flask import Flask, render_template, request, redirect, url_for
from database import Database

app = Flask(__name__)

db = Database()

@app.route('/')
def Accueil():

    recent_donations = db.get_recent_donations(5)
    

    total_recolte = db.get_total_recolte()

    
    return render_template('Accueil.html', recent_donations=recent_donations, total_recolte=total_recolte)

@app.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        adresse = request.form['adresse']
        email = request.form['email']
        somme_promise = request.form['somme_promise']
        conditions = True if 'conditions' in request.form else False

       
        db.insert_donation(nom, prenom, adresse, email, somme_promise, conditions)

        return redirect(url_for('merci_pharisien'))

    return render_template('donation.html')


@app.route('/merci_pharisien')
def merci_pharisien():
    return render_template('merci_pharisien.html')


@app.route('/a_propos')
def a_propos():
    return render_template('a_propos.html')

@app.route('/connexion')
def connexion():
    return render_template('connexion.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)