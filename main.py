from flask import Flask
from flask import render_template
from flask import request

app = Flask("Filmzer")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
import json
from daten import datenbank

@app.route('/')
def index():
    return render_template('index.html', app_name="Filmzer")

@app.route('/eingabe')
def eingabe():
    return render_template('eingabe.html', app_name="Eingabeformular")

@app.route("/film/<name>", methods=['GET', 'POST'])
def film(name):
    filme_json = filmeladen()
    titel=filme_json[name]["titel"]
    film_lustig=filme_json[name]["film_lustig"]
    film_traurig=filme_json[name]["film_traurig"]
    film_spannend=filme_json[name]["film_traurig"]

    if request.method == 'POST':
        user_lustig = request.form['user_lustig']
        user = request.form['produktname']
        produktpreis = request.form['produktpreis']
        antwort = speichern(zahl_1, produktname, produktpreis)
        return render_template('resultat.html')
        titel=titel,
        deutscher_titel=deutscher_titel,
        genre=genre,
        laenge=laenge,
        jahr=jahr,
        regie=regie,
        imdb_rating

    return render_template('resultat.html')
    titel=titel,\
    deutscher_titel=deutscher_titel,\
    genre=genre,\
    laenge=laenge,\
    jahr=jahr,\
    regie=regie,
    imdb_rating=imdb_rating
    return render_template('index.html')

# Create your views here.
def index(request):
    return render(request,'index.html')

def lustig(request):
   category=['1']
   film=filme.objects.filter(category=category)
   return render(request,'eingabe.html')

def traurig(request):
    category=['2']
    film=filme.objects.filter(category=category)
    return render(request,'eingabe.html')

def spannend(request):
    category=['3']
    film=filme.objects.filter(category=category)
    context = {'film':film}
    return render(request,'eingabe.html',context)

def resultat(request):
    res = 0
    if request.method == 'POST':
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])

        res =  abs(10-(val1-val2))

    context = {'res':res}
    return render(request,'eingabe.html',context)

