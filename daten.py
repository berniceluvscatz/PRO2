import json
with open('filme.json) as jsondata:
    data = json.load(jsondata))

def speichern(film_lustig, film_traurig, film_spannend):

    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)
    except:
        eintraege = []

    eintrag = (film_lustig, film_traurig, film_spannend)

    eintraege.append(eintrag)

    with open("filme.jason", "w") as filme:
        json.dump(eintraege, filme)

    return "Eingabe gespeichert"
