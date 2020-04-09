# UniPizza - Käyttöohje

## Käyttäjätyypit

Sovelluksessa on kahdenlaisia käyttäjiä. Tavallisilla käyttäjillä sovelluksen näkymä on hyvin rajoitettu, ja tällä hetkellä ainoat tuetut toiminnot ovat menun katseleminen, tuotteiden lisääminen ostoskoriin ja tilauksen lähettäminen. Admin-käyttäjillä puolestaan on pääsy koko sovelluksen toiminnallisuuteen. Tämä käyttöohje kirjoitetaan admin-käyttäjän näkökulmasta, sillä ohjelmaa arvioivalle tämä on mielekkäämpi käyttötapaus.

## Käyttäjät

Uuden käyttäjän luominen tapahtuu joko oikeasta yläkulmasta **Create an Account**-linkin kautta (kirjautumaton tila) tai navigaatiopalkin **Create an Account**-linkin kautta (kirjautunut&admin -tila). Kaikki lomakkeen kentät paitsi mahdollisesti näkyvissä oleva **Admin**-checkbox ovat vaadittuja, joskin sähköpostin tai puhelinnumeron ei tarvitse olla "oikeassa muodossa", eli lomaketta ei ole validoitu kovin tarkkaan.

**Admin**-checkbox antaa käyttäjälle ylläpitäjän oikeudet jos se on valittuna käyttäjää luodessa. Checkbox on näkyvissä ainoastaan muille admin-käyttäjille.

Kirjautuminen ja uloskirjautuminen tapahtuvat samoin oikeasta yläkulmasta linkkien **Log In** ja **Log Out** kautta.

## Tuotteet ja Täytteet

### Lisääminen

Tuotteiden ja täytteiden lisääminen on näkyvissä admin-käyttäjille, ja näihin lomakkeisiin pääsee navigaatiopalkin linkkien kautta.

Täytteillä on ainoastaan nimi, joka on lomakkeen ainoana kenttänä myöskin vaadittu. Nimi voi olla mitä tahansa.

Tuotteilla on nimi ja hinta sekä lista täytteitä. Nimi ja hinta ovat vaadittuja, ja hinnan tulisi olla numeerinen. Hinnan desimaaliosan pituudella ei ole väliä, ja esimerkiksi arvo **12** muuntuu automaattisesti muotoon **12.0** tietokantaan tallennettaessa. Täytteitä tulee olla valittuna ainakin yksi.

### Listaaminen

Navigaatiopalkista löytyy myös linkit tuotteiden ja täytteiden listoille. Näistä tuotelista eli **Menu** on näkyvissä kaikille, kun taas täytelista eli **Ingredients** on admin-rajoitettu.

### Muokkaaminen ja Poistaminen

Listojen kautta onnistuu myös tuotteiden ja täytteiden muokkaaminen ja poistaminen. Muokkausnappi näyttää lomakkeen halutun kohteen muokkaamiseen, ja pyrkii parhaansa mukaan esitäyttämään lomakkeen muokattavan kohteen tiedoilla. Ainoa ei-täytetty kohta tällä hetkellä on täytteiden lista tuotetta muokatessa. Muokatessa kaikki kentät ovat vaadittuja, ja tuotetta muokatessa täytyy valita ainakin yksi täyte.

Poistolinkki ei turhia kysele tai varmistele, vaan poistaa kohteensa tietokannasta saman tien. Muuta käyttäjäsyötettä ei tarvita.

## Tilaukset

### Tilaaminen

Tilaaminen alkaa ruokalistasta. Listan tuotteita voi lisätä ostoskoriin, joka ilmestyy oikeaan yläkulmaan heti kun sinne lisätään jotain. Saman tuotteen voi lisätä useampaan kertaan, eikä lisäämisessä ole minkäänlaisia rajoituksia.

Ostoskorilistaukseen pääsee oikean yläkulman **Cart**-linkistä. Tässä näkymässä koria on vielä mahdollista tarkastella ja muokata. Listan tuotteiden **Remove**-nappi poistaa yhden yksikön kyseistä tuotetta korista.

Tilauksen voi vahvistaa **Confirm Order**-napilla, jolloin tilaus tallennetaan saman tien tietokantaan ja käyttäjä ohjataan varmistussivulle. Tilaukseen ei vielä tällä hetkellä liity käyttäjää, joten tilauksen voi tehdä kirjautumatta.

### Listaaminen

Admin-käyttäjillä on navigaatiopalkissaan **Orders**-linkki, jonka kautta pääsee katselemaan koko sovelluksen tilaushistoriaa.