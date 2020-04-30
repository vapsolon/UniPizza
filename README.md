# UniPizza
Tietokantasovellus 2020 -harjoitustyö

## Aihekuvaus

UniPizza on nettitilauspalvelu kuvitteelliselle pizzerialle.

Sovelluksen toiminnallisuus on jaettu kahteen osaan, julkisesti kaikille näkyvään käyttöliittymään sekä ylläpitäjille rajattuun admin-puoleen.

Sovelluksen julkisessa osassa käyttäjän on mahdollista tarkastella palvelun ruokalistaa, lisätä listalta tuotteita ostoskoriin ja lähettää lopulta ostoskorin kautta tilaus itse ravintolaan. Lisäksi käyttäjillä on mahdollisuus käyttäjätunnusten luomiseen, jolloin tilauksien yhteyteen tallentuu myös tieto tilauksen tehneestä käyttäjästä, ja heille avautuu mahdollisuus tarkastella omaa tilaushistoriaansa.

Admin-puolella toiminnallisuus on paljon laajempi. Ylläpitäjät voivat lisätä sovelluksen tietokantaan täytteitä ja edelleen näistä täytteistä koostuvia tuotteita. Samoin ylläpitäjät voivat luoda käyttäjätilejä ja tarvittaessa antaa näille käyttäjille admin-oikeudet. Lisäksi ylläpitäjät voivat tarkastella erilaisia tilastoja, kuten rekisteröityneiden käyttäjien ja varmistettujen tilausten listoja.

## Resurssit

[Heroku](https://unipizza.herokuapp.com/)

[Käyttöohje](https://github.com/vapsolon/UniPizza/blob/master/docut/Käyttöohje.md)

[Tietokantakaavio](https://vapsolon.github.io/UniPizza/docut/Tietokantakaavio.png)

[Käyttötapaukset](https://github.com/vapsolon/UniPizza/blob/master/docut/K%C3%A4ytt%C3%B6tapaukset.md)

Testikäyttäjätiedot:

* Normaalikäyttäjä: email: **normal**, password: **pass**
* Admin-käyttäjä: email: **test**, password **pass**

### Yhteenvetokyselyt
Kaksi vaadittua yhteenvetokyselyä löytyvät tiedostoista **application/ingredient/models.py** ja **application/product/models.py**. Näiden tulokset on nähtävissä statistiikkasivuilla, joihin on linkki täytelistauksen ja menun alla.

## Asennus

Kloonaamisen jälkeen riippuvuuksien asentaminen ajamalla ```pip install -r requirements.txt``` saa sovelluksen käyttökuntoon. Toiminnallisuus on kuitenkin rajoitettua, sillä mukana ei tule valmista tietokantaa ja oletuksena admin-käyttäjien luominen sallitaan vain muille admin-käyttäjille, joten ensimmäisen adminin luominen vaatii pientä kikkailua.

Admin-luomisen saa näkyviin kaikille vaihtamalla tiedoston **application\auth\views.py** rivin 40 admin-check muotoon ```admin = True```, jolloin kirjautumaton käyttäjä voi luodessaan uutta käyttäjää antaa itselleen admin-oikeudet, ja sovelluksen koko toiminnallisuus aukeaa.