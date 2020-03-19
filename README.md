# UniPizza
Tietokantasovellus 2020 -harjoitustyö

## Aihekuvaus

Tarkoituksena on luoda nettitilaustoiminnallisuus kuvitteelliselle pizzapalvelulle. Käyttäjän on mahdollista kirjautua sivulle jolloin hänen tietonsa haetaan automaattisesti tietokannasta, ja samoin käyttäjä voi halutessaan rekisteröityä toistotilaamisen helpottamiseksi ja mahdollisen kanta-asiakasohjelman etuja hyödyntääkseen. Tilaamisen täytyy kuitenkin onnistua myös kirjautumatta.

Ensin käyttäjä valitsee haluamansa tuotteet verkkokaupasta ja siirtyy sitten tilaamaan. Tilausta voi muokata aina tilauksen vahvistamiseen ja ravintolalle lähettämiseen asti, mutta heti vahvistamisen jälkeen tilaus on lukittu ja tallennettu tietokantaan.

Jokainen tuote on tallennettu erikseen tietokantaan, ja jokaisen tuotteen täytteet on eritelty vielä omiksi tietokantaolioikseen esimerkiksi lisätäytteiden tukemisen helpottamiseksi. Tilatessa kysytään ja varmistetaan käyttäjän yhteystiedot, tilauksen sisältö ja toimitustapa. Jokainen tilaus tallennetaan erikseen tietokantaan.

Admin-puolella ainakin täytteiden ja tuotteiden poistaminen ja lisääminen tulisi onnitua. Tilaushistorian tarkastelemisen pitäisi myös olla mahdollista. Lisäksi jonkinlainen järjestelmä kanta-asiakaspisteiden kertymiseen ja käyttämiseen voitaisiin toteuttaa perustoiminnallisuuden päälle.

## Resurssit

[Heroku](https://unipizza.herokuapp.com/)

[Tietokantakaavio](https://vapsolon.github.io/UniPizza/docut/Tietokantakaavio.png)

[Käyttötapaukset](https://github.com/vapsolon/UniPizza/blob/master/docut/K%C3%A4ytt%C3%B6tapaukset.md)