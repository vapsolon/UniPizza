# UniPizza
Tietokantasovellus 2020 -harjoitustyö

## Aihekuvaus

Tarkoituksena on luoda nettitilaustoiminnallisuus kuvitteelliselle pizzapalvelulle. Käyttäjän on mahdollista kirjautua sivulle jolloin hänen tietonsa haetaan automaattisesti tietokannasta, ja samoin käyttäjä voi halutessaan rekisteröityä toistotilaamisen helpottamiseksi ja mahdollisen kanta-asiakasohjelman etuja hyödyntääkseen. Tilaamisen täytyy kuitenkin onnistua myös kirjautumatta.

Ensin käyttäjä valitsee haluamansa tuotteet verkkokaupasta ja siirtyy sitten tilaamaan. Tilausta voi muokata aina tilauksen vahvistamiseen ja ravintolalle lähettämiseen asti, mutta heti vahvistamisen jälkeen tilaus on lukittu ja tallennettu tietokantaan.

Jokainen tuote on tallennettu erikseen tietokantaan, ja jokaisen tuotteen täytteet on eritelty vielä omiksi tietokantaolioikseen esimerkiksi lisätäytteiden tukemisen helpottamiseksi. Tilatessa kysytään ja varmistetaan käyttäjän yhteystiedot, tilauksen sisältö ja toimitustapa. Jokainen tilaus tallennetaan erikseen tietokantaan.

Admin-puolella ainakin täytteiden ja tuotteiden poistaminen ja lisääminen tulisi onnitua. Tilaushistorian tarkastelemisen pitäisi myös olla mahdollista. Lisäksi jonkinlainen järjestelmä kanta-asiakaspisteiden kertymiseen ja käyttämiseen voitaisiin toteuttaa perustoiminnallisuuden päälle.

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