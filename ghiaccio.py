from operator import itemgetter


def main():
    with open("data/listino.txt") as f:
        lines = f.readlines()
    
    # carico file "listino.txt" in dizionario città
    cities = {}
    for line in lines:
        line = line.strip().split()
        city_id = line[0]
        # le chiavi del dizionario sono le lettere identificative delle città
        # i valori sono espressi a loro volta come dei dizionari
        cities[city_id] = {
            "name": " ".join(line[1:-1]),
            "offer": int(line[-1]),
            # aggiungo e inizializzo elementi per richieste successive
            "distance": None,
            "connected": False,
            "tradeoff": None
        }
    # setto distanza di Los Angeles a zero
    cities["a"]["distance"] = 0        
    
    with open("data/distanze.txt") as f:
        lines = f.readlines()
    
    # aggiorno dizionario città con informazioni prese dal file "distanze.txt"
    for line in lines:
        line = line.strip().split(":")
        city_id_start, city_id_end, distance = line[0][0], line[0][2], int(line[1])
        # tramite identificativi ottengo dizionario informazioni delle di città partenza e arrivo della tratta
        city_start = cities[city_id_start]
        city_end = cities[city_id_end]
        # calcolo la distanza da Los Angeles della città di arrivo (distanza città partenza + lunghezza tratta)
        city_end["distance"] = city_start["distance"] + distance
        # calcolo il rapporto offerta/distanza per la città di arrivo
        city_end["tradeoff"] = city_end["offer"] / city_end["distance"]
        # se la città di partenza è Los Angeles la città di arrivo è direttamente connessa
        if city_id_start == "a":
            cities[city_id_end]["connected"] = True
    
    # creo lista di dizionari con i valori del dizionario città (si può fare anche un for)
    cities_info = list(cities.values())

    # stessa cosa ma escludo Los Angeles
    cities_no_a = [info for city_id, info in cities.items() if city_id != "a"]

    # creo nuova lista dizionari escludendo città distanti 4000 km o più (si può fare anche con for)
    cities_4000 = [info for info in cities_info if info["distance"] < 4000]

    # estraggo nomi città connesse direttamente a Los Angeles (si può fare anche un for)
    connected = [info["name"] for info in cities_info if info["connected"]]

    # trovo città migliori/peggiori usando funzioni max e min sulle liste di dizionari create
    # la ricerca del massimo/minimo avviene sull'attributo del dizionario specificato tramite itemgetter
    city_best = max(cities_info, key=itemgetter("offer"))
    city_worst_tradeoff = min(cities_no_a, key=itemgetter("tradeoff"))
    city_best_4000 = max(cities_4000, key=itemgetter("offer"))

    print("Città direttamente connesse a Los Angeles:")
    for name in connected:
        print(name)

    print("Per raggiungere l'offerta migliore, {}, servono: {} km".format(city_best["name"], city_best["distance"]))
    print("La città con il peggior rapporto è {}".format(city_worst_tradeoff["name"]))
    print("La migliore offerta entro 4000 km è a {}".format(city_best_4000["name"]))  


if __name__ == "__main__":
    main()
