import requests


def search_show(search_input):

    url = f"https://api.tvmaze.com/search/shows?q={search_input}"

    # Jos verkko-operaatio ei onnistu, käsitellään poikkeustilanne
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Verkko-ongelma.")
        return

    if response.status_code != 200:
        print(f"Palvelin ei vastaa kutsuun, status {response.status_code}")
        return

    # parsitaan response bodyn (vastauksen runko) json formaatista Pythonin vastaava tietorakenne
    # (listoja ja sanakirjoja)
    response_body = response.json()

    if len(response_body) < 1:
        print("Ei tuloksia")
        return

    # Tulostetaan ensimmäinen hakutulos
    ensimmainen_hakutulos = response_body[0]['show']['name']
    print(f"Ohjelman nimi: {ensimmainen_hakutulos}")

    # Tulostetaan kaikkien ohjelmien tietoja
    for item in response_body:
        print(item['show']['name'])
        print(f"Linkki: {item['show']['url']}")
        for genre in item['show']['genres']:
            print(f"Genre: {genre}")

search_show(input("Anna hakusana: "))