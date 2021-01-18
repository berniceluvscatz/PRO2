from flask import Flask
from flask import render_template
from flask import request

from daten import speichern

app = Flask("filmzer")


@app.route('/')
def main():
    return "Willkommen!"

@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():

    if request.method == 'POST':
        aktivitaet = request.form['aktivitaet']
        dauer = request.form['dauer']
        antwort = speichern(aktivitaet, dauer)
        return 'Gespeicherte Daten: <br>' + str(antwort)

    return render_template('eingabe.html', app_name="Tracker! - Eingabe")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, render_template
def main():
    return render_template('index.html')